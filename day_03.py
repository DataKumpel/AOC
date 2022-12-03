import string


PRIORITY = {
    char: prio for prio, char in enumerate(string.ascii_letters, start=1)
}


def main():
    with open("input_03.txt") as f:
        rucksacks = f.readlines()
    
    prio_sum = 0
    for rucksack in rucksacks:
        half_length = len(rucksack) // 2
        comps = rucksack[:half_length], rucksack[half_length:]

        common = set(comps[0]).intersection(set(comps[1]))
        prio_sum += PRIORITY[list(common)[0]]
    
    print(f"{prio_sum=}")

    #=== Part II ==============================================================

    prio_sum = 0
    for index in range(0, len(rucksacks), 3):
        group = [rucksack.strip() for rucksack in rucksacks[index:index + 3]]
        common = set(group[0]).intersection(set(group[1]), set(group[2]))
        prio_sum += PRIORITY[list(common)[0]]
    
    print(f"{prio_sum=}")



if __name__ == "__main__":
    main()
