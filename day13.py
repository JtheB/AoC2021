import time
import numpy as np


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def fold(coordinates, axis, value):
    if axis == 'y':
        return [(x, y) if value >= y else (x, 2 * value - y) for x, y in coordinates]
    elif axis == 'x':
        return [(x, y) if value >= x else (2 * value - x, y) for x, y in coordinates]
    else:
        return None


def fold_x(coordinates, x_axis):
    return [(x, y) if x_axis >= x else (2 * x_axis - x, y) for x, y in coordinates]


def parse_input(data) -> (list, list):
    line_list = [line.strip() for line in data.readlines()]
    coordinates = [line.split(',') for line in line_list if len(line) > 0 and line[0] is not 'f' and line is not '']
    coordinates = [(int(x), int(y)) for x, y in coordinates]
    folds = []
    for line in line_list:
        if len(line) > 0:
            if line[0] == 'f':
                if line[11] == 'x':
                    folds.append(('x', int(line[13:])))
                elif line[11] == 'y':
                    folds.append(('y', int(line[13:])))
    return coordinates, folds


def part_one(data) -> int:
    coordinates, folds = data
    axis, value = folds[0]
    coordinates = set(fold(coordinates, axis, value))
    return len(coordinates)


def part_two(data):
    coordinates, folds = data
    for axis, value in folds:
        coordinates = list(set(fold(coordinates, axis, value)))

    max_x = max(x for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    table = np.zeros(shape=(max_y + 1, max_x + 1), dtype="bool")
    for x, y in coordinates:
        table[y, x] = True
    output_string = ""
    for row in table:
        line = ""
        for dot in row:
            if dot:
                line += "X"
            else:
                line += " "
        output_string += line + "\n"
    print(output_string)


if __name__ == '__main__':
    # print(f"Answer 1 for day 13 is {part_one(parse_input(read_input_for_testing('inputs/input_13_test.txt')))}")
    startTime = time.time()
    print(f"Answer 1 for day 13 is {part_one(parse_input(read_input_for_testing('inputs/input_13.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    # print(f"Answer 2 for day 13 is {part_two(parse_input(read_input_for_testing('inputs/input_13_test.txt')))}")
    startTime = time.time()
    print(f"Answer 2 for day 13 is:")
    part_two(parse_input(read_input_for_testing('inputs/input_13.txt')))
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")
