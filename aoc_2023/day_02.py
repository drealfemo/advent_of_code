def solver(part=1):
    colours = {"red": 12, "green": 13, "blue": 14}
    output = 0
    for game in lines:
        impossible_game = False
        data = game.rpartition(":")
        game_num, res = int(data[0].split(" ")[1]), data[2].split(";")
        max_red, max_green, max_blue = 0, 0, 0
        for st in res:
            cubes = [x.strip().split(" ") for x in st.split(",")]
            for cube in cubes:
                c = int(cube[0])
                if part == 1:
                    if c > colours[cube[1]]:
                        impossible_game = True
                        break
                else:
                    if cube[1] == "red":
                        max_red = max(max_red, c)
                    elif cube[1] == "green":
                        max_green = max(max_green, c)
                    else:
                        max_blue = max(max_blue, c)
            if impossible_game:
                break
        else:
            if part == 1:
                output += game_num
            else:
                game_output = max_red * max_green * max_blue
                output += game_output
    return output


if __name__ == "__main__":
    with open("data/input_day02.txt") as f:
        lines = f.read().splitlines()

    print(solver())
    print(solver(part=2))
