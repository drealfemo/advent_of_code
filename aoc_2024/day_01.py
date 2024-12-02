from collections import Counter


def solver(rows: list[str]) -> tuple[int, int]:
    loc_ids_1 = sorted([int(x.split(" ")[0]) for x in rows])
    loc_ids_2 = sorted([int(x.split(" ")[-1]) for x in rows])
    p1 = sum(abs(a - b) for a, b in zip(loc_ids_1, loc_ids_2))

    ids_2_count = Counter(loc_ids_2)
    p2 = 0
    for idx in loc_ids_1:
        p2 += idx * ids_2_count.get(idx, 0)

    return p1, p2


if __name__ == "__main__":
    with open("data/input_day01.txt") as f:
        lines = f.read().splitlines()
    part_1, part_2 = solver(lines)
    print(part_1, part_2)

