<#
Create a separate PPTX with conservative native animation using Windows PowerPoint.
File automation only: no mouse/keyboard operations, downloads, or macro execution.
Use -DryRun for package/plan checks without starting PowerPoint.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$InputPptx,
    [Parameter(Mandatory=$true)][string]$Plan,
    [Parameter(Mandatory=$true)][string]$OutputPptx,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Read-Field($Object, [string]$Name, $Default) {
    if ($null -eq $Object) { return $Default }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) { return $Default }
    return $property.Value
}

function Read-ZipXml($Archive, [string]$Name) {
    $entry = $Archive.GetEntry($Name)
    if ($null -eq $entry) { throw "Missing PPTX part: $Name" }
    $stream = $entry.Open()
    $settings = New-Object System.Xml.XmlReaderSettings
    $settings.DtdProcessing = [System.Xml.DtdProcessing]::Prohibit
    $settings.XmlResolver = $null
    $reader = [System.Xml.XmlReader]::Create($stream, $settings)
    try {
        $document = New-Object System.Xml.XmlDocument
        $document.XmlResolver = $null
        $document.Load($reader)
        return ,$document
    } finally { $reader.Dispose(); $stream.Dispose() }
}

$inputPath = (Resolve-Path -LiteralPath $InputPptx).Path
$planPath = (Resolve-Path -LiteralPath $Plan).Path
$outputPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputPptx)
if ([System.IO.Path]::GetExtension($inputPath).ToLowerInvariant() -ne '.pptx' -or
    [System.IO.Path]::GetExtension($outputPath).ToLowerInvariant() -ne '.pptx') {
    throw 'Input and output must be .pptx files.'
}
if ($inputPath -eq $outputPath -or (Test-Path -LiteralPath $outputPath)) {
    throw 'Output must be a new path; existing files are never overwritten.'
}
$motionPlan = Get-Content -LiteralPath $planPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ((Read-Field $motionPlan 'version' 0) -ne 1) { throw 'Plan version must be 1.' }
$items = @(Read-Field $motionPlan 'slides' @())
if ($items.Count -eq 0) { throw 'Plan must contain at least one slide.' }
$effectMap = @{ fade = 10; appear = 1 }
$triggerMap = @{ click = 1; with_previous = 2; after_previous = 3 }
$transitionMap = @{ fade = 3849; none = 0 }
$prepared = New-Object System.Collections.Generic.List[object]
$seenSlides = @{}
Add-Type -AssemblyName System.IO.Compression.FileSystem
$archive = [System.IO.Compression.ZipFile]::OpenRead($inputPath)
try {
    if ($archive.Entries.Count -gt 10000 -or ($archive.Entries | Measure-Object Length -Sum).Sum -gt 536870912) {
        throw 'Input exceeds the supported package size.'
    }
    $pres = Read-ZipXml $archive 'ppt/presentation.xml'
    $rels = Read-ZipXml $archive 'ppt/_rels/presentation.xml.rels'
    $ns = New-Object System.Xml.XmlNamespaceManager($pres.NameTable)
    $ns.AddNamespace('p', 'http://schemas.openxmlformats.org/presentationml/2006/main')
    $ns.AddNamespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')
    $slideNodes = $pres.SelectNodes('/p:presentation/p:sldIdLst/p:sldId', $ns)
    foreach ($item in $items) {
        $rawNumber = Read-Field $item 'slide' 0
        if ([double]$rawNumber -ne [int]$rawNumber) { throw 'Slide number must be an integer.' }
        $number = [int]$rawNumber
        if ($number -lt 1 -or $number -gt $slideNodes.Count -or $seenSlides.ContainsKey($number)) {
            throw "Invalid or repeated slide number: $number"
        }
        $seenSlides[$number] = $true
        $rid = $slideNodes[$number-1].GetAttribute('id', $ns.LookupNamespace('r'))
        $relationship = @($rels.DocumentElement.ChildNodes | Where-Object {
            $_.NodeType -eq [System.Xml.XmlNodeType]::Element -and
            $_.LocalName -eq 'Relationship' -and
            $_.NamespaceURI -eq 'http://schemas.openxmlformats.org/package/2006/relationships' -and
            $_.GetAttribute('Id') -eq $rid
        })
        if ($relationship.Count -ne 1) { throw "Cannot resolve slide $number" }
        $baseUri = [Uri]'https://package.invalid/ppt/presentation.xml'
        $partUri = New-Object Uri($baseUri, $relationship[0].GetAttribute('Target'))
        if ($partUri.Host -ne $baseUri.Host) { throw 'External slide target is unsupported.' }
        $partName = [Uri]::UnescapeDataString($partUri.AbsolutePath.TrimStart('/'))
        $slideXml = Read-ZipXml $archive $partName
        $sns = New-Object System.Xml.XmlNamespaceManager($slideXml.NameTable)
        $sns.AddNamespace('p', $ns.LookupNamespace('p'))
        $props = $slideXml.SelectNodes('//p:cNvPr', $sns)
        $effectItems = @(Read-Field $item 'effects' @())
        if ($effectItems.Count -gt 0 -and $null -ne $slideXml.SelectSingleNode('/p:sld/p:timing', $sns)) {
            throw "Slide $number already has native timing. Use an unanimated baseline or preserve/edit it with another backend."
        }
        $effects = New-Object System.Collections.Generic.List[object]
        $seenTargets = @{}
        foreach ($entry in $effectItems) {
            $shapeId = Read-Field $entry 'shape_id' $null
            $shapeName = Read-Field $entry 'shape_name' $null
            if (($null -eq $shapeId) -eq ($null -eq $shapeName)) {
                throw 'Each effect requires exactly one of shape_id or shape_name.'
            }
            $matches = @($props | Where-Object {
                if ($null -ne $shapeId) { $_.GetAttribute('id') -eq [string]$shapeId }
                else { $_.GetAttribute('name') -ceq [string]$shapeName }
            })
            if ($matches.Count -ne 1) { throw "Slide $number has missing or ambiguous target: $shapeId $shapeName" }
            $prop = $matches[0]
            $shapeNode = $prop.ParentNode.ParentNode
            if ($shapeNode.ParentNode.LocalName -ne 'spTree') {
                throw 'Only top-level slide objects are supported. Animate a group as one object.'
            }
            $resolvedId = [int]$prop.GetAttribute('id')
            if ($seenTargets.ContainsKey($resolvedId)) { throw 'Only one entrance effect per object is supported.' }
            $seenTargets[$resolvedId] = $true
            $kind = [string](Read-Field $entry 'effect' 'fade')
            $trigger = [string](Read-Field $entry 'trigger' 'click')
            $duration = [double](Read-Field $entry 'duration' 0.4)
            $delay = [double](Read-Field $entry 'delay' 0.0)
            if (-not $effectMap.ContainsKey($kind) -or -not $triggerMap.ContainsKey($trigger)) {
                throw "Unsupported effect/trigger: $kind / $trigger"
            }
            if ([double]::IsNaN($duration) -or [double]::IsInfinity($duration) -or $duration -lt 0.01 -or $duration -gt 5 -or
                [double]::IsNaN($delay) -or [double]::IsInfinity($delay) -or $delay -lt 0 -or $delay -gt 30) {
                throw 'Duration must be 0.01..5 s and delay 0..30 s.'
            }
            $effects.Add([pscustomobject]@{ id=$resolvedId; effect=$effectMap[$kind]; trigger=$triggerMap[$trigger]; duration=$duration; delay=$delay })
        }
        $transition = Read-Field $item 'transition' $null
        $transitionValue = $null
        $transitionDuration = 0.4
        if ($null -ne $transition) {
            $kind = [string](Read-Field $transition 'effect' 'fade')
            if (-not $transitionMap.ContainsKey($kind)) { throw "Unsupported transition: $kind" }
            $transitionValue = $transitionMap[$kind]
            $transitionDuration = [double](Read-Field $transition 'duration' 0.4)
            if ([double]::IsNaN($transitionDuration) -or [double]::IsInfinity($transitionDuration) -or $transitionDuration -lt 0.01 -or $transitionDuration -gt 5) {
                throw 'Transition duration must be 0.01..5 seconds.'
            }
        }
        $prepared.Add([pscustomobject]@{ number=$number; effects=$effects.ToArray(); transition=$transitionValue; transitionDuration=$transitionDuration })
    }
} finally { $archive.Dispose() }

