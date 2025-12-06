# def max_joltage_per_bank(bank: str) -> int:
#     """
#     Given a string of digits (a battery bank),
#     return the maximum 2-digit number that can be formed
#     by selecting two digits *in order* (no rearranging).
#     """
#     best = 0
#     n = len(bank)
#
#     # try every pair (i < j)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             val = int(bank[i] + bank[j])
#             if val > best:
#                 best = val
#
#     return best


def max_joltage_digits(bank: str, k=2) -> int:
    """
    Given a string of digits (a battery bank),
    return the maximum k-digit number that can be formed
    by selecting K digits *in order* (no rearranging) provided.
    """
    drop = len(bank) - k  # number of digits that can be removed
    stack = []

    for digit in bank:
        while drop > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)

    result = ''.join(stack[:k])
    return int(result)


if __name__ == "__main__":
    with open("data/input_day03.txt") as f:
        batteries = f.read().splitlines()

    res1 = 0
    res2 = 0
    for battery_bank in batteries:
        res1 += max_joltage_digits(battery_bank)
        res2 += max_joltage_digits(battery_bank, k=12)

    print(res1)  # part 1
    print(res2)  # part 2
