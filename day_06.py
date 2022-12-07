from aoc_utility import get_puzzle_input


def get_marker(data: str, offset=4):
    for start in range(len(data) - offset):
        if len(set(marker:=data[start:start + offset])) == offset:
            start += offset
            print(f"{marker=} {start=}")
            return marker, start

def main():
    data = get_puzzle_input(6)
    get_marker(data)
    get_marker(data, 14)

    


if __name__ == "__main__":
    get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")
    get_marker("nppdvjthqldpwncqszvftbrmjlhg")
    get_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    get_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
    get_marker("nppdvjthqldpwncqszvftbrmjlhg", 14)
    get_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
    get_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)
    main()


