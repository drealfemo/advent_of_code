adjacent_positions = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1)  # down-right
  ]


def get_accessible_rolls(rolls_grid: list[str]) -> tuple[int, list[tuple[int, int]]]:
    num_rows = len(rolls_grid)
    num_cols = len(rolls_grid[0])
    accessible_rolls = 0
    to_remove = []
    for i in range(num_rows):
        for j in range(num_cols):
            val = rolls_grid[i][j]
            if val == ".":
                continue

            neighbours = 0
            for pos in adjacent_positions:
                ni, nj = i + pos[0], j + pos[1]
                if 0 <= ni < num_rows and 0 <= nj < num_cols and rolls_grid[ni][nj] == "@":
                    neighbours += 1
            if neighbours < 4:
                accessible_rolls += 1
                to_remove.append((i, j))
    return accessible_rolls, to_remove


def remove_paper_rolls(rolls_grid: list[str], to_remove: list[tuple[int, int]]) -> list[str]:
    for pos in to_remove:
        col = pos[1]
        val = rolls_grid[pos[0]]
        rolls_grid[pos[0]] = val[:col] + "." + val[col+1:]
    return rolls_grid


if __name__ == "__main__":
    with open("data/input_day04.txt") as f:
        data = f.read().splitlines()

    print(get_accessible_rolls(data)[0])  # part 1

    accessible_rolls_count = 1  # just to initialise
    removables_pos = []
    total_accessible_rolls_count = 0
    while accessible_rolls_count:
        data_fil = remove_paper_rolls(data, to_remove=removables_pos)
        accessible_rolls_count, removables_pos = get_accessible_rolls(data_fil)
        total_accessible_rolls_count += accessible_rolls_count
    print(total_accessible_rolls_count)  # part 2
