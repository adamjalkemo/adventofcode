from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    d = [line.strip() for line in f.readlines() if line != "\n"]

g = [0] * len(d[0])
for n in d:
    for i, k in enumerate(n):
        g[i] += 1 if k == "1" else -1

gamma = int("".join(["1" if k > 0 else "0" for k in g]), 2)
eps = int("".join(["0" if k > 0 else "1" for k in g]), 2)
print(gamma * eps)

def rec(ds, idx, func):
    print(ds)
    c = 0
    for n in ds:
        c += 1 if n[idx] == "1" else -1

    #print(c)
    #if func(c):
    #    print(1)

    ds = [n for n in ds if (n[idx] == "1" and func(c)) or (n[idx] == "0" and not func(c))]
    #print(ds)
    if len(ds) == 1:
        return ds[0]
    return rec(ds, idx + 1, func)

ox = int(rec(d, 0, lambda x: x >= 0), 2)
co2 = int(rec(d, 0, lambda x: x < 0), 2)
print(ox * co2)