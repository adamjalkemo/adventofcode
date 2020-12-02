from csv import DictReader
from pathlib import Path

print("Part 1:")
with Path("input.txt").open() as f:
    reader = DictReader(f, fieldnames=("interval", "letter", "password"), delimiter=" ")

    valid_passwords = 0
    for l in reader:
        min_count, max_count = [int(x) for x in l["interval"].split("-")]
        letter = l["letter"].strip(":")
        count = l["password"].count(letter)
        if min_count <= count <= max_count:
            valid_passwords += 1
    print(f"Solution: There are {valid_passwords} valid passwords")

print("Part 2:")
with Path("input.txt").open() as f:
    reader = DictReader(f, fieldnames=("indices", "letter", "password"), delimiter=" ")

    valid_passwords = 0
    for l in reader:
        letter = l["letter"].strip(":")
        password = l["password"]
        letter0, letter1 = [password[int(x) - 1] for x in l["indices"].split("-")]
        if (letter0 == letter) ^ (letter1 == letter):
            valid_passwords += 1
    print(f"Solution: There are {valid_passwords} valid passwords")
