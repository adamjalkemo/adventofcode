import numpy as np

puzzle_input = """######.#
#.###.#.
###.....
#.####..
##.#.###
.######.
###.####
######.#""".splitlines()


sample = """.#.
..#
###""".splitlines()


def simulate_grid(data, iterations):
    tensor = np.array([[[1 if c == "#" else 0 for c in row] for row in data]])
    tensor = grow_tensor(tensor)
    for _ in range(iterations):
        tensor = grow_tensor(tensor)
        new_tensor = np.zeros_like(tensor)
        for z, slice in enumerate(tensor[1:-1], 1):
            for y, row in enumerate(slice[1:-1], 1):
                for x, val in enumerate(row[1:-1], 1):
                    cube = tensor[z - 1 : z + 2, y - 1 : y + 2, x - 1 : x + 2]
                    number_of_active_neighbours = cube.sum() - val
                    active = val == 1
                    if active:
                        if 2 <= number_of_active_neighbours <= 3:
                            new_tensor[z, y, x] = 1
                    else:
                        if number_of_active_neighbours == 3:
                            new_tensor[z, y, x] = 1
        tensor = new_tensor
    return tensor


def grow_tensor(tensor):
    new_tensor = np.zeros(tensor.shape + np.array(2), dtype=int)
    new_tensor[1:-1, 1:-1, 1:-1] = tensor
    return new_tensor


def test_part1():
    tensor = simulate_grid(sample, 6)
    assert tensor.sum() == 112


def part1():
    tensor = simulate_grid(puzzle_input, 6)
    assert tensor.sum() == 448


def simulate_4d_grid(data, iterations):
    tensor = np.array([[[[1 if c == "#" else 0 for c in row] for row in data]]])
    tensor = grow_tensor_4d(tensor)
    for _ in range(iterations):
        tensor = grow_tensor_4d(tensor)
        new_tensor = np.zeros_like(tensor)
        for w, d_slice in enumerate(tensor[1:-1], 1):
            for z, slice in enumerate(d_slice[1:-1], 1):
                for y, row in enumerate(slice[1:-1], 1):
                    for x, val in enumerate(row[1:-1], 1):
                        hypercube = tensor[
                            w - 1 : w + 2, z - 1 : z + 2, y - 1 : y + 2, x - 1 : x + 2
                        ]
                        number_of_active_neighbours = hypercube.sum() - val
                        active = val == 1
                        if active:
                            if 2 <= number_of_active_neighbours <= 3:
                                new_tensor[w, z, y, x] = 1
                        else:
                            if number_of_active_neighbours == 3:
                                new_tensor[w, z, y, x] = 1
        tensor = new_tensor
    return tensor


def grow_tensor_4d(tensor):
    new_tensor = np.zeros(tensor.shape + np.array(2), dtype=int)
    new_tensor[1:-1, 1:-1, 1:-1, 1:-1] = tensor
    return new_tensor


def test_part2():
    tensor = simulate_4d_grid(sample, 6)
    assert tensor.sum() == 848


def part2():
    tensor = simulate_4d_grid(puzzle_input, 6)
    assert tensor.sum() == 2400


test_part1()
part1()
test_part2()
part2()
