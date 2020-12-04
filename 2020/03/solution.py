from pathlib import Path
from functools import reduce
from operator import mul


with Path("input.txt").open() as f:
    map = f.read().splitlines()

def get_number_of_trees(map, right_steps, down_steps):
    pos = 0
    number_of_trees = 0 if map[0][0] == "." else 1
    for y, row in enumerate(map[1:], 1):
        if y % down_steps != 0:
            continue
        pos += right_steps
        pos = pos % len(row)
        if row[pos] == "#":
            number_of_trees += 1
    return number_of_trees

print("Part 1:")
number_of_trees = get_number_of_trees(map, 3, 1)
print(f"Solution: {number_of_trees} trees would be encountered")
assert number_of_trees == 284


print("Part 2:")
number_of_trees = (get_number_of_trees(map, right_steps, down_steps) for right_steps, down_steps in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
product_of_trees = reduce(mul, number_of_trees, 1)
print(f"Solution: {product_of_trees} is the product of trees encountered")
assert product_of_trees == 3510149120
