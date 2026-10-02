#!/usr/bin/env python3
"""Check explicit sRGB text/background pairs. Standard library only."""
import argparse
import json
import math
import re
from pathlib import Path


def rgb(value):
    if not isinstance(value, str) or not re.fullmatch(r"#?[0-9a-fA-F]{6}", value):
        raise ValueError(f"Expected six-digit sRGB hex, received {value!r}")
    value = value.lstrip("#")
    return [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def luminance(value):
    channels = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb(value)]
    return sum(c * w for c, w in zip(channels, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check_palette(palette):
    if not isinstance(palette, dict):
        raise ValueError("Each palette must be an object")
    colors = palette["colors"]
    if not isinstance(colors, dict) or not colors:
        raise ValueError("Palette colors must be a nonempty object")
    for value in colors.values():
        rgb(value)
    pairs = palette.get("pairs", [
        {"fg": "text", "bg": "background", "minimum": 4.5},
        {"fg": "muted", "bg": "background", "minimum": 4.5},
        {"fg": "text", "bg": "surface", "minimum": 4.5},
        {"fg": "on_accent", "bg": "accent", "minimum": 4.5},
    ])
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("Palette pairs must be a nonempty array")
    results = []
    for pair in pairs:
        if not isinstance(pair, dict):
            raise ValueError("Each contrast pair must be an object")
        minimum = float(pair.get("minimum", 4.5))
        if not math.isfinite(minimum) or minimum < 1 or minimum > 21:
            raise ValueError("Contrast minimum must be between 1 and 21")
        ratio = contrast(colors[pair["fg"]], colors[pair["bg"]])
        results.append({**pair, "ratio": round(ratio, 3), "pass": ratio >= minimum})
    return {"name": palette.get("name", "custom"), "pairs": results,
            "pass": all(r["pass"] for r in results)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("palette", type=Path, help="One palette object, array, or {palettes:[...]}")
    args = parser.parse_args()
    data = json.loads(args.palette.read_text(encoding="utf-8-sig"))
    if not isinstance(data, (dict, list)):
        raise ValueError("Input must be a palette object or nonempty palette array")
    palettes = data if isinstance(data, list) else data.get("palettes", [data])
    if not isinstance(palettes, list) or not palettes:
        raise ValueError("At least one palette is required")
    results = [check_palette(p) for p in palettes]
    print(json.dumps({"palettes": results, "pass": all(r["pass"] for r in results),
                      "scope": "Explicit opaque sRGB pairs only; not a full accessibility audit."},
                     ensure_ascii=True, indent=2))
    return 0 if all(r["pass"] for r in results) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        raise SystemExit(f"Palette input error: {exc}")
