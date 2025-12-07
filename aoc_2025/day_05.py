def merge_ranges(input_ranges):
    """find overlapping ranges and merge them"""
    sorted_ranges = sorted(input_ranges, key=lambda x: x[0])
    merged = []
    for interval in sorted_ranges:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)  # No overlap
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


if __name__ == "__main__":
    with open("data/input_day05.txt") as f:
        data = f.read().split("\n\n")

    ingredient_id_ranges = [list(map(int, x.split("-"))) for x in data[0].split("\n")]
    ingredient_ids = map(int, data[1].split("\n"))
    merged_id_ranges = merge_ranges(ingredient_id_ranges)
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for id_range in merged_id_ranges:
            if id_range[0] <= ingredient_id <= id_range[1]:
                fresh_count += 1
                break
    print(fresh_count)  # part 1
    print(sum(map(lambda x: x[1] - x[0] + 1, merged_id_ranges)))  # part 2
