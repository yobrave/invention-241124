"""inv6: gadget pitch review board. Board members inspect, chair signs."""
import json
import os
import sys
from pathlib import Path

HOOP = 220


class Pitch:
    def __init__(self, raw: str):
        self.raw = raw
        self.line = raw.strip()
        self.n = len(self.line)

    def member_checks(self):
        return {
            "not_blank": bool(self.line) and not self.line.isspace(),
            "within_hoop": self.n <= HOOP,
        }


class Chair:
    def __init__(self, pitch: Pitch):
        self.pitch = pitch
        self.signed = all(pitch.member_checks().values())

    def hand_over(self):
        if self.signed:
            stand = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
            stand.mkdir(parents=True, exist_ok=True)
            (stand / "entry.txt").write_bytes(self.pitch.line.encode("utf-8"))
        return {"board": "inv6-pitch-r6", "signed": self.signed, "n": self.pitch.n, "hoop": HOOP}


def main():
    pitch = Pitch(Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8"))
    print("VERDICT", json.dumps(Chair(pitch).hand_over()))
    return 0 if Chair(pitch).signed else 1


if __name__ == "__main__":
    sys.exit(main())
