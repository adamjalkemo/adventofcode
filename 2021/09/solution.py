from pathlib import Path

import cv2
import numpy as np

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

sample_lines = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]

def lines_to_arr(lines):
    return np.array([[int(x) for x in line] for line in lines])

def get_min_neighbour_mask(arr):
    #print(arr)
    mask = np.zeros(arr.shape, dtype=np.bool)
    for i in range(arr.shape[0]):
        istart = max(0, i - 1)
        istop = i + 1 + 1
        for j in range(arr.shape[1]):
            jstart = max(0, j - 1)
            jstop = j + 1 + 1
            patch_mask = arr[istart : istop,  jstart : jstop] > arr[i, j]
            if np.sum(patch_mask == 0) == 1:
                mask[i, j] = True
    #print(mask)
    return mask

def get_basin_size(arr, x, y):
    mask = np.zeros(arr.shape, dtype=np.uint8)
    mask[y, x] = True
    mask_nines = arr == 9
    kernel = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ], dtype=np.uint8)
    prev_mask = np.zeros_like(mask)
    while not (prev_mask == mask).all():
        prev_mask = mask
        mask = cv2.dilate(mask, kernel)
        mask[mask_nines] = 0
    return np.sum(mask)


def part1():
    arr = lines_to_arr(sample_lines)
    mask = get_min_neighbour_mask(arr)
    risk_level = np.sum(arr[mask] + 1)
    assert risk_level == 15

    arr = lines_to_arr(lines)
    mask = get_min_neighbour_mask(arr)
    risk_level = np.sum(arr[mask] + 1)
    assert risk_level == 522

def part2():
    arr = lines_to_arr(sample_lines)
    mask = get_min_neighbour_mask(arr)
    coords = np.nonzero(mask)
    basin_sizes = np.array([get_basin_size(arr, x, y) for y, x in zip(*coords)])
    top_3_basin_sizes = -np.partition(-basin_sizes, 3)[:3]
    prod = np.prod(top_3_basin_sizes)
    assert prod == 1134

    arr = lines_to_arr(lines)
    mask = get_min_neighbour_mask(arr)
    coords = np.nonzero(mask)
    basin_sizes = np.array([get_basin_size(arr, x, y) for y, x in zip(*coords)])
    top_3_basin_sizes = -np.partition(-basin_sizes, 3)[:3]
    prod = np.prod(top_3_basin_sizes)
    assert prod == 916688

part1()

part2()