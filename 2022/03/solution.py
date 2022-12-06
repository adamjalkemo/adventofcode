from pathlib import Path

input = Path("input.txt").read_text().strip().split("\n")

common_items = []
for rucksack in input:
    mid = len(rucksack) // 2
    union = set(rucksack[:mid]) & set(rucksack[mid:])
    assert len(union) == 1
    common_items.append(next(iter(union)))

priorities = []
for item in common_items:
    if item.isupper():
        priority = ord(item) - ord("A") + 27
    else:
        priority = ord(item) - ord("a") + 1
    priorities.append(priority)

print("pt1:", sum(priorities))


common_items = []
for rucksacks in zip(input[0::3], input[1::3], input[2::3]):
    union = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
    assert len(union) == 1
    common_items.append(next(iter(union)))

priorities = []
for item in common_items:
    if item.isupper():
        priority = ord(item) - ord("A") + 27
    else:
        priority = ord(item) - ord("a") + 1
    priorities.append(priority)

print("pt2:", sum(priorities))