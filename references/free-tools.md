# Free tools and reference-driven design

Checked 2026-10-02. Choose tools for the visual problem and the available environment, not to maximize the number used. The skill should work without buying a template, subscribing to a design service or calling a paid image API. A hosted agent itself may still have a subscription or usage cost. Host tool instructions remain authoritative.

## Select a route

Choose the graphic required by the claim before the tool. Preserve distributions, pairing and uncertainty even when a specialized plot must be exported as SVG/PNG instead of a native chart. Retain its data and plotting source plus editable slide annotations. Set the intended placement width before plotting: a 10 pt label in an 8-inch export becomes effectively 5 pt at 4 inches. Inspect placed labels, lines and legends at final slide size.

| Need | Suitable free/open-source option | Source and output | Important boundary |
|---|---|---|---|
| Editable PPTX text, shapes, tables and common charts | [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) when no host presentation engine is prescribed | JavaScript source → native PPTX; [MIT license](https://github.com/gitbrent/PptxGenJS/blob/master/LICENSE) | Use documented APIs. It is an authoring option, not an aesthetic reviewer or proof of native animation support. |
| Process, architecture or relationship diagram | [diagrams.net / draw.io](https://www.drawio.com/docs/about/) | Preserve `.drawio` source; export SVG or reconstruct native PowerPoint shapes; [terms](https://www.drawio.com/trust/terms-of-use/) | SVG in a slide is not automatically an individually editable PowerPoint diagram. Preserve labels and exact connections. |
| Simple reproducible process or sequence draft | [Mermaid](https://mermaid.js.org/intro/) | Preserve text definition; render SVG; [MIT license](https://github.com/mermaid-js/mermaid/blob/develop/LICENSE) | Auto-layout is a starting point. Inspect crossings, label spacing and reading order; rebuild natively when slide editing is required. |
| Scientific plots beyond common native chart types | [Matplotlib](https://matplotlib.org/) | Preserve data and plotting source; export SVG/PDF plus a PNG fallback; [license](https://matplotlib.org/stable/project/license.html) | Keep native PowerPoint charts for ordinary editable comparisons when supported. Never create error bars without underlying evidence. |
| Refine an existing vector illustration or icon composition | [Inkscape](https://inkscape.org/acerca-de/) | Preserve SVG source; export SVG/PDF/PNG as appropriate; free software under the GPL | Respect the source asset's license. Vector format alone does not imply native PowerPoint editability. |
| Open and render a static deck without Office | [LibreOffice Impress](https://www.libreoffice.org/discover/impress/) | PPTX import and PDF/render review; [license information](https://www.libreoffice.org/licenses/) | Check font substitution, layout and compatibility. Its rendering does not establish PowerPoint animation playback. |
| A free font covering English and Korean | [Noto CJK](https://github.com/notofonts/noto-cjk) | Use an installed Noto Sans KR/CJK Korean family; check the selected font's license | Verify the installed family name, glyph coverage and recipient environment. Do not silently download or bundle unrelated fonts. |

These are selectable pathways, not bundled integrations or a claim that every tool was executed for the example. Check current official documentation, installed versions and export support before use. The included example uses the host presentation engine and PowerPoint. Image generation is not required; its earlier diagram draft is documented separately from the native final slide.

## Turn a reference into a design decision

For a new art direction, inspect actual pixels from relevant external references. Record a cover, a typical body slide and a difficult evidence or process slide when available. A title thumbnail cannot establish body-slide quality. Use [reference-library.md](reference-library.md), then search for the topic and visual task.

Save an entry in the plan or [reference ledger](../assets/design-reference-template.md) for each selected reference: URL, access date, inspection depth, observed composition, principle adapted, traits rejected and asset rights if any assets are reused. Keep inspiration separate from copying. Free software does not make a third-party template free to redistribute.

For example, a baseline → distillation → INT8 process can use open columns, aligned labels, small stage markers, fine directional connectors and one caveat. Those are composition choices. The nodes and arrows must still match the scientific source; never infer model internals from a stylish reference. The public example illustrates one useful direction, not a mandatory layout for every method slide.

## Three practical combinations

1. **Editable research seminar:** native PPTX shapes for a simple process, native table/chart for summary data, one coherent installed font family. Browse reference slides for rhythm and spacing. No image-generation service is necessary.
2. **Data-heavy conference talk:** Matplotlib for the specialized scientific figure, source data and code retained; native PPTX titles, annotations and simple comparisons. Use the same palette and typography across both tools.
3. **Architecture explanation:** diagrams.net or Mermaid to clarify relationships, then native reconstruction if every node must be editable. Use Inkscape only when vector refinement materially improves a supplied asset.

If a selected tool is unavailable, use the supported alternative and state the effect on deliverables. Do not claim an installation, integration, export or visual check that was not performed. Do not add animation merely to compensate for a weak composition.

## English and Korean

These tool choices do not set the presentation language. Use real target-language copy, select fonts with the needed glyphs, and retain source identifiers where technically meaningful. Adapt column widths, line breaks, chart labels and notes for each edition. Render both; verify intended headline and takeaway line counts plus actual table/chart labels. Apply [typography.md](typography.md) after the last export.
