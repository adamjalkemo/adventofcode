from pathlib import Path

input = Path("input.txt").read_text().split("\n")

def sum_calibration_values(lines):
    filter_non_digits = lambda line: ''.join([c for c in line if c.isdigit()])
    input_digits_only = map(filter_non_digits, lines)

    first_and_last = [digits[0] + digits[-1] for digits in input_digits_only]
    first_and_last_int = map(int, first_and_last)

    return sum(first_and_last_int)

print("A: the sum is", sum_calibration_values(input))

digit_map = {
    # keep digit in text to allow chars to be a part of multiple
    # digit replacements.
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

def replace_digit_str(line):
    for k, v in digit_map.items():
        line = line.replace(k, v)
    return line
assert replace_digit_str("two1nine") == "two2two1nine9nine"
assert replace_digit_str("zoneight234") == "zone1oneight8eight234"

lines = map(replace_digit_str, input)
print("B: the sum is", sum_calibration_values(lines))
