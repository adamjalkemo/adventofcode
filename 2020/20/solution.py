import re
import numpy as np

sample = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...""".splitlines()

# sample1 = """Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14""".splitlines()


with open("input.txt") as f:
    tiles_input = f.read().splitlines()

def parse_tiles(tile_str):
    tiles = []
    tile = None
    images = []
    for line in [*tile_str, "Tile 1000:"]:
        if "Tile" in line:
            if tile:
                assert(images)
                tiles.append((tile, images))
                tile = None
                images = []
            tile = re.match("Tile (\d+):", line).group(1)
        elif line == "":
            pass
        else:
            images.append(line)
    #print(tiles)
    #print(images)

    new_tiles = []
    for id, tile in tiles:
        tile = np.array([[1 if t == "#" else 0 for t in ti] for ti in tile], dtype=np.bool)
        sides = [tile[0, :], tile[:, -1], tile[-1, :], tile[:, 0]]
        new_tiles.append({
            "id": int(id),
            "sides": sides
        })
    tiles = new_tiles

    lookup = {}
    for tile in tiles:
        for side in tile["sides"]:
            side_tmp = side.tobytes()
            for side in [side_tmp]:#, side_tmp[-1::-1]]:
                if side not in lookup:
                    lookup[side] = []
                lookup[side].append(tile)
    return tiles, lookup

def get_product(tile_str):
    tiles, lookup = parse_tiles(tile_str)
    # history = []
    # history.append({
    #     "used_tiles": [tiles[0]],
    #     "placement": [[0, 0]]
    # })
    #while history[-1]["used_tiles"] != 2:
    #    for tile in 

    prod = 1
    for tile in tiles:
        #print(tile["id"])
        cnt = 0
        for side in tile["sides"]:
            side = side.tobytes()
            #print(len(lookup[side]))
            if (len(lookup[side]) + len(lookup.get(side[-1::-1], []))) == 1:
                cnt += 1
                #print("+1")
            #else:
                #print("0")
        #print(cnt, tile["id"])
        if cnt == 2:
            prod *= tile["id"]

    return prod


def count_sea_monsters(tile_str):
    tiles, lookup = parse_tiles(tile_str)

    for tile in tiles:
        for side in tile["sides"]:
            side = side.tobytes()
            #print(len(lookup[side]))
            print(len(lookup[side]) + len(lookup.get(side[-1::-1], [])))
            #if (len(lookup[side]) + len(lookup.get(side[-1::-1], []))) == 1:
                



def test_part1():
    assert get_product(sample) == 20899048083289


def part1():
    print("Part 1")
    assert get_product(tiles_input) == 4006801655873
    print(f"Solution: {get_product(tiles_input)}")


def test_part2():
     #assert count_sea_monsters(sample) == 291
     print(f"Solution {count_sea_monsters(sample)} sea monsters")


# def part2():
#     print("Part 2")
#     assert run_recursive_game(puzzle_input) == 35836
#     print(f"Solution: {run_recursive_game(puzzle_input)}")


#test_part1()
#part1()

test_part2()
# part2()
