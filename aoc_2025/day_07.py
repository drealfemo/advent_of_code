from functools import lru_cache


def count_splits_and_timelines(grid):
    splits = 0
    @lru_cache(maxsize=None)
    def dfs(current_position):
        nonlocal splits
        row, col = current_position
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return 1

        value = grid[row][col]
        if value in (".", "S"):
            return dfs((row + 1, col))
        elif value == "^":
            splits += 1
            return dfs((row, col - 1)) + dfs((row, col + 1))
        return 1

    return dfs((1, grid[0].index("S"))), splits


def count_splits(grid):
    start_col = data[0].index("S")
    stack = [(1, start_col)]

    visited = set()
    splits = 0
    while stack:
        row, col = stack.pop()
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            continue

        state = (row, col)
        if state in visited:
            continue
        visited.add(state)

        value = grid[row][col]
        if value == "." or value == "S":
            stack.append((row+1, col))
        elif value == "^":
            splits += 1
            stack.append((row, col-1))
            stack.append((row, col+1))

    return splits


if __name__ == "__main__":
    with open("data/input_day07.txt") as f:
        data = f.read().splitlines()

    print(count_splits(data))  # part 1 only
    print(*count_splits_and_timelines(data))  # part 1 and 2
