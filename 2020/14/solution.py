from collections import defaultdict
from pathlib import Path
import re


class Memory:
    def __init__(self):
        self.mem = defaultdict(str)
        self.mask = None

    def __setitem__(self, idx, x):
        st = "0" * 36 + f"{x:b}"
        st = st[-36:]
        st = "".join(m if m != "X" else x for x, m in zip(st, self.mask))
        self.mem[idx] = st

    def sum(self):
        return sum(int(x, 2) for x in self.mem.values())


def test_part1():
    mem = Memory()
    mem.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    mem[8] = 11
    assert mem.sum() == 73
    mem[7] = 101
    assert mem.sum() == 73 + 101
    mem[8] = 0
    assert mem.sum() == 165


def run_on_input_data(mem):
    with Path("input.txt").open() as f:
        lines = f.read().splitlines()
    for line in lines:
        if line.startswith("mask = "):
            line = line.replace("mask = ", "")
            mem.mask = line
        else:
            idx, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups(0)
            mem[int(idx)] = int(val)



def part1():
    print("Part 1")
    mem = Memory()
    run_on_input_data(mem)
    print("Solution:", mem.sum())
    assert mem.sum() == 11179633149677


class MemoryAddressDecoder:
    def __init__(self):
        self.mem = defaultdict(str)
        self.mask = None

    def __setitem__(self, idx, val):
        st = "0" * 36 + f"{idx:b}"
        st = st[-36:]
        st = "".join(m if m != "0" else x for x, m in zip(st, self.mask))
        addresses = [st]
        while any("X" in x for x in addresses):
            new_addresses = []
            for address in addresses:
                for i, x in enumerate(address):
                    if x == "X":
                        new_addresses.append(address[:i] + "0" + address[i + 1 :])
                        new_addresses.append(address[:i] + "1" + address[i + 1 :])
                        break
            addresses = new_addresses
        for address in addresses:
            self.mem[address] = val

    def sum(self):
        return sum(self.mem.values())


def test_part2():
    mem = MemoryAddressDecoder()
    mem.mask = "000000000000000000000000000000X1001X"
    mem[42] = 100
    mem.mask = "00000000000000000000000000000000X0XX"
    mem[26] = 1
    assert mem.sum() == 208


def part2():
    print("Part 2")
    mem = MemoryAddressDecoder()
    run_on_input_data(mem)
    print("Solution:", mem.sum())
    assert mem.sum() == 4822600194774

test_part1()
part1()

test_part2()
part2()