

def main():
    with open("input_01.txt") as f:
        data = f.read()
    
    elfes = [sum([int(c) for c in cal.split()]) for cal in data.split("\n\n")]
    print(elfes)

    elfes = list(sorted(elfes, reverse=True))
    print(s := elfes[:3], sum(s))


if __name__ == "__main__":
    main()
