def rambunctious_fn(seq, idx):
    val = seq[-1]
    seq = seq[:-1]
    last_idx_per_val = {v: i for i, v in enumerate(seq)}

    for i in range(len(seq), idx-1):
        old_val = val
        if val in last_idx_per_val:
            val = i - last_idx_per_val[val]
        else:
            val = 0
        last_idx_per_val[old_val] = i
    return val


def test_part1():
    assert rambunctious_fn([1, 3, 2], 2020) == 1
    assert rambunctious_fn([2, 1, 3], 2020) == 10
    assert rambunctious_fn([1, 2, 3], 2020) == 27
    assert rambunctious_fn([2, 3, 1], 2020) == 78
    assert rambunctious_fn([3, 2, 1], 2020) == 438
    assert rambunctious_fn([3, 1, 2], 2020) == 1836


def part1():
    print("Part 1")
    assert rambunctious_fn([9, 6, 0, 10, 18, 2, 1], 2020) == 1238
    print("Solution:", rambunctious_fn([9, 6, 0, 10, 18, 2, 1], 2020))


def test_part2():
    assert rambunctious_fn([0, 3, 6], 30000000) == 175594
    assert rambunctious_fn([1, 3, 2], 30000000) == 2578
    assert rambunctious_fn([2, 1, 3], 30000000) == 3544142
    assert rambunctious_fn([1, 2, 3], 30000000) == 261214
    assert rambunctious_fn([2, 3, 1], 30000000) == 6895259
    assert rambunctious_fn([3, 2, 1], 30000000) == 18
    assert rambunctious_fn([3, 1, 2], 30000000) == 362


def part2():
    print("Part 2")
    assert rambunctious_fn([9, 6, 0, 10, 18, 2, 1], 30000000) == 3745954
    print("Solution:", rambunctious_fn([9, 6, 0, 10, 18, 2, 1], 30000000))


test_part1()
part1()

test_part2()
part2()