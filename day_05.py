from aoc_utility import get_puzzle_input


def main():
    data = get_puzzle_input(5).split("\n")
    columns_data = list(reversed(data[:8]))
    columns = [[] for _ in range(9)]

    for col in columns_data:
        for index, i in enumerate(range(1, len(col), len("] [") + 1)):
            if col[i] != " ":
                columns[index].append(col[i])

    columns: list[list[str]]
    columns_p2 = [col.copy() for col in columns]

    instructions_data = data[10:]
    for instruction in instructions_data:
        num_crates, mv_from, mv_to = [int(inst) for inst in instruction.split()[1::2]]
        
        # convert to index:
        mv_from -= 1
        mv_to -= 1

        while num_crates > 0:
            columns[mv_to].append(columns[mv_from].pop())
            num_crates -= 1
    
    tops = "".join([col[-1] for col in columns])
    print(f"{tops=}")

    #=== Part II ==============================================================

    columns = columns_p2
    for instruction in instructions_data:
        num_crates, mv_from, mv_to = [int(inst) for inst in instruction.split()[1::2]]
        
        # convert to index:
        mv_from -= 1
        mv_to -= 1

        move_pack = columns[mv_from][-num_crates:]
        columns[mv_from] = columns[mv_from][:-num_crates]
        columns[mv_to].extend(move_pack)

    tops = "".join([col[-1] for col in columns])
    print(f"{tops=}")


if __name__ == "__main__":
    main()
