import numpy as np


def read_input_03(filepath: str) -> list:
    file = open(filepath, "r")
    value_list = []
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        value_list.append(line)
    return value_list


# solution with loops
def calc_eps_and_gamma_product_03_01(value_list: list) -> int:
    # transpose binary list
    transposed_list = map(list, zip(*value_list))
    eps = gamma = ""
    for code in transposed_list:
        code = "".join(code)
        zeroes = code.count("0")
        ones = code.count("1")
        if zeroes > ones:
            gamma += "0"
            eps += "1"
        else:
            gamma += "1"
            eps += "0"
    return int(eps, 2) * int(gamma, 2)


def calc_oxygen_and_co2_product_03_02(value_list: list) -> int:
    data = np.array([[int(b) for b in c] for c in value_list])
    oxygen = co2 = data

    length_of_code = data.shape[1]

    for i in range(length_of_code):
        if oxygen.shape[0] != 1:
            mask = oxygen[:, i] == 1
            ones = oxygen[mask]
            zeroes = oxygen[~mask]
            if ones.shape[0] >= zeroes.shape[0]:
                oxygen = ones
            else:
                oxygen = zeroes

        if co2.shape[0] != 1:
            mask = co2[:, i] == 1
            ones = co2[mask]
            zeroes = co2[~mask]
            if zeroes.shape[0] <= ones.shape[0]:
                co2 = zeroes
            else:
                co2 = ones

    # convert to number
    oxygen_num = int("".join([str(b) for b in oxygen.flatten()]), 2)
    co2_num = int("".join([str(b) for b in co2.flatten()]), 2)

    return oxygen_num * co2_num


if __name__ == '__main__':
    list_03 = read_input_03("inputs/input_03.txt")
    print(f"Answer 1 for day 3 is {calc_eps_and_gamma_product_03_01(list_03)}")
    print(f"Answer 2 for day 3 is {calc_oxygen_and_co2_product_03_02(list_03)}")
