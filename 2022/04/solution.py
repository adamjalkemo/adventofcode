from pathlib import Path

input = Path("input.txt").read_text().strip().split("\n")

pairs = [x.split(",") for x in input]
pairs = [[[int(z) for z in y.split("-")] for y in x] for x in pairs]


overlaps = 0
overlaps_pt2 = 0
for range0, range1 in pairs:
    range0 = list(range(range0[0], range0[1] + 1))
    range1 = list(range(range1[0], range1[1] + 1))

    if len(set(range0) & set(range1)) >= min(len(range0), len(range1)):
        overlaps += 1

    if len(set(range0) & set(range1)):
        overlaps_pt2 += 1

print("pt 1:", overlaps)
print("pt 2:", overlaps_pt2)