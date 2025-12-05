def is_repeated_twice(num_str: str) -> bool:
    """
    Returns True if the integer n consists of some sequence of digits repeated twice.
    Example: 55, 6464, 123123.
    """
    if len(num_str) % 2 == 0:
        midpoint = len(num_str) // 2
        return num_str[:midpoint] == num_str[midpoint:]
    return False


def is_repeated_pattern(num_str: str) -> bool:
    """
    Returns True if n is composed of some digit-sequence repeated
    at least twice. Examples:
    11, 22, 123123, 1212121212, 1111111, etc.
    """
    str_length = len(num_str)

    # Try all possible unit lengths
    for str_pos in range(1, str_length):
        if str_length % str_pos == 0 and str_length // str_pos >= 2:
            str_slice = num_str[:str_pos]
            if str_slice * (str_length // str_pos) == num_str:
                return True

    return False


if __name__ == "__main__":
    with open("data/input_day02.txt") as f:
        id_ranges = [x.split("-") for x in f.read().split(",")]

    res1 = 0
    res2 = 0
    for id_range in id_ranges:
        for num in range(int(id_range[0]), int(id_range[1]) + 1):
            str_num = str(num)
            len_num_str = len(str_num)
            if is_repeated_twice(str_num):
                res1 += num
            if is_repeated_pattern(str_num):
                res2 += num

    print(res1)  # part 1
    print(res2)  # part 2
