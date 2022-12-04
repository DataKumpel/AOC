from aoc_utility import get_puzzle_input


def pair_to_sections(pair: str) -> tuple[set[int]]:
    """Create two sets of sections from a string input of the form: 'a-b,c-d'

    Args:
        pair (str): A pair in the form of 'a-b,c-d'; a, b, c, d integers

    Returns:
        tuple[set[int]]: two sets in the form {range(a, b+1)}, {range(c, d+1)}
    """
    
    elf1, elf2 = pair.split(",")
    elf1 = [int(part) for part in elf1.split("-")]
    elf2 = [int(part) for part in elf2.split("-")]

    section1 = set(range(elf1[0], elf1[1] + 1))
    section2 = set(range(elf2[0], elf2[1] + 1))

    return section1, section2


def main():
    data = get_puzzle_input(4).split()

    num_contains = 0
    
    for pair in data:
        sections = pair_to_sections(pair)

        if sections[0].issubset(sections[1]) \
            or sections[1].issubset(sections[0]):
            num_contains += 1
    
    print(f"{num_contains=}")

    #=== Part II ==============================================================

    num_overlaps = 0
    
    for pair in data:
        sections = pair_to_sections(pair)
        if not sections[0].isdisjoint(sections[1]):
            num_overlaps += 1
    
    print(f"{num_overlaps=}")


if __name__ == "__main__":
    main()
