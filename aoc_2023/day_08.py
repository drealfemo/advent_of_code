class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return "Node({!r})".format(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def add_children(self, nodes):
        self.children.extend(nodes)


if __name__ == "__main__":
    with open("data/input_day08.txt") as f:
        lines = f.read().splitlines()
    pattern = lines[0]
    len_p = len(pattern)
    data = [d.split(" = ") for d in lines[2:]]
    nds_map = {Node(x[0]): [Node(y) for y in x[1].replace("(", "").replace(")", "").split(", ")] for x in data}
    nds = list(nds_map.keys())

    # part 1
    start_node = None
    for n, ch in nds_map.items():
        idx = nds.index(n)
        ch1_idx, ch2_idx = nds.index(ch[0]), nds.index(ch[1])
        nds[idx].add_children([nds[ch1_idx], nds[ch2_idx]])
        if n.value == "AAA":
            start_node = n

    steps = 0
    st = 0
    nd = start_node
    while nd.value != "ZZZ":
        if pattern[st] == "R":
            nd = nd.children[1]
        else:
            nd = nd.children[0]
        st += 1
        steps += 1
        if st == len_p:
            st = 0
    print(steps)
