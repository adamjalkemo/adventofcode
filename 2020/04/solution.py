from pathlib import Path

# Regexp is cheating

def create_passport(passport: str) -> dict:
    # Place all passport fields on the same line
    passport = passport.replace('\n', ' ')

    # Create lists from the fields
    fields = passport.split(" ")

    # Split key and value
    kv_fields = (field.split(":") for field in fields)
    return {k: v for k, v in kv_fields}

EXPECTED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
VALID_EYECOLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

with Path("input.txt").open() as f:
    passports = f.read().split("\n\n")

print("Part 1:")
passports_dicts = [create_passport(passport) for passport in passports]
number_of_valid_passports = 0
for passport in passports_dicts:
    if all(field in passport for field in EXPECTED_FIELDS):
        number_of_valid_passports += 1

print(f"Solution: {number_of_valid_passports} passports are valid")
assert number_of_valid_passports == 250

print("Part 2:")
validators = {
    "byr": lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: x.isdigit() and 2010 <= int(x) <= 2030,
    "hgt": lambda x: x[:-2].isdigit() and (
        (x.endswith("in") and 59 <= int(x[:-2]) <= 76) or (x.endswith("cm") and 150 <= int(x[:-2]) <= 193)
    ),
    "hcl": lambda x: x.startswith("#") and int(x[1:], 16),
    "ecl": lambda x: VALID_EYECOLORS.count(x) == 1,
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True
}

number_of_valid_passports = 0
for passport in passports_dicts:
    for field in EXPECTED_FIELDS:
        if field not in passport:
            break
        v = passport[field]
        if not validators[field](v):
            break
    else:
        number_of_valid_passports += 1

print(f"Solution: {number_of_valid_passports} passports are valid")
assert number_of_valid_passports == 158

