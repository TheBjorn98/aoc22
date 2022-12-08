with open("input_5.txt", "r") as f:
    data = f.readlines()
    instructions = data[10:]
    # data = data.split("\n\n")
    # stacks = data[0].split("\n")
    # instructions = data[1].split("\n")

# data = """
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

# stacks = {
#     1: ["Z", "N"],
#     2: ["M", "C", "D"],
#     3: ["P"]
# }
# data = data.split("\n\n")
# instructions = data[1].split("\n")

stacks = {
    1: ["M", "J", "C", "B", "F", "R", "L", "H"],
    2: ["Z", "C", "D"],
    3: ["H", "J", "F", "C", "N", "G", "W"],
    4: ["P", "J", "D", "M", "T", "S", "B"],
    5: ["N", "C", "D", "R", "J"],
    6: ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    7: ["P", "Z", "T", "F", "R", "H"],
    8: ["L", "V", "M", "G"],
    9: ["C", "B", "G", "P", "F", "Q", "R", "J"],
}

# print(stacks)
# print(instructions)

# 0    1 2    3      4  5
# move x from source to dest

def parse_instruction(instr):
    arr = instr.split(" ")
    x = int(arr[1])
    source = int(arr[3])
    dest = int(arr[5])
    return (x, source, dest)

def execute_instruction(x, source, dest):
    tmp = []
    for i in range(x):
        e = stacks[source].pop()
        tmp.append(e)
    for i in range(x):
        e = tmp.pop()
        stacks[dest].append(e)

print(stacks)

for instr in instructions:
    x, s, d = parse_instruction(instr)
    execute_instruction(x, s, d)
print("")
# print(stacks)

for (k, v) in stacks.items():
    print(f"{k}: {v}")

