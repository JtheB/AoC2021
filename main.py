# AoC 2021

def read_input_01_01(filepath: str) -> list:
    file = open(filepath, "r")
    value_list = []
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        value_list.append(int(line))
    return value_list


def calc_and_count_increases_01_01(value_list: list) -> int:
    return len([(y - x) for x, y in zip(value_list[:-1], value_list[1:]) if y - x > 0])


# ( B + C + D) - (A + B + C) = D - A
def calc_and_count_increases_01_02(value_list: list) -> int:
    return len([(y - x) for x, y in zip(value_list[:-3], value_list[3:]) if y - x > 0])


if __name__ == '__main__':
    list_01_01 = read_input_01_01("inputs/01_input.txt")
    print(f"Answer for 01-01 is {calc_and_count_increases_01_01(list_01_01)}")
    print(f"Answer for 01-02 is {calc_and_count_increases_01_02(list_01_01)}")
