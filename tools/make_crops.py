"""Cut the text crops out of the full images, unscaled, using crop_box from labels.jsonl.
    python tools/make_crops.py v1         -> v1/crops/NNNNN.png
Needs Pillow (pip install pillow). Run from the repository root after unzipping the image parts into v1/."""
import json
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else 'v1')
os.makedirs(os.path.join(VER, 'crops'), exist_ok=True)
n = 0
for line in open(os.path.join(VER, 'labels.jsonl'), encoding='utf-8'):
    r = json.loads(line)
    dst = os.path.join(VER, 'crops', '%05d.png' % r['id'])
    if os.path.exists(dst):
        continue
    x0, y0, x1, y1 = r['crop_box']
    Image.open(os.path.join(VER, r['image'])).crop((x0, y0, x1, y1)).save(dst)
    n += 1
print('crops written:', n)
