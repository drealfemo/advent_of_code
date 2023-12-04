def solver(rows):
    c = {x[0].split("Card")[1].strip(): x[2].split(" | ") for x in rows}
    cards = {
        k: ([x for x in v[0].split(" ") if x], [y for y in v[1].split(" ") if y]) for k, v in c.items()
    }
    cards_matches = {k: set(v[0]).intersection(v[1]) for k, v in cards.items()}

    pts = 0
    for _, match in cards_matches.items():
        if match:
            if (num_match := len(match)) > 1:
                pts += 2 ** (num_match - 1)
            else:
                pts += 1

    cards_occurrence = {int(k): 1 for k in cards_matches}
    for card, match in cards_matches.items():
        card = int(card)
        if match:
            mult = cards_occurrence[card]
            for i in range(start := card + 1, start + len(match)):
                if i <= list(cards_occurrence.keys())[-1]:
                    cards_occurrence[i] += 1 * mult
    n_cards = sum(cards_occurrence.values())

    return pts, n_cards


if __name__ == "__main__":
    with open("data/input_day04.txt") as f:
        lines = [x.rpartition(":") for x in f.read().splitlines()]

    points, num_cards = solver(lines)
    print(f"part 1: {points}")
    print(f"part 2: {num_cards}")
