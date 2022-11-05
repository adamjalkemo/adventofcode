from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

lines = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]
lines = [np.array([int(x) for x in line]) for line in lines]

risk_sum = 0
for line in lines:
    print(line)
    d = np.diff(line)
    mask = np.ones_like(line, dtype=bool)
    #print(mask)
    #print(d < 0)
    #print(d > 0)
    mask[1:] &= d < 0
    mask[:-1] &= d > 0
    risk_sum += np.sum(line[mask]) + np.sum(mask)
    print(risk_sum)
    print(mask)
    #exit()
print(risk_sum)