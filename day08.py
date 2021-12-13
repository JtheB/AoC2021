import time

opener_chars = "([{<"
closer_chars = ")]}>"
error_scores_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
error_scores_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> list:
    data_array = [[set(i) for i in line.split() if i is not "|"] for line in data.read().split("\n")]
    return data_array


def part_one(data) -> int:
    global_sum = 0
    for signal in data:
        # digits 1, 4, 7, and 8 are always 2, 3, 4, or 7 chars long
        print(signal[-4:])
        global_sum += sum([len(digits) in (2, 3, 4, 7) for digits in signal[-4:]])
    return global_sum


def part_two(data) -> int:
    return 0


if __name__ == '__main__':
    # print(f"Answer 1 for day 8 is {part_one(parse_input(read_input_for_testing('inputs/input_08_test.txt')))}")
    startTime = time.time()
    print(f"Answer 1 for day 8 is {part_one(parse_input(read_input_for_testing('inputs/input_08.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    print(f"Answer 2 for day 8 is {part_two(parse_input(read_input_for_testing('inputs/input_08_test.txt')))}")
    # startTime = time.time()
    # print(f"Answer 2 for day 10 is {part_two(parse_input(read_input_for_testing('inputs/input_10.txt')))}")
    # print(f"Execution time of {(time.time() - startTime) * 1000}ms")
