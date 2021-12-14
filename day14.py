import math
import time
from collections import defaultdict


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


# initiated new tuples need a 0 value...
def default_val():
    return 0


def parse_input(data) -> (str, list):
    line_list = [line.strip() for line in data.readlines()]
    start_sequence = line_list.pop(0)
    reaction_dict = {}
    for line in line_list:
        if len(line) > 0:
            reaction_dict[line[:2]] = line[-1]
    return start_sequence, reaction_dict


def part_one(data, steps) -> int:
    start_sequence, reaction_dict = data

    # almost forgot this one and got lucky... thanks @rswilli for the universal fix idea
    last_char = start_sequence[-1]

    pair_count = defaultdict(default_val)
    for char_pos in range(len(start_sequence) - 1):
        current_pair = start_sequence[char_pos:char_pos + 2]
        if not current_pair in pair_count:
            pair_count[current_pair] = 1
        else:
            pair_count[current_pair] += 1

    for step in range(steps):
        tmp_pair_count = defaultdict(default_val)

        for pair in pair_count:
            if pair in reaction_dict:
                created_pairs = (pair[0] + reaction_dict[pair], reaction_dict[pair] + pair[1])
                for new_pair in created_pairs:
                    tmp_pair_count[new_pair] += pair_count[pair]
            else:
                tmp_pair_count[pair] += pair_count[pair]
        pair_count = tmp_pair_count

    char_amount = defaultdict(default_val)

    for pair in pair_count:
        char_amount[pair[0]] += pair_count[pair]

    char_amount[last_char] += 1

    max_count = 0
    min_count = math.inf
    for char in char_amount:
        min_count = min(char_amount[char], min_count)
        max_count = max(char_amount[char], max_count)

    return int(max_count - min_count)


if __name__ == '__main__':
    # print(f"Answer 1 for day 14 is {part_one(parse_input(read_input_for_testing('inputs/input_14_test.txt')), 10)}")
    startTime = time.time()
    print(f"Answer 1 for day 14 is {part_one(parse_input(read_input_for_testing('inputs/input_14.txt')), 10)}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    # print(f"Answer 2 for day 14 is {part_one(parse_input(read_input_for_testing('inputs/input_14_test.txt')), 40)}")
    startTime = time.time()
    print(f"Answer 2 for day 13 is {part_one(parse_input(read_input_for_testing('inputs/input_14.txt')), 40)}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")
