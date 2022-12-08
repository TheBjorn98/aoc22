with open("input_4.txt", "r") as f:
    data = f.readlines()

# data = [
#     "2-4,6-8",
#     "2-3,4-5",
#     "5-7,7-9",
#     "2-8,3-7",
#     "6-6,4-6",
#     "2-6,4-8"
# ]

f = []
s = []

for i in range(len(data)):
    tmp = data[i].split(",")
    r1 = tmp[0]
    r2 = tmp[1]
    r1s = [int(ss) for ss in r1.split("-")]
    r2s = [int(ss) for ss in r2.split("-")]

    f.append(set(range(r1s[0], r1s[1]+1)))
    s.append(set(range(r2s[0], r2s[1]+1)))

fully_contained = []
for (a, b) in zip(f, s):
    if a.issubset(b):
        fully_contained.append(a)
    elif b.issubset(a):
        fully_contained.append(b)
    else:
        pass

# print(fully_contained)
print(len(fully_contained))

is_overlapping = 0
for (a, b) in zip(f, s):
    if a.isdisjoint(b):
        pass
    else:
        is_overlapping += 1

print(is_overlapping)
