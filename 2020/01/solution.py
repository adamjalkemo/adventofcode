from itertools import combinations
from pathlib import Path

with Path("input.txt").open() as f:
    values = [int(x.strip()) for x in f.readlines()]

print("Part 1:")
for vals in combinations(values, 2):
    if sum(vals) == 2020:
        v1, v2 = vals
        print(f"Found the solution, v1 * v2 = {v1} * {v2} = {v1 * v2}")

print("Part 2:")
for vals in combinations(values, 3):
    if sum(vals) == 2020:
        v1, v2, v3 = vals
        print(f"Found the solution, v1 * v2 * v3 = {v1} * {v2} * {v3} = {v1 * v2 * v3}")
