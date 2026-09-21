# WhatFontIs-Bench — A Synthetic Benchmark for Font Family Identification

A synthetic test set for **font family identification**: a single word, set in a known font, printed or painted on real
surfaces and in real scenes, with the exact font, the text and the position of every letter recorded for each
image.

Made by [WhatFontIs](https://www.whatfontis.com), the [font finder](https://www.whatfontis.com) that identifies
fonts from images, to measure how well a tool can [find the font](https://www.whatfontis.com) in a real-looking
photo.

**Official page:** [whatfontis.com/WhatFontIs-Bench.html](https://www.whatfontis.com/WhatFontIs-Bench.html)

## Versions

| Version | Fonts | Images | Data | Images download |
|---|---|---|---|---|
| **v1.0** | 600 | 11,995 | [`v1/`](v1) | [release v1.0](https://github.com/whatfontis/WhatFontIs-Bench/releases/tag/v1.0) |

Each version is a separate folder and a separate release, so results on different versions are not mixed.
The rest of this page describes **v1.0**.

## v1.0 contents

| | |
|---|---|
| Fonts | 600: 200 sans-serif, 200 serif, 100 slab serif, 100 monospaced |
| Font sources | 215 Adobe Fonts, 191 Creative Fabrica, 183 Google Fonts, 11 DaFont (commercial-use license) |
| Images | 11,995 (20 per font; *Colt Soft Regular* has 15, see *v1.0 known gaps*) |
| Text | one word per image, 7–12 letters, taken from COCO-Text v2 |
| Size | long side 442–1998 px (never over 2000), short side at least 301 px |

Each font has 20 images:

| Type | Easy | Medium | Hard | Per font |
|---|---|---|---|---|
| **texture**: the word printed or painted straight on a close-up photo of a real surface (wood, plaster, concrete, brick, metal, fabric, leather, paper, cardboard) | 3 | 2 | 5 | 10 |
| **scene**: the word painted on a wall inside a real photo (rooms, shops, facades, workshops) | 1 | 2 | 3 | 6 |
| **object**: the word on a printed object (label, box, book cover, poster, menu, shop sign, packaging, business card, painted wall) over a real photo | 1 | 1 | 2 | 4 |

Difficulty levels:

- **easy**: capital height 160–220 px, little blur and noise, JPEG quality 88–95, almost even light
- **medium**: capital height 130–180 px, blur σ 0.3–0.8, noise 1.5–3.5, JPEG 78–90, uneven light
- **hard**: capital height 100–140 px, blur σ 0.7–1.3, noise 3–6, JPEG 65–80, strong uneven light, and often
  a cast shadow over part of the word (3,354 images), a glare spot (2,747) or light print wear (357)

When a scene wall is too small for a long word at the level's size, that image uses the next smaller size
range, so a few easy scene images have capitals of 130–160 px and a few medium ones of 100–130 px.

The images are frontal, with no slant or perspective, so an upright font never looks italic. Texture and scene
images add only a small camera deviation, as in a real photo taken straight on: corners moved at most 1.5 %,
rotation at most 1°. The exact transform is saved in the labels.

Text contrast is at least 70 grey levels (50 on the hard level). No letter is clipped. Fonts that only have
capitals (107 of them) are written in capitals.

## v1.0 results: WhatFontIs API (api2)

These are the results of the [WhatFontIs](https://www.whatfontis.com) API (api2) on all 11,995 images, September 2026.
The API searched its whole catalogue of **over 1.2 million fonts**, not only the 600 fonts of this set.

A result counts as correct when it is the right font family, in any weight or from any source: an image in
Roboto Bold answered with Roboto Regular is correct, answered with Arial Bold it is wrong. The 3 images where no
letters were found count as misses.

| | Images | Correct at 1 | In top 5 | In top 20 |
|---|---|---|---|---|
| **All images** | 11,995 | **83.7 %** | **93.3 %** | **96.5 %** |
| texture | 5,997 | 83.6 % | 93.3 % | 96.3 % |
| scene | 3,599 | 82.4 % | 92.3 % | 96.0 % |
| object | 2,399 | 85.9 % | 95.0 % | 97.5 % |
| easy | 2,995 | 85.2 % | 93.9 % | 97.4 % |
| medium | 3,000 | 83.3 % | 92.8 % | 96.0 % |
| hard | 6,000 | 83.1 % | 93.3 % | 96.3 % |
| sans-serif | 4,000 | 75.7 % | 88.7 % | 94.2 % |
| serif | 4,000 | 84.0 % | 95.1 % | 97.7 % |
| slab serif | 1,995 | 95.0 % | 98.5 % | 99.0 % |
| monospaced | 2,000 | 87.8 % | 94.0 % | 96.1 % |

## v1.0 download

The images are in the release [**v1.0**](https://github.com/whatfontis/WhatFontIs-Bench/releases/tag/v1.0)
as four zip files (they are release downloads, not files in the repository):

| File | Size | Images |
|---|---|---|
| [WhatFontIs-Bench_v1.0_images_part1.zip](https://github.com/whatfontis/WhatFontIs-Bench/releases/download/v1.0/WhatFontIs-Bench_v1.0_images_part1.zip) | 466 MB | 00000–02998 |
| [WhatFontIs-Bench_v1.0_images_part2.zip](https://github.com/whatfontis/WhatFontIs-Bench/releases/download/v1.0/WhatFontIs-Bench_v1.0_images_part2.zip) | 470 MB | 02999–05997 |
| [WhatFontIs-Bench_v1.0_images_part3.zip](https://github.com/whatfontis/WhatFontIs-Bench/releases/download/v1.0/WhatFontIs-Bench_v1.0_images_part3.zip) | 460 MB | 05998–08996 |
| [WhatFontIs-Bench_v1.0_images_part4.zip](https://github.com/whatfontis/WhatFontIs-Bench/releases/download/v1.0/WhatFontIs-Bench_v1.0_images_part4.zip) | 604 MB | 08997–11994 |

With the GitHub CLI: `gh release download v1.0 --repo whatfontis/WhatFontIs-Bench`

Unzip all four into `v1/`; they create `v1/scenes/NNNNN.jpg`. To also get the text crops
(the word cut out of each image, unscaled), run:

```
pip install pillow
python tools/make_crops.py v1
```

This writes `v1/crops/NNNNN.png`.

## v1.0 files

| File | What it holds |
|---|---|
| `v1/labels.jsonl` | one line per image, with everything about it (see below) |
| `v1/annotations.json` | the same set in COCO format: `images`, `categories` (one per font), `annotations` (word box, text, letters) |
| `v1/fonts.json` | the 600 fonts: title, family, source, category, capitals-only flag, WhatFontIs page, number of images |
| `v1/backgrounds.json` | the 153 background photos used, with source page, author and license |
| `words.txt` | the word list the texts were drawn from (shared by all versions) |
| `v1/specimens/` | ten sheets showing all 600 fonts, 60 per sheet |
| `tools/make_crops.py` | cuts the text crops out of the images |

Font files are **not** included.

### labels.jsonl

The main fields of each line:

- **Image and font**
  - `id`, `image` (`scenes/NNNNN.jpg`, relative to `v1/`), `width`, `height`
  - `text`: the word in the image
  - `title`, `family`, `source`, `category`, `caps_only`, `url`: the font
  - `type` (`texture` / `scene` / `object`), `difficulty` (`easy` / `medium` / `hard`)
- **Where the text is**
  - `crop_box`: `[x0, y0, x1, y1]` of the text crop
  - texture and scene images: `ink_quad` (the word's four corners) and `char_quads` (four corners per letter)
  - object images: `ink_box`, `word_box` and `chars` (letter boxes), plus `object_box`
- **How it was made**
  - `cap_height_px`, `font_px`, `ink_rgb`, `contrast`, `blur_sigma`, `noise_sigma`, `jpeg_quality`
  - `effects` / `hard_effects`: the hard-level problems applied
  - `camera`: `corner_jitter`, `rotation_deg`, `homography`
- **Background**
  - texture images: `surface`, `texture`, `texture_source`, `texture_license`
  - scene images: `scene_source_file`, `scene_source`, `scene_page`, `scene_license`
  - object images: `scene` (object kind), `material`, `extras`, `background` (`file`, `source`, `page`, `license`)

The background identifiers match the `id` field in `backgrounds.json`.

## v1.0 known gaps

- *Colt Soft Regular* has 15 images instead of 20: it is so wide that a 7-letter word with 160 px capitals
  does not fit in 2000 px, so 5 easy images are missing.
- The scene images reuse a limited number of real scenes (each scene appears many times, with a different
  word, font, position and light).
- Some fonts in the set are close look-alikes of other fonts that exist under different names.

## Licenses and credits

- **Backgrounds**: all CC0 1.0. Surface photos from [Poly Haven](https://polyhaven.com) and
  [ambientCG](https://ambientcg.com); scene photos from Wikimedia Commons, found through
  [Openverse](https://openverse.org); panorama views from Poly Haven. Per-file details are in `backgrounds.json`.
- **Words**: from COCO-Text v2 (CC BY 4.0), Veit et al., *COCO-Text: Dataset and Benchmark for Text Detection
  and Recognition in Natural Images*, 2016.
- **Fonts**: the typefaces belong to their designers and foundries. The images show text rendered in them;
  the font files are not part of this set.
