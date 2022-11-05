from pathlib import Path
import numpy as np

depth = 0
hor = 0
with Path("input.txt").open() as f:
    for line in f:
        if "down" in line:
            line = line.replace("down", "").strip()
            depth += int(line)
        elif "up" in line:
            line = line.replace("up", "").strip()
            depth -= int(line)
        elif "forward" in line:
            line = line.replace("forward", "").strip()
            hor += int(line)

print(depth * hor)

aim = 0
depth = 0
hor = 0
with Path("input.txt").open() as f:
    for line in f:
        if "down" in line:
            line = line.replace("down", "").strip()
            aim += int(line)
        elif "up" in line:
            line = line.replace("up", "").strip()
            aim -= int(line)
        elif "forward" in line:
            line = line.replace("forward", "").strip()
            hor += int(line)
            depth += aim * int(line)

print(depth * hor)