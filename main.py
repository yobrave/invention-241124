"""Invention pitch stagehand: cues the pitch, spotlights it, lowers it to output."""
STAMP = "onebug-11251142-inv3"
import json
import os
from pathlib import Path

STAGE = Path(__file__).resolve().parent
MIC_MAX = 220
PITCH = ("The UmbrellaHint is a small drone that follows you on sunny days "
         "whispering you will want me by three, "
         "fixing forgotten umbrellas through pure smugness.")


def cue():
    mic = STAGE / "entry.txt"
    line = mic.read_text(encoding="utf-8").strip()
    lit = bool(line) and len(line) <= MIC_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and lit:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(mic.read_bytes())
    print(json.dumps({"lit": lit, "stamp": STAMP, "mic_chars": len(line), "mic_max": MIC_MAX}))


if __name__ == "__main__":
    cue()
