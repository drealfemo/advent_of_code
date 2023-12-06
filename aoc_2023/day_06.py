def solver(rows, part=1):
    times = [int(x) for x in rows[0].rpartition("Time: ")[2].strip().split(" ") if x]
    distances = [int(x) for x in rows[1].rpartition("Distance: ")[2].strip().split(" ") if x]
    if part == 2:
        times = [int("".join([str(x) for x in times]))]
        distances = [int("".join([str(x) for x in distances]))]
    error_margins = []
    for tm, dst in zip(times, distances):
        e_m = 0
        for t in range(1, tm // 2 + 1):
            if t * (tm - t) > dst:
                e_m += 1
        if tm % 2 == 0:
            e_m = ((e_m - 1) * 2) + 1
        else:
            e_m = e_m * 2
        error_margins.append(e_m)

    res = 1
    for num in error_margins:
        res *= num
    return res


if __name__ == "__main__":
    with open("data/input_day06.txt") as f:
        lines = f.read().splitlines()

    print(solver(lines))
    print(solver(lines, part=2))
