from dataclasses import dataclass

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    directories: list
    files: list
    level: int

class FileHierarchy:
    directories: list
    files: list
    wd: str

    def __init__(self, wd, files=None, directories=None):
        self.files = files if files is not None else []
        self.directories = directories if directories is not None else []
        self.wd = wd

commands = [
"$ cd /",
"$ ls",
"dir a",
"14848514 b.txt",
"8504156 c.dat",
"dir d",
"$ cd a",
"$ ls",
"dir e",
"29116 f",
"2557 g",
"62596 h.lst",
"$ cd e",
"$ ls",
"584 i",
"$ cd ..",
"$ cd ..",
"$ cd d",
"$ ls",
"4060174 j",
"8033020 d.log",
"5626152 d.ext",
"7214296 k"
]

with open("input.txt", "r") as f:
    commands = f.readlines()
    commands = [cmd.replace("\n", "") for cmd in commands]

wd = ""
fh = {}
dirs = ["/"]

def cd(wd, d):
    if d == "..":
        tmp = wd.split("/")
        print(wd)
        return "/".join(tmp[:-2]) + "/"
    elif d == "/":
        wd = "/"
        print(wd)
        return wd
    else:
        wd += d + "/"
        print(wd)
        if wd not in dirs:
            dirs.append(wd)
        return wd

def create_file(name, size):
    fh[wd+name] = size

# inline this instead, ls is actually no-op
# def ls(cmds):
#     for cmd in cmds:
#         args = cmd.split(" ")
#         if args[0] == "dir":
#             pass
#         else:
#             sz = int(args[0])
#             nm = args[1]
#             create_file(nm, sz)

for _cmd in commands:
    # print(_cmd)
    cmd = _cmd.split(" ")

    if cmd[0] == "$":
        if cmd[1] == "cd":
            wd = cd(wd, cmd[2])
        elif cmd[1] == "ls":
            pass
        else:
            pass
    elif cmd[0] == "dir":
        pass
    else:
        sz = int(cmd[0])
        name = cmd[1]
        create_file(name, sz)

print(dirs[:10])
# print(fh)

dir_szs = {}

for dir in dirs:
    dir_szs[dir] = 0

for (abspath, sz) in fh.items():
    abspath_arr = abspath.split("/")
    dirs = [("/".join(abspath_arr[:-1-i]) + "/") for i in range(len(abspath_arr)-1)]
    for dir in dirs:
        dir_szs[dir] += sz

total = dir_szs["/"]
sz_under_threshold = 0
for (dir, sz) in dir_szs.items():
    # total += sz
    if sz <= 100_000:
        sz_under_threshold += sz

print(f"""
    Size of small directories:  {sz_under_threshold}
    Total used space:           {total}""")

sz_del_dir = total
free_space = 70_000_000 - total
target_sz = 30_000_000 - free_space
for (dir, sz) in dir_szs.items():
    if sz >= target_sz and sz < sz_del_dir:
        sz_del_dir = sz

print(f"""
    free space:                 {free_space}
    target dir sz:              {target_sz}
    smallest sufficient dir:    {sz_del_dir}
""")
# print(f"Size of smallest sufficient directory: {sz_del_dir}")


# cap = 70_000_000
# update = 30_000_000

