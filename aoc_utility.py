

def get_puzzle_input(number: int) -> str:
    """Load the input of a inputfile on the same level as cwd.

    Parameters
    ----------
    number : int
        number of the input file => input_02.txt, input_12.txt, etc.

    Returns
    -------
    str
        The input of the given puzzle.
    """
    
    with open(f"input_{number:02}.txt") as input_file:
        return input_file.read()


if __name__ == "__main__":
    # Testing first 3 puzzle inputs:
    for i in range(1, 4):
        print(get_puzzle_input(i))
        