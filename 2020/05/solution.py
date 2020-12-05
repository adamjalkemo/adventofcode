from pathlib import Path

with Path("input.txt").open() as f:
    seats = f.read().splitlines()

def seat_coding_to_seat(seat):
    # Convert to binary
    seat = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    return int(seat, 2)

assert seat_coding_to_seat("BFFFBBFRRR") == 567
assert seat_coding_to_seat("FFFBBBFRRR") == 119
assert seat_coding_to_seat("BBFFBBFRLL") == 820

print("Part 1:")
max_seat_id = max(seat_coding_to_seat(seat) for seat in seats)
print(f"Solution: {max_seat_id} is the highest seat id")
assert max_seat_id == 996

# oneliner
assert max(int("".join("1" if x in "BR" else "0" for x in s), 2) for s in seats) == 996


print("Part 2:")
all_seats = set(range(2**10))
seats_in_list = set(seat_coding_to_seat(seat) for seat in seats)
empty_seats = all_seats - seats_in_list

# The first and last seats does not fulfil the -1 and +1 seat id conditions so they will be filtered
candidates = [seat for seat in empty_seats if (seat - 1 in seats_in_list) and (seat + 1 in seats_in_list)]
assert len(candidates) == 1
seat_id = candidates[0]

print(f"Solution: {seat_id} is the seat id")
assert seat_id == 671
