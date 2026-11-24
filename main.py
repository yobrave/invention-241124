"""Invention pitch: one sentence, filed with the office of ideas."""
import os
import sys

PITCH = ("The Fridge Dimmer: a sensor that fades the midnight fridge "
         "glow down to bar-at-closing-time, so 2 AM snack runs feel "
         "discreet instead of indicted.")
FILE_NO = "inv2"
OFFICE = "patents-adjacent"
FEE = "waived"


def file_it(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    data = PITCH + "\n"
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
    if open(p, "rb").read() != data.encode("utf-8"):
        sys.exit("filed under wrong universe")
    return open(p, encoding="utf-8").read().strip()


got = file_it(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print(FILE_NO, OFFICE, len(got), "chars on file")
print("fee:", FEE, "stamped at 2 AM")
