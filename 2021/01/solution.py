from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    d = [int(line) for line in f.readlines() if line != "\n"]

diff = np.diff(d)
print(np.sum(diff > 0))

v = np.convolve(d, np.ones((3)), mode="valid")
diff = np.diff(v)
print(np.sum(diff > 0))