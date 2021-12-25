import time


def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> (dict, int, int):
    data_array = data.read().splitlines()
    map_of_cucumbers = [[chars for chars in line] for line in data_array]
    max_x, max_y = len(map_of_cucumbers[0]), len(map_of_cucumbers)
    map_of_cucumbers_dict = {(x, y): char for y, row in enumerate(map_of_cucumbers) for x, char in enumerate(row)}
    return map_of_cucumbers_dict, max_x, max_y


def part_one(data) -> int:
    map_of_cucumbers, max_x, max_y = data
    current_step = 0
    moved_cucumbers = True
    while moved_cucumbers:
        current_step += 1

        east_moves = [(x, y) for (x, y) in map_of_cucumbers if
                      map_of_cucumbers[(x, y)] == '>' and map_of_cucumbers[((x + 1) % max_x, y)] == '.']

        for (x, y) in east_moves:
            map_of_cucumbers[(x, y)] = '.'
            map_of_cucumbers[(x + 1) % max_x, y] = '>'

        south_moves = [(x, y) for (x, y) in map_of_cucumbers if
                       map_of_cucumbers[(x, y)] == 'v' and map_of_cucumbers[(x, (y + 1) % max_y)] == '.']

        for (x, y) in south_moves:
            map_of_cucumbers[(x, y)] = '.'
            map_of_cucumbers[(x, (y + 1) % max_y)] = 'v'

        moves = len(east_moves) + len(south_moves)
        moved_cucumbers = moves > 0
        # print_map(map_of_cucumbers, max_x, max_y)
    return current_step


# just for debugging
def print_map(map_of_cucumbers, max_x, max_y):
    print('\n')
    for y in range(max_y):
        prt_str = ''
        for x in range(max_x):
            prt_str += map_of_cucumbers[(x, y)]
        print(prt_str)


if __name__ == '__main__':
    # print(f"Answer 1 for day 14 is {part_one(parse_input(read_input_for_testing('inputs/input_14_test.txt')), 10)}")
    input_data = parse_input(read_input_for_testing('inputs/input_25.txt'))
    startTime = time.time()
    print(f"Answer 1 for day 25 is {part_one(input_data)}")
    print(f"Execution time of {(time.time() - startTime) * 1000}ms")
