import numpy as np
from pathlib import Path
import sys
np.set_printoptions(threshold=sys.maxsize)


with Path("input.txt").open() as f:
    map = f.read()

# map = """
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

map = map.strip().split("\n")

map = np.array([[int(x) for x in r] for r in map])

def compute_cost(map):
    diff_cost = np.ones_like(map, dtype=float)
    prev_cost = np.zeros_like(diff_cost)
    while (diff_cost != 0).all():
        cost = np.full_like(map, np.nan, dtype=float)
        cost[-1, -1] = map[-1, -1]
        #print(map)
        #print(cost)
        for i in range(map.shape[0] - 1, -1, -1):
            for j in range(map.shape[1] - 1, -1, -1):
                if (np.array([i, j]) == map.shape).all():
                    continue
                #if np.isnan(cost[i, j]):
                #    break
                #print(map.shape, i, j)
                min_cost = np.inf
                for ii, jj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if (np.array([ii, jj]) >= map.shape).any() or (np.array([ii, jj]) < (0, 0)).any():
                        continue
                    if np.isnan(cost[ii, jj]):
                        continue
                    #cost[ii, jj] = map[ii, jj] + cost[i, j]
                    min_cost = min(min_cost, cost[ii, jj])
                if np.isinf(min_cost):
                    continue
                cost[i, j] = map[i, j] + min_cost
        diff_cost = prev_cost - cost
        prev_cost = cost
    #print(cost)
    #print(map)
    return min(cost[1, 0], cost[0, 1])
print("min_cost is", compute_cost(map))

new_map = np.zeros(np.array(map.shape) * 5)
for i in range(5):
    for j in range(5):
        ly, lx = map.shape
        new_map[ly*i:ly*i+ly, lx*j:lx*j+lx] = i + j

map = new_map + np.tile(map, (5, 5))
#map[map > 9] -= 9
map = ((map - 1) % 9) + 1
print(map[-20:, -20:])

print("min_cost is", compute_cost(map))