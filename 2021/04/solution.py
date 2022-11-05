from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

numbers = [int(number) for number in lines[0].split(",")]
lines = lines[2:]

lines = [line.split(" ") for line in lines]
lines = [[int(l) for l in line if l != ""] for line in lines]

boards = []
boards_mask = []
for i in range(0, len(lines), 6):
    boards.append(np.array(lines[i:i+5]))
    boards_mask.append(np.zeros_like(lines[i:i+5]))
boards_mask = np.array(boards_mask)

for number in numbers:
    found = False
    for board, mask in zip(boards, boards_mask):
        mask |= (board == number)
        if np.isclose(mask.mean(axis=0), 1.0).any() or np.isclose(mask.mean(axis=1), 1.0).any():
            found = True
            break
    if found:
        break
else:
    print("no winner")

print(board)
print(mask)
print(board[mask == 0])
print(np.sum(board[mask == 0]) * number)
print(number)
for number in numbers:
    found = False
    for board, mask in zip(boards, boards_mask):
        mask |= (board == number)
        val = np.maximum(
            np.max(boards_mask.mean(axis=1), axis=1),
            np.max(boards_mask.mean(axis=2), axis=1))
        if np.isclose(np.mean(val), 1):
            found = True
            break
    if found:
        break
else:
    print("no winner")

print(board)
print(mask)
print(board[mask == 0])
print(np.sum(board[mask == 0]) * number)