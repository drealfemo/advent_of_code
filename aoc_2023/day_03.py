def solver(part=1):
    symbols = {}
    gears = {}
    width = len(lines[0]) - 1
    num_rows = len(lines) - 1
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if not val.isdigit() and val != ".":
                key = (i, j)
                symbols[key] = []
                is_gear = True if val == "*" else False

                left = j - 1
                if left >= 0:
                    if lines[i][left].isdigit():
                        symbols[key].append((i, left))

                right = j + 1
                if right <= width:
                    if lines[i][right].isdigit():
                        symbols[key].append((i, right))

                up = i - 1
                if up >= 0:
                    if lines[up][j].isdigit():
                        symbols[key].append((up, j))

                down = i + 1
                if down <= num_rows:
                    if lines[down][j].isdigit():
                        symbols[key].append((down, j))

                if up >= 0 and left >= 0:
                    if lines[up][left].isdigit():
                        symbols[key].append((up, left))

                if up >= 0 and right <= width:
                    if lines[up][right].isdigit():
                        symbols[key].append((up, right))

                if down <= num_rows and left >= 0:
                    if lines[down][left].isdigit():
                        symbols[key].append((down, left))

                if down <= num_rows and right <= width:
                    if lines[down][right].isdigit():
                        symbols[key].append((down, right))

                if is_gear:
                    gears[key] = symbols[key]

    if part == 1:
        all_pos = [y for x in symbols.values() for y in x if y]
        res = 0
        for i, line in enumerate(lines):
            num = ""
            num_pos = []
            for j, val in enumerate(line):
                if val.isdigit():
                    num += val
                    num_pos.append((i, j))
                if num and (not val.isdigit() or j == width):
                    if any(x for x in num_pos if x in all_pos):
                        res += int(num)
                    num = ""
                    num_pos = []
    else:
        gears_num = {k: [] for k in gears}
        for i, line in enumerate(lines):
            num = ""
            num_pos = []
            for j, val in enumerate(line):
                if val.isdigit():
                    num += val
                    num_pos.append((i, j))
                if num and (not val.isdigit() or j == width):
                    for g, poss in gears.items():
                        if any(x for x in num_pos if x in poss):
                            gears_num[g].append(int(num))
                    num = ""
                    num_pos = []
        res = sum(v[0] * v[1] for v in gears_num.values() if len(v) == 2)
    return res


if __name__ == "__main__":
    with open("data/input_day03.txt") as f:
        lines = f.read().splitlines()

    print(solver())
    print(solver(part=2))
