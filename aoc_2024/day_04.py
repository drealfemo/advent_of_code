pos_to_check = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1)  # down-right
  ]
num_map = {"X": 1, "M": 2, "A": 3, "S": 4}
step_cum_sum_map = {1: 1, 2: 3, 3: 6, 4: 10}


def solver(rows):
    num_rows = len(rows)
    num_cols = len(rows[0])
    count = 0
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "X":
                for pos in pos_to_check:
                    step = 1
                    cum_sum = 1
                    try:
                        while True:
                            if step == 1:
                                x, y = i + pos[0], j + pos[1]
                            else:
                                x, y = x + pos[0], y + pos[1]
                            if x < 0 or y < 0 or x > num_rows-1 or y > num_cols-1:
                                break
                            step += 1
                            cum_sum += num_map[rows[x][y]]
                            if step_cum_sum_map[step] == cum_sum:
                                if step == 4\
                                        :
                                    count += 1
                                    break
                            else:
                                break
                    except IndexError:
                        pass
    return count


pos_to_check_two = [
    (1, 1),  # down-right
    (1, -1)  # down-left
]
num_map_two_fwd = {"M": 1, "A": 2, "S": 3}
num_map_two_bwd = {"S": 1, "A": 2, "M": 3}
step_cum_sum_map_two = {1: 1, 2: 3, 3: 6}


def solver_two(rows):
    num_rows = len(rows)
    num_cols = len(rows[0])
    count = 0
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char in ("M", "S"):
                for k, pos in enumerate(pos_to_check_two):
                    brk_loop = False
                    if k == 0:
                        a, b = i, j
                    else:
                        a, b = i, j+2
                    try:
                        char = rows[a][b]
                    except IndexError:
                        break
                    if char not in ("M", "S"):
                        break
                    num_map_two = num_map_two_fwd if char == "M" else num_map_two_bwd
                    step = 1
                    cum_sum = 1
                    try:
                        while True:
                            if step == 1:
                                x, y = a + pos[0], b + pos[1]
                            else:
                                x, y = x + pos[0], y + pos[1]

                            if x < 0 or y < 0 or x > num_rows-1 or y > num_cols-1:
                                break
                            step += 1

                            cum_sum += num_map_two[rows[x][y]]
                            if step_cum_sum_map_two[step] == cum_sum:
                                if step == 3:
                                    if k == 0:
                                        break
                                    else:
                                        count += 1
                                        break
                            else:
                                brk_loop = True
                                break
                    except (IndexError, KeyError):
                        break
                    if brk_loop:
                        break
    return count


if __name__ == "__main__":
    with open("data/input_day04.txt") as f:
        data = f.read().splitlines()
    print(solver(data))
    print(solver_two(data))
            