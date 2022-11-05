from pathlib import Path
import numpy as np
from collections import Counter

inputs = []
outputs = []

with Path("input.txt").open() as f:
    for line in f:
        line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        input, output = line.split("|")
        inputs.append([inp.strip() for inp in input.split(" ") if inp != ""])
        outputs.append([out.strip() for out in output.split(" ") if out != ""])
        break

#print(outputs)
ct = Counter([len(out) for output in outputs for out in output])
print(ct)
print("Solution a:", ct[2] + ct[4] + ct[3] + ct[7])

rails = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"]
}

for k, v in rails.items():
    pass

total = 0
for input, output in zip(inputs, outputs):
    input = ["".join(sorted(x)) for x in input]
    output = ["".join(sorted(x)) for x in output]
    print(input)
    print(output)
    mappings = {c: [] for c in "abcdefg"}
    print(mappings)
    for inp in input:
        for c in inp:
            mappings[c].append(inp)
            print(c)
    print(mappings)
    exit()


#digits = set([y for x in inputs for y in x]) | set([y for x in outputs for y in x])
#print(digits)


#inp = ["".join(sorted(list(y))) for x in inputs for y in x]
#out = ["".join(sorted(list(y))) for x in outputs for y in x]
#print(set(inp) | set(out))

# for inp in inputs:
# for x in set(out):
#     print(x)
#     assert len(x) > 1

