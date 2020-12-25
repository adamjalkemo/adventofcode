sample = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''.splitlines()


sample1 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.splitlines()

with open("input.txt") as f:
    puzzle_input = f.read().splitlines()


def test_part1():
    rules = parse_rules(sample)
    messages = parse_messages(sample)
    number_of_valid_messages = len([message for message in messages if rules[0].verify_message(message)])
    assert number_of_valid_messages == 2


def part1():
    print("Part 1")
    rules = parse_rules(puzzle_input)
    messages = parse_messages(puzzle_input)
    number_of_valid_messages = len([message for message in messages if rules[0].verify_message(message)])
    assert number_of_valid_messages == 126
    print(f"Solution: {number_of_valid_messages}")


def test_part2():
    puzzle_data = sample1
    replacements = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
    messages = parse_messages(puzzle_data)
    rules = parse_rules(puzzle_data, replacements)
    number_of_valid_messages = len([message for message in messages if rules[0].verify_message(message)])
    assert number_of_valid_messages == 12


def part2():
    print("Part 2")
    puzzle_data = puzzle_input
    replacements = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
    messages = parse_messages(puzzle_data)
    rules = parse_rules(puzzle_data, replacements)
    number_of_valid_messages = len([message for message in messages if rules[0].verify_message(message)])
    assert number_of_valid_messages == 282
    print(f"Solution: {number_of_valid_messages}")


def parse_rules(*puzzle_datas):
    rules = {}
    for puzzle_data in puzzle_datas:
        for line in puzzle_data:
            if line == "":
                break
            key, value = line.split(":")
            rules[int(key)] = create_rule(rules, value)
    return rules


def parse_messages(puzzle_data):
    messages = None
    for message in puzzle_data:
        if message == "":
            messages = []
            continue
        if messages is not None:
            messages.append(message)

    return messages


def create_rule(rules, value):
    value = value.strip()
    if "|" in value:
        return OrRule(rules, value)
    elif " " in value:
        return SequenceRule(rules, value)
    elif "\"" in value:
        return CharRule(rules, value)
    else:
        return ReferenceRule(rules, value)


class OrRule:
    def __init__(self, rules, value):
        self.rules = [create_rule(rules, rule) for rule in value.split("|")]

    def is_message_valid(self, message):
        for rule in self.rules:
            for new_message, ret in rule.is_message_valid(message):
                if ret:
                    yield new_message, ret
        yield "", False


class SequenceRule:
    def __init__(self, rules, value):
        self.rules = [create_rule(rules, rule) for rule in value.split()]

    def verify_message(self, message):
        for new_message, ret in self.is_message_valid(message):
            if ret and len(new_message) == 0:
                return True
        return False

    def is_message_valid(self, message):
        yield from self.is_message_valid_i(message, 0)

    def is_message_valid_i(self, message, idx):
        rule = self.rules[idx]
        for new_message, ret in rule.is_message_valid(message):
            if ret:
                if idx + 1 == len(self.rules):
                    yield new_message, True
                else:
                    yield from self.is_message_valid_i(new_message, idx + 1)
        yield message, False


class CharRule:
    def __init__(self, rules, value):
        value = value.strip("\"")
        assert value in ["a", "b"]
        self.char = value

    def is_message_valid(self, message):
        if len(message) == 0:
            yield message, False
        else:
            yield message[1:], self.char == message[0]


class ReferenceRule:
    def __init__(self, rules, value):
        self.rules = rules
        self.ref = int(value)

    def is_message_valid(self, message):
        yield from self.rules[self.ref].is_message_valid(message)


test_part1()
part1()

test_part2()
part2()
