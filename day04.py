import numpy as np
from aocd import get_data


# Not used first attempt of parsing data
def parse_input(data) -> (list, list):
    drawn_numbers = bingo_boards = []
    tmp_5by5_array = []
    for value in data:
        if not drawn_numbers:
            drawn_numbers = value.split(",")
        elif not value == "":
            print(f"{len(tmp_5by5_array)}: {value}")
            if len(tmp_5by5_array) < 5:
                tmp_numbers = value.split(" ")
                tmp_5by5_array.append(tmp_numbers)
            else:
                print(tmp_5by5_array)
                bingo_boards.append(tmp_5by5_array)
                tmp_5by5_array = []
                tmp_numbers = value.split(" ")
                tmp_5by5_array.append(tmp_numbers)
    bingo_boards.append(np.array(tmp_5by5_array))
    return drawn_numbers, bingo_boards


def parse_input_better(data) -> (list, list):
    data = data.split("\n\n")
    numbers = [int(n) for n in data[0].split(',')]
    bingo_boards = [np.array([[int(n) for n in l.split()] for l in board.splitlines()]) for board in data[1:]]
    return numbers, bingo_boards


def check_board_for_win(masked_board):
    rows = np.sum(masked_board, axis=1)
    cols = np.sum(masked_board, axis=0)
    if 5 in rows or 5 in cols:
        return True
    else:
        return False


def part_one(data):
    numbers, bingo_boards = parse_input_better(data)

    masked_boards = [np.zeros_like(b) for b in bingo_boards]
    for n in numbers:
        for board, masked_board in zip(bingo_boards, masked_boards):
            masked_board |= (board == n)
            if check_board_for_win(masked_board):
                return np.sum(board[(masked_board == 0)]) * n


def part_two(data):
    numbers, bingo_boards = parse_input_better(data)

    masked_boards = [np.zeros_like(b) for b in bingo_boards]
    board_won_already_list = [False] * len(bingo_boards)
    for n in numbers:
        for i, (board, masked_board) in enumerate(zip(bingo_boards, masked_boards)):
            if not board_won_already_list[i]:
                masked_board |= (board == n)
                board_won_already_list[i] = check_board_for_win(masked_board)
                if all(board_won_already_list):
                    return np.sum(board[(masked_board == 0)]) * n


if __name__ == '__main__':
    print(f"Answer 1 for day 4 is {part_one(get_data(day=4, year=2021))}")
    print(f"Answer 2 for day 4 is {part_two(get_data(day=4, year=2021))}")
