word_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solver(rows, part=1):
    if part == 2:
        rows_word_nums = {}
        for i in range(len(rows)):
            rows_word_nums[i] = []
            for w in word_to_int:
                pos1 = rows[i].find(w)
                pos2 = rows[i].rfind(w)
                if (pos1 == pos2) and pos1 != -1:
                    rows_word_nums[i].append((w, pos1))
                else:
                    if pos1 != -1:
                        rows_word_nums[i].append((w, pos1))
                    if pos2 != -1:
                        rows_word_nums[i].append((w, pos2))
        rows_word_nums = {k: sorted(v, key=lambda x: x[1]) for k, v in rows_word_nums.items()}

        for idx, word_nums in rows_word_nums.items():
            w = rows[idx]
            num = [(x, i) for i, x in enumerate(w) if x.isdigit()]
            all_nums = sorted(word_nums + num, key=lambda x: x[1])
            start = word_to_int.get(all_nums[0][0], all_nums[0][0])
            end = word_to_int.get(all_nums[-1][0], all_nums[-1][0])
            rows[idx] = start + end
    numbers_list = []
    for row in rows:
        numbers = [x for x in row if x.isdigit()]
        if len(numbers) > 1:
            numbers_list.append(int(numbers[0] + numbers[-1]))
        else:
            numbers_list.append(int(numbers[0] * 2))
    return numbers_list


if __name__ == "__main__":
    with open("data/input_day01.txt") as f:
        lines = f.read().splitlines()

    part1_result = sum(solver(lines))
    print(part1_result)
    part2_result = sum(solver(lines, part=2))
    print(part2_result)
