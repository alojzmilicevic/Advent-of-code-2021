import time
from collections import defaultdict, Counter
from linereader import read_parts

d = read_parts('14.in.txt', '', split_instructions=['start', 'rules'])
rules = dict([(p[0], p[1]) for p in [y.replace(' -> ', ' ').split(' ') for y in d['rules']]])
start = d['start'][0]


def simulate_brute_force(polymer, number_of_sims=40):
    for k in range(0, number_of_sims):
        t0 = time.time()
        parts = []
        for i in range(1, len(polymer)):
            pair = "{first}{second}".format(first=polymer[i - 1], second=polymer[i])

            if i == len(polymer) - 1:
                parts.append(pair[:1] + rules[pair] + pair[1:])
            else:
                parts.append(pair[:1] + rules[pair])

        polymer = "".join(parts)
        print(time.time() - t0, "seconds", k)
    return polymer


pairs = Counter(start[i: i + 2] for i in range(len(start) - 1))
char_count = Counter(start)


def get_res():
    return max(char_count.values()) - min(char_count.values())


for i in range(40):
    if i == 10:
        print(get_res())

    new_pairs = defaultdict(int)
    for pair, cur_count in pairs.items():
        if pair in rules:
            c = rules[pair]
            new_pairs[pair[0] + c] += cur_count
            new_pairs[c + pair[1]] += cur_count
            char_count[c] += cur_count

    pairs = new_pairs

print(get_res())
