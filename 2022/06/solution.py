from pathlib import Path

input = Path("input.txt").read_text().strip()

for i in range(4, len(input)):
    if len(set(input[i-4:i])) == 4:
        break
print("pt 1:", i)

for i in range(14, len(input)):
    if len(set(input[i-14:i])) == 14:
        break
print("pt 2:", i)