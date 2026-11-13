import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.b64")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
with open(SRC, "r", encoding="ascii") as f:
    data = base64.b64decode("".join(f.read().split()))
with open(DST, "wb") as f:
    f.write(data)
