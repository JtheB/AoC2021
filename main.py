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
    prev_value = None
    counter = 0
    for value in value_list:
        if prev_value is None:
            prev_value = value
        else:
            if value - prev_value > 0:
                counter += 1
            prev_value = value
    return counter


# ( B + C + D) - (A + B + C) = D - A
def calc_and_count_increases_01_02(value_list: list) -> int:
    value_A = value_list[0]
    value_B = value_list[1]
    value_C = value_list[2]
    counter = 0
    for value in value_list[3:]:
        if value - value_A > 0:
            counter += 1
        value_A = value_B
        value_B = value_C
        value_C = value
    return counter


if __name__ == '__main__':
    list_01_01 = read_input_01_01("inputs/01_input.txt")
    print(f"Answer for 01-01 is {calc_and_count_increases_01_01(list_01_01)}")
    print(f"Answer for 01-02 is {calc_and_count_increases_01_02(list_01_01)}")

