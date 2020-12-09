from itertools import combinations
from pathlib import Path

with Path("input.txt").open() as f:
    data = f.read().splitlines()

sample = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()

intify = lambda a: [int(x) for x in a]

print("Part 1:")

def get_failing_index(sequence, n):
    for idx, expected_sum in enumerate(sequence[n:], n):
        if not any(x + y == expected_sum for x, y in combinations(sequence[idx - n: idx], 2)):
            return expected_sum


assert get_failing_index(intify(sample), 5) == 127

number = get_failing_index(intify(data), 25)
print(f"Solution: The first number that does not have this property is {number}")
assert get_failing_index(intify(data), 25) == 31161678


print("Part 2:")

sample2 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()


def find_consecutive_sum_index(sequence, number, min_length = 2):
    for j in range(len(sequence)):
        for i in range(j, 0, -1):
            s = sequence[i: j]
            if len(s) < min_length:
                continue
            k = sum(s)
            if k == number:
                return min(s) + max(s)
            elif k > number:
                break
    raise Exception

assert find_consecutive_sum_index(intify(sample2), 127) == 62

min_max_sum = find_consecutive_sum_index(intify(data), number)
print(f"Solution: The sum of the min max is {min_max_sum}")
assert min_max_sum == 5453868
