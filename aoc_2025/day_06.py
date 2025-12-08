from itertools import zip_longest


def solver(data, cephalopod_math=False):
    if cephalopod_math:
        action_row = data[-1].strip().split()[::-1]
        new_data = []
        for val in zip_longest(*data, fillvalue=""):
            new_data.append("".join(val).replace("*", "").replace("+", ""))
        length = len(new_data)
        data = new_data
    else:
        data = [x.strip().split() for x in data]
        length = len(data[0])

    add = []
    mult = []
    col_data = []
    for col_idx in range(length):
        if cephalopod_math:
            if val := data[col_idx].strip():
                col_data.append(val)
                if col_idx < length - 1:
                    continue
            else:
                pass
            action = action_row.pop()
        else:
            col_data = [row[col_idx] for row in data]
            action = col_data[-1]

        if action == "+":
            temp_add = 0
            for val in col_data:
                try:
                    temp_add += int(val)
                except ValueError:
                    pass
            add.append(temp_add)
        else:
            temp_mult = 1
            for val in col_data:
                try:
                    temp_mult *= int(val)
                except ValueError:
                    pass
            mult.append(temp_mult)
        col_data = []
    return sum(add + mult)


if __name__ == "__main__":
    with open("data/input_day06.txt") as f:
        input_data = f.read().splitlines()

    print(solver(input_data))  # part 1
    print(solver(input_data, cephalopod_math=True))  # part 2
