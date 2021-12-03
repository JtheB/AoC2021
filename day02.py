def read_input_02(filepath: str) -> list:
    file = open(filepath, "r")
    value_list = []
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        direction, distance = line.split()
        value_list.append((direction, int(distance)))
    return value_list

def calc_and_count_increases_01(value_list: list) -> int:
    horizontal_pos = sum([y for x, y in value_list if x == "forward"])
    depth_positive = sum([y for x, y in value_list if x == "down"])
    depth_negative = sum([y for x, y in value_list if x == "up"])

    return horizontal_pos * (depth_positive - depth_negative)


def calc_and_count_increases_02(value_list: list) -> int:
    aim = 0
    depth = 0
    horizontal_pos = 0

    for command, value in value_list:
        if command == "down":
            aim += value
        elif command == "up":
            aim -= value
        elif command == "forward":
            horizontal_pos += value
            depth += aim * value

    return horizontal_pos * depth


if __name__ == '__main__':
    list_day_02 = read_input_02("inputs/input_02.txt")
    print(f"Answer 1 for day 2 is {calc_and_count_increases_01(list_day_02)}")
    print(f"Answer 2 for day 2 is {calc_and_count_increases_02(list_day_02)}")