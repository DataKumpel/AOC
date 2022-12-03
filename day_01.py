from aoc_utility import get_puzzle_input


def main():
    data = get_puzzle_input(1)
    
    elfes = [sum([int(c) for c in cal.split()]) for cal in data.split("\n\n")]
    print(elfes)

    elfes = list(sorted(elfes, reverse=True))
    print(s := elfes[:3], sum(s))


if __name__ == "__main__":
    main()