if ($DryRun) {
    [pscustomobject]@{status='plan-validated';slides=$prepared.Count;powerpointStarted=$false} | ConvertTo-Json
    exit 0
}
if (@(Get-Process -Name POWERPNT -ErrorAction SilentlyContinue).Count -gt 0) {
    throw 'PowerPoint is already running. This helper does not attach to or close user sessions. Use an available native editing workflow, or keep the static deck until PowerPoint is closed.'
}
$app = $null
$deck = $null
$verification = $null
try {
    $app = New-Object -ComObject PowerPoint.Application
    $app.AutomationSecurity = 3
    $deck = $app.Presentations.Open($inputPath, -1, 0, 0)
    foreach ($item in $prepared) {
        $slide = $deck.Slides.Item($item.number)
        if ($null -ne $item.transition) {
            $slide.SlideShowTransition.EntryEffect = $item.transition
            if ($item.transition -ne 0) { $slide.SlideShowTransition.Duration = [single]$item.transitionDuration }
            $slide.SlideShowTransition.AdvanceOnClick = -1
            $slide.SlideShowTransition.AdvanceOnTime = 0
        }
        foreach ($entry in $item.effects) {
            $target = $null
            for ($index = 1; $index -le $slide.Shapes.Count; $index++) {
                $candidate = $slide.Shapes.Item($index)
                if ($candidate.Id -eq $entry.id) { $target = $candidate; break }
            }
            if ($null -eq $target) { throw "PowerPoint could not resolve shape ID $($entry.id)" }
            $effect = $slide.TimeLine.MainSequence.AddEffect($target, $entry.effect, 0, $entry.trigger)
            $effect.Timing.Duration = [single]$entry.duration
            $effect.Timing.TriggerDelayTime = [single]$entry.delay
        }
    }
    $outputDir = Split-Path -Parent $outputPath
    if (-not (Test-Path -LiteralPath $outputDir)) { [void](New-Item -ItemType Directory -Path $outputDir) }
    $deck.SaveAs($outputPath, 24)
    $deck.Close()
    $deck = $null
    $verification = $app.Presentations.Open($outputPath, -1, 0, 0)
    foreach ($item in $prepared) {
        $slide = $verification.Slides.Item($item.number)
        if ($null -ne $item.transition -and $slide.SlideShowTransition.EntryEffect -ne $item.transition) { throw 'Saved transition differs from plan.' }
        if ($item.effects.Count -gt 0 -and $slide.TimeLine.MainSequence.Count -ne $item.effects.Count) { throw 'Saved effect count differs from plan.' }
        for ($index = 1; $index -le $item.effects.Count; $index++) {
            $expected = $item.effects[$index-1]
            $actual = $slide.TimeLine.MainSequence.Item($index)
            if ($actual.Shape.Id -ne $expected.id -or $actual.EffectType -ne $expected.effect -or
                $actual.Timing.TriggerType -ne $expected.trigger -or
                [Math]::Abs($actual.Timing.Duration - $expected.duration) -gt 0.03 -or
                [Math]::Abs($actual.Timing.TriggerDelayTime - $expected.delay) -gt 0.03) {
                throw "Saved effect settings differ on slide $($item.number), effect $index"
            }
        }
    }
    [pscustomobject]@{status='saved-and-reopened';output=$outputPath;slides=$verification.Slides.Count;motionSlides=$prepared.Count;playbackVerified=$false} | ConvertTo-Json
} finally {
    if ($null -ne $verification) { $verification.Close(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($verification) }
    if ($null -ne $deck) { $deck.Close(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($deck) }
    if ($null -ne $app) {
        if ($app.Presentations.Count -eq 0) { $app.Quit() }
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($app)
    }
}
