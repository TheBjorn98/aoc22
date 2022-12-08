with open("input_3_1.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda d: d.replace("\n", ""), data))

# data = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

lengths = list(map(lambda d: len(d) // 2, data))
first = []
second = []

for i in range(len(lengths)):
    f = data[i][:lengths[i]]
    s = data[i][lengths[i]:]
    first.append(f)
    second.append(s)

def char_to_prio(c):
    o = ord(c)
    if o > 96:
        return o - 96
    else:
        return o - 64 + 26

f_set = [set(f) for f in first]
s_set = [set(s) for s in second]
i_set = [f.intersection(s) for (f, s) in zip(f_set, s_set)]

i_vals = [[char_to_prio(c) for c in s] for s in i_set]


total = sum([sum(iv) for iv in i_vals])
print(total)

groups = []
i_grp = []

for i in range(0, len(data), 3):
    sets = [set(data[i+j]) for j in range(3)]
    i_sets = sets[0].intersection(sets[1]).intersection(sets[2])
    groups.append(sets)
    i_grp.append(i_sets)

i_grp_vals = [[char_to_prio(c) for c in s] for s in i_grp]
total = sum([sum(iv) for iv in i_grp_vals])
print(total)

