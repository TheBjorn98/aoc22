with open("input_6.txt", "r") as f:
    data = f.read()
    data.replace("\n", "")

# start: 5, 6, 10, 11
trials = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

def seek_start(signal: str, marker_size: int):
    for i in range(marker_size, len(signal)):
        s = signal[i-marker_size:i]
        if (len(set(s)) == marker_size):
            return i

for sig in trials:
    print(seek_start(sig, 14))

print(seek_start(data, 14))