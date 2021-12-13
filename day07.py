import statistics
import time


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> list:
    data_array = [int(number) for number in data.read().split(",")]
    return data_array


def part_one(data) -> int:
    print(data)
    aim = round(statistics.median(data))
    fuel = [abs(position - aim) for position in data]
    return sum(fuel)


# def part_two(data) -> int:
#     return 0


if __name__ == '__main__':
    # print(f"Answer 1 for day 7 is {part_one(parse_input(read_input_for_testing('inputs/input_07_test.txt')))}")
    startTime = time.time()
    print(f"Answer 1 for day 7 is {part_one(parse_input(read_input_for_testing('inputs/input_07.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    # print(f"Answer 2 for day 7 is {part_two(parse_input(read_input_for_testing('inputs/input_07_test.txt')))}")
    # startTime = time.time()
    # print(f"Answer 2 for day 10 is {part_two(parse_input(read_input_for_testing('inputs/input_10.txt')))}")
    # print(f"Execution time of {(time.time() - startTime) * 1000}ms")
