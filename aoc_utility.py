

def get_puzzle_input(number: int) -> str:
    with open(f"input_{number:02}.txt") as input_file:
        return input_file.read()


if __name__ == "__main__":
    # Testing first 3 puzzle inputs:
    for i in range(1, 4):
        print(get_puzzle_input(i))
        