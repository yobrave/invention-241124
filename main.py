import json
import os
from contextlib import closing

PITCH_TAG = "inv3-demo-day"
SPAN = 220


def harvest(blob):
    """Yield non-blank rows one at a time."""
    for row in blob.replace("\r", "").split("\n"):
        if row.strip():
            yield row


def booth(line, root):
    hall = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(hall, exist_ok=True)
    sign = os.path.join(hall, "entry.txt")
    data = line.encode("utf-8")
    with closing(open(sign, "wb")) as board:
        board.write(data)
    with closing(open(sign, "rb")) as glance:
        seen = glance.read()
    if seen != data:
        raise RuntimeError("sign printed wrong")
    return sign


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as flyer:
    rows = list(harvest(flyer.read()))

line = rows[0] if rows else ""
if not line or len(line) > SPAN:
    print(json.dumps({"pitch": "passed", "size": len(line)}))
    raise SystemExit(1)

sign = booth(line, root)
print(json.dumps({"pitch": "funded", "size": len(line), "span": SPAN, "tag": PITCH_TAG, "sign": os.path.basename(sign)}))
