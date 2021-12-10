import time

opener_chars = "([{<"
closer_chars = ")]}>"
error_scores_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
error_scores_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> list:
    data_array = [line for line in [x.strip() for x in data.readlines()]]
    return data_array


def part_one(data) -> int:
    score = 0
    for line in data:
        next_closing_char = []
        for char in line:
            # after opening char is found, add corresponding char to closing char
            if char in opener_chars:
                index = opener_chars.find(char)
                next_closing_char.append(closer_chars[index])
            # if closing char and the last one added to the next_closing_array, pop that one from the list
            elif char in closer_chars and char == next_closing_char[-1]:
                next_closing_char.pop(-1)
            else:
                score += error_scores_1.get(char)
                break
    return score


def part_two(data) -> int:
    scores = []
    for line in data:
        tmp_line_score = 0
        next_closing_char = []
        for char in line:
            # after opening char is found, add corresponding char to closing char
            if char in opener_chars:
                index = opener_chars.find(char)
                next_closing_char.append(closer_chars[index])
            # if closing char and the last one added to the next_closing_array, pop that one from the list
            elif char in closer_chars and char == next_closing_char[-1]:
                next_closing_char.pop(-1)
            else:
                break
        else:
            for closing_char in reversed(next_closing_char):
                tmp_line_score = tmp_line_score * 5 + error_scores_2.get(closing_char)
            scores.append(tmp_line_score)
    return sorted(scores)[int(len(scores) / 2)]


if __name__ == '__main__':
    # print(f"Answer 1 for day 9 is {part_one(parse_input(read_input_for_testing('inputs/input_10_test.txt')))}")
    startTime = time.time()
    print(f"Answer 1 for day 10 is {part_one(parse_input(read_input_for_testing('inputs/input_10.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")

    # print(f"Answer 2 for day 10 is {part_two(parse_input(read_input_for_testing('inputs/input_10_test.txt')))}")
    startTime = time.time()
    print(f"Answer 2 for day 10 is {part_two(parse_input(read_input_for_testing('inputs/input_10.txt')))}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")
