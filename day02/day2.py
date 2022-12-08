def elf_to_type(e):
    if e == "A": return "R"
    elif e == "B": return "P"
    else: return "S"

def my_to_type(m):
    if m == "X": return "X"
    elif m == "Y": return "Y"
    else: return "Z"

with open("input_2_1.txt") as f:
    data = f.readlines()
    elf_strat = []
    my_strat = []

    for s in data:
        ss = s.replace("\n", "")
        ss = ss.split(" ")
        elf_strat.append(elf_to_type(ss[0]))
        my_strat.append(my_to_type(ss[1]))

print(elf_strat[:20])
print(my_strat[:20])

# A = rock, B = paper, C = scissor
# X = rock, Y = paper, Z = scissor

# rock -> 1, paper -> 2, scissor -> 3
# loss -> 0, draw  -> 3, win     -> 6

victory_dict = {
    "RR": 3, "PP": 3, "SS": 3,
    "RP": 6, "PS": 6, "SR": 6,
    "PR": 0, "SP": 0, "RS": 0
}

def get_type_score(t):
    if t == "R": return 1
    elif t == "P": return 2
    else: return 3

def get_win_score(e, m):
    return victory_dict[e + m]

type_score = 0
win_score = 0

# for i in range(len(my_strat)):
#     type_score += get_type_score(my_strat[i])
#     win_score += get_win_score(elf_strat[i], my_strat[i])

print(type_score)
print(win_score)
print(type_score + win_score)

# X = lose, Y = draw, Z = win

my_type_dict = {
    "RX": "S", "PX": "R", "SX": "P",
    "RY": "R", "PY": "P", "SY": "S",
    "RZ": "P", "PZ": "S", "SZ": "R"
}

def get_alt_win_score(m):
    if m == "X": return 0
    elif m == "Y": return 3
    else: return 6

def get_cond_type(e, m):
    return my_type_dict[e + m]

type_score = 0
win_score = 0

# elf_strat = ["R", "P", "S"]
# my_strat = ["Y", "X", "Z"]

for i in range(len(my_strat)):
    m = get_cond_type(elf_strat[i], my_strat[i])
    type_score += get_type_score(m)
    win_score += get_win_score(elf_strat[i], m)

print(type_score)
print(win_score)
print(type_score + win_score)



