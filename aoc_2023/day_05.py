def get_map_value(rows, row_num, key):
    n = row_num + 1
    ln = rows[n]
    while ln:
        data = [int(x) for x in ln.split(" ")]
        source, destination, width = data[1], data[0], data[2]
        if source > key or key > (source + width):
            if n + 1 == len(rows):
                map_value = key
                break
            ln = rows[n + 1]
            n = n + 1
            continue
        else:
            diff = key - source
            map_value = destination + diff
            break
    else:
        map_value = key
    return map_value


def solver(rows):
    tag_lines = []
    for j, line in enumerate(rows):
        if line and line[0].isalpha() and j > 0:
            tag_lines.append((j, line))

    seeds = [int(x) for x in rows[0].rpartition("seeds: ")[2].split(" ")]

    seeds_map = {k: [] for k in seeds}
    for seed in seeds:
        for i, line in tag_lines:
            if "seed-to-soil" in line:
                seeds_map[seed].append(get_map_value(rows, i, seed))
                continue

            if "soil-to-fertilizer" in line:
                k = seeds_map[seed][0]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue

            if "fertilizer-to-water" in line:
                k = seeds_map[seed][1]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue

            if "water-to-light" in line:
                k = seeds_map[seed][2]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue

            if "light-to-temperature" in line:
                k = seeds_map[seed][3]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue

            if "temperature-to-humidity" in line:
                k = seeds_map[seed][4]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue

            if "humidity-to-location map" in line:
                k = seeds_map[seed][5]
                seeds_map[seed].append(get_map_value(rows, i, k))
                continue
    res = min(v[-1] for v in seeds_map.values())

    return res


if __name__ == "__main__":
    with open("data/input_day05.txt") as f:
        lines = f.read().splitlines()

    print(solver(lines))
