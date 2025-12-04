def solver(levels, dampener=False):
    num_safe = 0
    for level in levels:
        if is_safe_level(level, dampener):
            num_safe += 1
    return num_safe


if __name__ == "__main__":
    with open("data/input_day01.txt") as f:
        lines = f.read().splitlines()
