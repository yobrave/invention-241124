"""Absurd invention pitch: inspect the sentence, then convey it to the gate output."""
import json
import os
import pathlib

PITCH_FILE = "entry.txt"
CEILING = 220


def inspect_entry(blob: str) -> dict:
    words = blob.split()
    sentences = [seg for seg in blob.replace("!", ".").replace("?", ".").split(".") if seg.strip()]
    dossier = {
        "word_tally": len(words),
        "sentence_tally": len(sentences),
        "glyphs": len(" ".join(words)),
        "raw_bytes": len(blob.encode("utf-8")),
        "under_ceiling": len(" ".join(words)) <= CEILING,
        "one_sentence": len(sentences) <= 1,
    }
    dossier["board_ready"] = dossier["under_ceiling"] and dossier["one_sentence"] and dossier["glyphs"] > 0
    return dossier


def convey() -> int:
    home = pathlib.Path(__file__).resolve().parent
    blob = (home / PITCH_FILE).read_text(encoding="utf-8")
    dossier = inspect_entry(blob)
    quay = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", home / "quay"))
    quay.mkdir(parents=True, exist_ok=True)
    (quay / PITCH_FILE).write_bytes(blob.encode("utf-8"))
    print(json.dumps({"pitch": "fridge-dimmer", "dossier": dossier, "quay": str(quay)}))
    return 0 if dossier["board_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(convey())
