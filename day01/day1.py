from util import read_input_by_day


def find_max(array):
    max_ind = 0
    max_val = 0
    for (i, e) in enumerate(array):
        if e > max_val:
            max_val = e
            max_ind = i
    return max_ind, max_val


if __name__ == "__main__":
    data = read_input_by_day(1, 1)

    elves = [0]

    for s in data:
        s.replace("\n", "")
        if s == "\n":
            elves.append(0)
        else:
            i = int(s)
            elves[-1] += i

    max_ind = 0
    max_val = 0
    for (i, e) in enumerate(elves):
        if e > max_val:
            max_val = e
            max_ind = i

    print(f"Elf number {max_ind} has {max_val} calories.")

    top = max_val
    elves[max_ind] = 0

    for k in range(2):
        mi, mv = find_max(elves)
        print(f"Elf number {mi} has {mv} calories.")
        top += mv
        elves[mi] = 0

    print(f"Top three elves has {top} calories.")

