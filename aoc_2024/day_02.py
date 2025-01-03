def is_safe_level(level, dampener=False):
    prev_diff = None
    direction = None
    for i in range(1, len(level)):
        if i <= len(level)-1:
            diff = level[i] - level[i - 1]
            if not 1 <= abs(diff) <= 3:
                if dampener:
                    for n in range(len(level)):
                        lev = level.copy()
                        lev.pop(n)
                        if is_safe_level(lev):
                            return True
                    else:
                        return False
                else:
                    return False
            if not prev_diff:
                prev_diff = diff
                if diff > 0:
                    direction = 1
                elif diff < 0:
                    direction = -1
                else:
                    if dampener:
                        for n in range(len(level)):
                            lev = level.copy()
                            lev.pop(n)
                            if is_safe_level(lev):
                                return True
                        else:
                            return False
                    else:
                        return False
            else:
                if diff != 0 and ((diff > 0 and direction == 1) or (diff < 0 and direction == -1)):
                    prev_diff = diff
                else:
                    if dampener:
                        for n in range(len(level)):
                            lev = level.copy()
                            lev.pop(n)
                            if is_safe_level(lev):
                                return True
                        else:
                            return False
                    else:
                        return False
    return True


def solver(levels, dampener=False):
    num_safe = 0
    for level in levels:
        if is_safe_level(level, dampener):
            num_safe += 1
    return num_safe


if __name__ == "__main__":
    with open("data/input_day02.txt") as f:
        rows = [[int(y) for y in x.split(" ")] for x in f.read().splitlines()]
    print(solver(rows))  # part 1
    print(solver(rows, dampener=True))  # part 2
