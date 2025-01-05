import re


def solver(data):
    res = 0
    for val in data:
        val = val.split(",")
        res += int(val[0]) * int(val[1])
    return res


if __name__ == "__main__":
    with open("data/input_day03.txt") as f:
        mem = f.read()
    mul_regex = r"mul\((\d{1,3},\d{1,3})\)"
    print(solver(re.findall(mul_regex, mem)))  # part 1

    rgx_do = r"do\(\)"
    rgx_dont = r"don't\(\)"
    dos = [x.end() for x in re.finditer(rgx_do, mem)]
    donts = [x.end() for x in re.finditer(rgx_dont, mem)]
    all_idx = sorted(dos + donts)

    string = mem[:all_idx[0]]
    i = 0
    while True:
        idx = all_idx[i]
        if idx in donts:
            i += 1
            continue
        elif idx in dos:
            start = idx
            j = 1
            while True:
                if start + j >= len(mem) or i+j >= len(all_idx):
                    string += mem[start:]
                    i = len(all_idx)
                    break

                if all_idx[i+j] in donts:
                    string += mem[start:all_idx[i+j]]
                    i = i+j+1
                    break
                else:
                    j += 1

        if i >= len(all_idx):
            break

    print(solver(re.findall(mul_regex, string)))  # part 2
