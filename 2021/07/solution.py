from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    numbers = f.read()
#numbers = "16,1,2,0,4,2,7,1,2,14"
numbers = np.array([int(x) for x in numbers.split(",")])

rng = np.arange(np.min(numbers), np.max(numbers) + 1)
diff = np.abs(numbers[None, :] - rng[:, None])
cost = np.sum(diff, axis=1)
print("solution 1", np.min(cost))

lookup = np.cumsum(rng)
costs = lookup[diff]
cost = np.sum(costs, axis=1)
print("solution 2", np.min(cost))