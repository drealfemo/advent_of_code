from functools import reduce


def solver(junction_boxes, single_circuit=False):
    junction_box_dists = {}
    for x in junction_boxes:
        for y in junction_boxes:
            if (
                x != y
                and (x, y) not in junction_box_dists
                and (y, x) not in junction_box_dists
            ):
                junction_box_dists[x, y] = (
                    ((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2) + ((x[2] - y[2]) ** 2)
                ) ** 0.5
    sorted_pairs = sorted(junction_box_dists.items(), key=lambda x: x[1])

    result = None
    circuits = []
    visited = []
    num_pairs = len(sorted_pairs) if single_circuit else 1000
    i = 0
    while (
        not (
            len(circuits) == 1
            and (len(circuits[0]) == len(visited) == len(junction_boxes))
        )
        if single_circuit
        else num_pairs > 0
    ):
        (j1, j2), _ = sorted_pairs[i]
        seen_j1, seen_j2 = j1 in visited, j2 in visited
        if not seen_j1 and not seen_j2:
            circuits.append({j1, j2})
            visited.extend((j1, j2))
        elif seen_j1 and not seen_j2:
            idx_j1 = next(circuits.index(x) for x in circuits if j1 in x)
            circuits[idx_j1].add(j2)
            visited.append(j2)
        elif not seen_j1 and seen_j2:
            idx_j2 = next(circuits.index(x) for x in circuits if j2 in x)
            circuits[idx_j2].add(j1)
            visited.append(j1)
        elif seen_j1 and seen_j2:
            idx_j1 = next(circuits.index(x) for x in circuits if j1 in x)
            idx_j2 = next(circuits.index(x) for x in circuits if j2 in x)
            if idx_j1 != idx_j2:
                merged_circuit = circuits[idx_j1].union(circuits[idx_j2])
                circuits = [
                    circuits[i]
                    for i in range(len(circuits))
                    if i not in (idx_j1, idx_j2)
                ]
                circuits.append(merged_circuit)

        if (
            single_circuit
            and len(circuits) == 1
            and (len(circuits[0]) == len(visited) == len(junction_boxes))
        ):
            result = j1[0] * j2[0]

        i += 1
        num_pairs -= 1

    if not single_circuit:
        circuit_lengths = sorted({len(x) for x in circuits}, reverse=True)
        result = reduce(lambda x, y: x * y, circuit_lengths[:3])

    return result


if __name__ == "__main__":
    with open("data/input_day08.txt") as f:
        data = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]

    print(solver(data))  # part 1
    print(solver(data, single_circuit=True))  # part 2
