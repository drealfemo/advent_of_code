from collections import Counter
from itertools import chain

CARD_RANKS = dict(zip([str(n) for n in range(2, 10)] + list('TJQKA'), range(13)))
CARD_RANKS_2 = dict(zip(["J"] + [str(n) for n in range(2, 10)] + list('TQKA'), range(13)))


class Card:
    def __init__(self, char, part=1):
        self.char = char
        if part == 1:
            self.rank = CARD_RANKS[char]
        else:
            self.rank = CARD_RANKS_2[char]


class Hand:
    def __init__(self, hand_str, part=1):
        self.hand_str = hand_str
        self.hand = [Card(c, part=part) for c in hand_str]
        self.hand_num = [x.rank for x in self.hand]

        count = Counter(self.hand_str)
        max_count = max(count.values())
        if part == 2:
            if "J" in self.hand_str and count["J"] != 5:
                max_val_occur = max({k: v for k, v in count.items() if k != "J"}.items(), key=lambda x: x[1])[0]
                count = Counter(self.hand_str.replace("J", max_val_occur))
                max_count = max(Counter(count).values())

        if max_count == 5:
            self.rank = 7
        elif max_count == 4:
            self.rank = 6
        elif max_count == 3 and 2 in count.values():
            self.rank = 5
        elif max_count == 3:
            self.rank = 4
        elif Counter(count.values())[2] == 2:
            self.rank = 3
        elif Counter(count.values())[2] == 1:
            self.rank = 2
        else:
            self.rank = 1

    def __iter__(self):
        return iter(self.hand)

    def __repr__(self):
        return f"Hand('{self.hand_str}')"


if __name__ == "__main__":
    with open("data/input_day07.txt") as f:
        lines = f.read().splitlines()

    rows = [x.split(" ") for x in lines]
    hs_ = {Hand(k): v for k, v in rows}
    hs = sorted(hs_, key=lambda k: k.rank)
    hs_r = {k: k.rank for k in hs}
    r_hs = {}
    for r in hs_r.values():
        r_hs[r] = sorted([k for k in hs_r.keys() if hs_r[k] == r], key=lambda c: [n for n in c.hand_num])
    n = 1
    res = 0
    for h in chain(*r_hs.values()):
        res += n * int(hs_[h])
        n += 1
    print(res)

    hs2_ = {Hand(k, part=2): v for k, v in rows}
    hs2 = sorted(hs2_, key=lambda k: k.rank)
    hs2_r = {k: k.rank for k in hs2}
    r_hs2 = {}
    for r in hs2_r.values():
        r_hs2[r] = sorted([k for k in hs2_r.keys() if hs2_r[k] == r], key=lambda c: [n for n in c.hand_num])
    n2 = 1
    res2 = 0
    for h2 in chain(*r_hs2.values()):
        res2 += n2 * int(hs2_[h2])
        n2 += 1
    print(res2)
