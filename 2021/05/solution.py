from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

lines = [line.split(" -> ") for line in lines]
lines = [[x.split(",") for x in line] for line in lines]
lines = [[[int(k) for k in x] for x in line] for line in lines]

grid_size = 1000

ground = np.zeros((grid_size, grid_size))
for l0, l1 in lines:
    if l0[0] == l1[0] or l0[1] == l1[1]:
        mi = np.minimum(l0, l1)
        ma = np.maximum(l0, l1)
        assert (ma < grid_size).all()
        ground[mi[1]:ma[1] + 1, mi[0]:ma[0] + 1] += 1

print((ground >= 2).sum())


ground = np.zeros((grid_size, grid_size))
for l0, l1 in lines:
    mi = np.minimum(l0, l1)
    ma = np.maximum(l0, l1)
    assert (ma < grid_size).all()
    diff = ma - mi
    if (diff == 0).any():
        ground[mi[1]:ma[1] + 1, mi[0]:ma[0] + 1] += 1
    else:
        signs = np.sign(np.array(l1) - np.array(l0))
        assert diff[0] == diff[1]
        mask = np.eye(diff[0] + 1)
        if signs.prod() < 0:
            mask = mask[-1::-1]
        ground[mi[1]:ma[1] + 1, mi[0]:ma[0] + 1] += mask

print((ground >= 2).sum())