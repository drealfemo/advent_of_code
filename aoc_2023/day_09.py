def solver(rows, part=1):
    pos = -1 if part == 1 else 0
    res = 0
    for i, row in enumerate(rows):
        value = row[pos] if part == 1 else [row[pos]]
        while not all(x == 0 for x in row):
            row = [j - i for i, j in zip(row[:-1], row[1:])]
            if part == 1:
                value += row[pos]
            else:
                value.append(row[pos])
        if part == 1:
            res += value
        else:
            value = value[:-1]
            l = len(value)
            v = 0
            for _ in range(l):
                v = value.pop() - v
            res += v
    return res


if __name__ == "__main__":
    with open("data/input_day09.txt") as f:
        lines = [[int(y) for y in x.split(" ")] for x in f.read().splitlines()]

    print(solver(lines))
    print(solver(lines, part=2))
