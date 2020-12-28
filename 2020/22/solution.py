sample = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".splitlines()

sample1 = """Player 1:
43
19

Player 2:
2
29
14""".splitlines()


with open("input.txt") as f:
    puzzle_input = f.read().splitlines()


def run_game(puzzle_input):
    decks = create_decks(puzzle_input)
    assert len(decks) == 2

    while 0 not in (len(deck) for deck in decks):
        cards = [deck.pop(0) for deck in decks]
        argmax = max(range(len(cards)), key=lambda x: cards[x])
        winning_deck = decks[argmax]
        winning_deck.extend(sorted(cards, reverse=True))
    num_cards = len(winning_deck)

    return sum(m * x for m, x in zip(range(1,num_cards + 1), winning_deck[-1:-num_cards - 1:-1]))


def run_recursive_game(puzzle_input):
    decks = create_decks(puzzle_input)
    assert len(decks) == 2

    winner_idx = subgame(decks)
    winning_deck = decks[winner_idx]
    num_cards = len(winning_deck)

    return sum(m * x for m, x in zip(range(1,num_cards + 1), winning_deck[-1:-num_cards - 1:-1]))

def subgame(decks):
    historic_decks = set()
    while 0 not in (len(deck) for deck in decks):
        decks_tuple = (tuple(decks[0]), tuple(decks[1]))
        if decks_tuple in historic_decks:
            return 0 # Prevent infinite game
        historic_decks.add(decks_tuple)

        cards = [deck.pop(0) for deck in decks]
        if any(card > len(deck) for deck, card in zip(decks, cards)):
            winner_idx = max(range(len(cards)), key=lambda x: cards[x])
        else:
            new_deck = [deck[:card] for deck, card in zip(decks, cards)]
            winner_idx = subgame(new_deck)
        winning_deck = decks[winner_idx]
        winning_deck.append(cards[winner_idx])
        winning_deck.append(cards[1 if winner_idx == 0 else 0])
    return winner_idx


def create_decks(puzzle_input):
    decks = []
    deck = None
    for line in puzzle_input:
        if "Player" in line:
            if deck is not None:
                decks.append(deck)
            deck = []
        else:
            if line == "":
                continue
            deck.append(int(line))
    if deck is not None:
        decks.append(deck)
    return decks


def test_part1():
    assert run_game(sample) == 306


def part1():
    print("Part 1")
    assert run_game(puzzle_input) == 32598
    print(f"Solution: {run_game(puzzle_input)}")


def test_part2():
    assert run_recursive_game(sample) == 291
    assert run_recursive_game(sample1) == 105


def part2():
    print("Part 2")
    assert run_recursive_game(puzzle_input) == 35836
    print(f"Solution: {run_recursive_game(puzzle_input)}")


test_part1()
part1()

test_part2()
part2()
