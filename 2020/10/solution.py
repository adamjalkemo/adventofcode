from collections import defaultdict
from functools import reduce
from pathlib import Path
from typing import List

sample0 = """16
10
15
5
1
11
7
19
6
12
4"""

sample1 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def intify(input_str: str) -> List[int]:
    data_str = input_str.splitlines()
    data = [int(d) for d in data_str]
    return data


def add_edge_values(data: List[int]) -> List[int]:
    data.insert(0, 0)
    data.append(data[-1] + 3)
    return data


def diff(data: List[int]) -> List[int]:
    return [d1 - d0 for d0, d1 in zip(data, data[1:])]


def multiply_ones_and_threes(data):
    return data.count(1) * data.count(3)


with Path("input.txt").open() as f:
    input_data = f.read()


transform = lambda input_data: reduce(
    lambda x, fn: fn(x),
    [intify, sorted, add_edge_values, diff, multiply_ones_and_threes],
    input_data,
)

print("Part 1:")
assert transform(sample0) == 7 * 5
assert transform(sample1) == 22 * 10
assert transform(input_data) == 1984
print(f"Solution: The product is {transform(input_data)}")


def get_valid_combinations(data):
    data.insert(0, 0)
    combinations_to_value = defaultdict(int)
    combinations_to_value[0] = 1
    for i, n0 in enumerate(data):
        for n1 in data[i + 1 :]:
            if n1 - n0 > 3:
                break
            combinations_to_value[n1] += combinations_to_value[n0]
    return combinations_to_value[n1]


transform = lambda input_data: reduce(
    lambda x, fn: fn(x),
    [intify, sorted, get_valid_combinations],
    input_data,
)

print("Part 2:")
assert transform(sample0) == 8
assert transform(sample1) == 19208
assert transform(input_data) == 3543369523456
print(f"Solution: The number of combinations is {transform(input_data)}")
