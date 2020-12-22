from collections import defaultdict
from functools import reduce
import operator

sample = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".splitlines()


sample2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".splitlines()


with open("input.txt") as f:
    input_data = f.read().splitlines()


def parse_ticket_data(data):
    rules = []
    for line in data:
        if line == "":
            break
        rules.append(line)

    parsed_lines = ""
    for line in data:
        if "your ticket:" not in parsed_lines:
            parsed_lines += line
            continue
        my_ticket = [int(x) for x in line.split(",")]
        break

    nearby_tickets = []
    parsed_lines = ""
    for line in data:
        if "nearby tickets:" not in parsed_lines:
            parsed_lines += line
            continue
        ticket = [int(x) for x in line.split(",")]
        nearby_tickets.append(ticket)

    rule_dict = defaultdict(list)
    for rule in rules:
        rule_name, rules_str = rule.split(": ")
        for rule_str in rules_str.split(" or "):
            rule_range = [int(x) for x in rule_str.split("-")]
            rule_dict[rule_name].append(rule_range)
        pass

    return my_ticket, nearby_tickets, rule_dict


def get_bad_values(data):
    _, nearby_tickets, rule_dict = parse_ticket_data(data)
    rule_ranges = [y for x in rule_dict.values() for y in x]
    bad_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            for rule_range in rule_ranges:
                if rule_range[0] <= value <= rule_range[1]:
                    break
            else:
                bad_values.append(value)
    return bad_values


def part1_test():
    bad_values = get_bad_values(sample)
    assert sum(bad_values) == 71


def part1():
    print("Part 1")
    bad_value_sum = sum(get_bad_values(input_data))
    print("Solution:", bad_value_sum)
    assert bad_value_sum == 20048


def get_ticket(data):
    my_ticket, nearby_tickets, rule_ranges = parse_ticket_data(data)
    valid_nearby_tickets = get_valid_tickets(nearby_tickets, rule_ranges)
    tickets = valid_nearby_tickets + [my_ticket]

    # get dict with compatible columns per category
    columns_by_category = get_compatible_ticket_column_per_category(
        rule_ranges, tickets
    )

    # sort by number of compatible columns
    columns_by_category = {
        k: v
        for k, v in sorted(columns_by_category.items(), key=lambda item: len(item[1]))
    }

    # perform exhaustive seach by starting at least common (first)
    column_by_category = solve(columns_by_category)

    ticket_value_by_category = {}
    for category, column in column_by_category.items():
        ticket_value_by_category[category] = my_ticket[column]

    return ticket_value_by_category


def get_valid_tickets(tickets, rule_dict):
    nearby_tickets = tickets
    rule_ranges = [y for x in rule_dict.values() for y in x]
    valid_tickets = []
    for ticket in nearby_tickets:
        ticket_valid = True
        for value in ticket:
            for rule_range in rule_ranges:
                if rule_range[0] <= value <= rule_range[1]:
                    break
            else:
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)

    return valid_tickets


def get_compatible_ticket_column_per_category(rule_ranges, tickets):
    columns_by_category = {}
    columns = list(zip(*tickets))
    for category, ranges in rule_ranges.items():
        columns_by_category[category] = set()
        for i, column in enumerate(columns):
            failed = False
            for value in column:
                for range in ranges:
                    if range[0] <= value <= range[1]:
                        break
                else:
                    failed = True
                    break

            if not failed:
                columns_by_category[category].add(i)
    return columns_by_category


def solve(columns_by_category):
    for category, columns in columns_by_category.items():
        for column in columns:
            new_columns_by_category = dict(columns_by_category)
            del new_columns_by_category[category]
            if not new_columns_by_category:
                return {category: column}

            # Remove column in other categories
            new_columns_by_category = {
                k: {x for x in v if x != column}
                for k, v in new_columns_by_category.items()
            }

            if [v for v in new_columns_by_category.values() if not v]:
                continue
            k = solve(new_columns_by_category)
            if k is not None:
                return {category: column, **k}
        return None
    raise NotImplementedError  # Not solvable


def part2_test():
    ticket = get_ticket(sample2)
    assert ticket["class"] == 12
    assert ticket["row"] == 11
    assert ticket["seat"] == 13


def part2():
    print("Part 2")
    ticket = get_ticket(input_data)
    product = reduce(
        operator.mul, (v for k, v in ticket.items() if k.startswith("departure")), 1
    )
    assert product == 4810284647569
    print("Solution:", product)


part1_test()
part1()

part2_test()
part2()