from pathlib import Path

input = Path("input.txt").read_text().strip().split("\n")

bags = [[]]
for item in input:
    if not item:
        bags.append([])
    else:
        bags[-1].append(int(item))

total_cals = [sum(bag) for bag in bags]

print("total cals:", max(total_cals))

print("total cals (top 3):", sum(sorted(total_cals)[-3:]))