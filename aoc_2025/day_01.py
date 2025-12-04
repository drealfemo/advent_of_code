def count_zero_hits(rotations):
    pos = 50
    count = 0
    for line in rotations:
        dir_char = line[0]
        num = int(line[1:])
        if dir_char == 'L':
            pos = (pos - num) % 100
        else:  # 'R'
            pos = (pos + num) % 100

        if pos == 0:
            count += 1
    return count


def count_all_zeros(rotations):
    pos = 50
    zeros = 0
    for line in rotations:
        dir_ = line[0]
        dist = int(line[1:])
        for _ in range(dist):
            if dir_ == 'L':
                pos = (pos - 1) % 100
            else:  # 'R'
                pos = (pos + 1) % 100

            if pos == 0:
                zeros += 1
    return zeros


if __name__ == "__main__":
    with open("data/input_day01.txt") as f:
        lines = f.read().splitlines()
    zero_hits = count_zero_hits(lines)
    print(zero_hits)  # part 1
    all_zeros = count_all_zeros(lines)
    print(all_zeros)  # part 2
