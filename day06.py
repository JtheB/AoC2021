import time

from aocd import get_data

startTime = time.time()


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file.read()


def parse_input(data) -> list:
    data = [int(n.strip()) for n in data.split(",")]
    return data


def parse_input_by_count(data) -> list:
    data = [[int(number.strip()) for number in data.split(",")].count(i) for i in range(9)]
    return data


# First slow solution
def part_one(data, days) -> int:
    for day in range(days):
        new_data = []
        for fish in data:
            if fish == 0:
                new_data.append(6)
                new_data.append(8)
            else:
                new_data.append(fish - 1)
        data = new_data

    return len(data)


# fishshifting
def part_two(fishis, days) -> int:
    for d in range(days):
        # shift 0 fishis to last spot (8)
        fishis.append(fishis.pop(0))
        # Add number of new 8s
        fishis[6] += fishis[-1]
    return sum(fishis)


if __name__ == '__main__':
    # print(f"Answer 1 for day 6 is {part_one(parse_input(read_input_for_testing('inputs/input_06_test.txt')), 80)}")
    print(f"'shitty' Answer 1 for day 6 is {part_one(parse_input(get_data(day=6, year=2021)), 80)}")
    print(f"Execution time of 'shitty' algorithm {time.time() - startTime}s")

    print(f"'better' Answer 1 for day 6 is {part_two(parse_input_by_count(get_data(day=6, year=2021)), 80)}")
    print(f"Execution time of 'better' algorithm {time.time() - startTime}s")

    # print(f"Answer 2 for day 5 is {part_two(read_input_for_testing('inputs/input_05_test.txt'))}")
    print(f"Answer 2 for day 6 is {part_two(parse_input_by_count(get_data(day=6, year=2021)), 256)}")
    print(f"Execution time of 'shitty' algorithm {time.time() - startTime}s")
