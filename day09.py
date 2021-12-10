import time

import numpy as np
from numpy import ndarray
from scipy import ndimage as ndi

startTime = time.time()


def read_input(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> ndarray:
    data_array = []
    [data_array.append(np.array([int(c) for c in line.rstrip("\n")], dtype=np.uint8)) for line in data.readlines()]
    return np.array(data_array)


def part_one(data) -> int:
    print(data)
    height_map = np.pad(data, pad_width=1, mode="constant", constant_values=9)
    rows, cols = height_map.shape
    result = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # check for neighbors <- -> v ^
            if height_map[row, col] < height_map[row - 1, col] and \
                    height_map[row, col] < height_map[row + 1, col] and \
                    height_map[row, col] < height_map[row, col - 1] and \
                    height_map[row, col] < height_map[row, col + 1]:
                result += height_map[row, col] + 1
    return result


def part_two(data) -> int:
    # height of 9 divides regions
    basins = np.where(data == 9, False, True)

    labels, num_of_labels = ndi.measurements.label(basins)
    areas = ndi.measurements.sum(basins, labels, index=np.arange(np.max(labels) + 1))

    # Sort and return only the biggest ones
    areas = np.sort(areas)
    return int(np.prod(areas[-3:]))


if __name__ == '__main__':
    # print(f"Answer 1 for day 9 is {part_one(parse_input(read_input('inputs/input_09_test.txt')))}")
    print(f"Answer 1 for day 9 is {part_one(parse_input(read_input('inputs/input_09.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    # print(f"Answer 2 for day 9 is {part_two(parse_input(read_input('inputs/input_09_test.txt')))}")
    print(f"Answer 2 for day 9 is {part_two(parse_input(read_input('inputs/input_09.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")
