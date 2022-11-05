from pathlib import Path
import numpy as np

with Path("input.txt").open() as f:
    numbers = f.read()
#numbers = "3,4,3,1,2"
numbers = np.array([int(x) for x in numbers.split(",")])

def sol1(numbers):
    born = 0
    for i in range(80):
        numbers = (numbers - 1)
        numbers[numbers < 0] = 6
        numbers = np.hstack((numbers, np.full(born, 8)))
        print(i+1, len(numbers), numbers)
        born = np.sum(numbers == 0)

def sol2(numbers):

    count = np.zeros(9, dtype=int)
    for number in numbers:
        count[number] += 1

    print(0, count)
    for i in range(256):
        #count[8] = count[0]
        born = count[0]
        count = np.roll(count, shift=-1)
        count[6] += count[8] # roll to 6 not 8
        count[8] = born
        print(i+1, count)

    print(np.sum(count))

sol1(numbers)
sol2(numbers)