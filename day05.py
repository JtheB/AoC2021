from collections import Counter
from aocd import get_data


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file.read()


# only for tests
def parse_input(data) -> list:
    data = data.split("\n")
    coords_list = [[[coords for coords in lines.split(",")] for lines in datapoint.split(" -> ")] for datapoint in
                   data]
    return coords_list


def part_one(data):
    data = parse_input(data)
    lines = [(start, end) for start, end in data]
    points_from_straight_lines = calculate_points_from_straight_lines(lines)
    number_of_duplicates = len([item for item, count in Counter(points_from_straight_lines).items() if count > 1])

    return number_of_duplicates


def calculate_points_from_straight_lines(lines_list) -> list:
    points = []
    for line in lines_list:
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])
        if x1 == x2 or y1 == y2:
            points.extend(
                [(x, y) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)])
    return points


def calculate_points_from_lines(lines_list) -> list:
    points = []
    for line in lines_list:
        x1 = int(line[0][0])
        x2 = int(line[1][0])
        y1 = int(line[0][1])
        y2 = int(line[1][1])

        # straight lines
        if x1 == x2 or y1 == y2:
            points.extend(
                [(x, y) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)])
        # diagonals
        else:
            if x1 < x2:
                points.extend([(x, x - x1 + y1) for x in range(x1, x2 + 1)
                               if y1 < y2])
                points.extend([(x, y1 - (x - x1)) for x in range(x1, x2 + 1)
                               if y1 > y2])
            else:
                points.extend([(x, x - x2 + y2) for x in range(x2, x1 + 1)
                               if y2 < y1])
                points.extend([(x, y2 - (x - x2)) for x in range(x2, x1 + 1)
                               if y2 > y1])

    return points


def part_two(data):
    data = parse_input(data)
    lines = [(start, end) for start, end in data]
    points_from_lines = calculate_points_from_lines(lines)
    number_of_duplicates = len([item for item, count in Counter(points_from_lines).items() if count > 1])

    return number_of_duplicates


if __name__ == '__main__':
    # print(f"Answer 1 for day 5 is {part_one(read_input_for_testing('inputs/input_05_test.txt'))}")
    print(f"Answer 1 for day 5 is {part_one(get_data(day=5, year=2021))}")
    # print(f"Answer 2 for day 5 is {part_two(read_input_for_testing('inputs/input_05_test.txt'))}")
    print(f"Answer 2 for day 5 is {part_two(get_data(day=5, year=2021))}")
