import operator
import re

with open("input.txt") as f:
    puzzle_input = f.read().splitlines()


class NoPrecedence:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, NoPrecedence):
            return NoPrecedence(self.number + other.number)
        return NoPrecedence(self.number + other)

    def __sub__(self, other):
        if isinstance(other, NoPrecedence):
            return NoPrecedence(self.number * other.number)
        return NoPrecedence(self.number * other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)


def calculate_no_precedence(expr):
    p = re.compile(r"(\d+)")
    new_expr = p.sub(r"NoPrecedence(\1)", expr)
    new_expr = new_expr.replace("*", "-")
    return eval(new_expr).number


def test_part1():
    assert calculate_no_precedence("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632


def part1():
    assert sum(calculate_no_precedence(l) for l in puzzle_input) == 18213007238947


class AdditionHasPrecedence:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, AdditionHasPrecedence):
            return AdditionHasPrecedence(self.number * other.number)
        return AdditionHasPrecedence(self.number * other)

    def __mul__(self, other):
        if isinstance(other, AdditionHasPrecedence):
            return AdditionHasPrecedence(self.number + other.number)
        return AdditionHasPrecedence(self.number + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)


def calc_addition_has_precedence(expr):
    p = re.compile(r"(\d+)")
    new_expr = p.sub(r"AdditionHasPrecedence(\1)", expr)
    new_expr = new_expr.replace("+", "-")
    new_expr = new_expr.replace("*", "+")
    new_expr = new_expr.replace("-", "*")
    return eval(new_expr).number


def test_part2():
    assert calc_addition_has_precedence("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def part2():
    assert sum(calc_addition_has_precedence(l) for l in puzzle_input) == 388966573054664


test_part1()
part1()

test_part2()
part2()