from inputs.input_17 import target_area


def part_one() -> int:
    # get distance from 0 to y_min
    step_size = abs(0 - target_area.y_min - 1)
    tmp_max_height = 0
    # calculate max point from gravity
    while step_size >= 0:
        tmp_max_height += step_size
        step_size -= 1

    return tmp_max_height


def part_one_slim() -> int:
    return sum([step for step in range(abs(0 - target_area.y_min - 1), -1, -1) if step >= 0])


if __name__ == '__main__':
    print(f"Answer 1 for day 17 is {part_one()}")
    print(f"Answer 1 for day 17 is {part_one_slim()}")
