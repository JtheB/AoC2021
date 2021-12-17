from inputs.input_17 import target_area


def part_one() -> int:
    # get distance from 0 to y_min
    step_size = abs(0 - target_area.y_min - 1)
    tmp_max_height = 0
    # calculate max point with gauss
    while step_size >= 0:
        tmp_max_height += step_size
        step_size -= 1

    return tmp_max_height


if __name__ == '__main__':
    print(f"Answer 1 for day 17 is {part_one()}")
