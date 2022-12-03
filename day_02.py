
ROCK, PAPER, SCISSOR = 1, 2, 3
WIN, DRAW, LOOSE = 6, 3, 0

STRAT_ENCODING_1 = {
    ("A", "X"): ROCK + DRAW,      # ROCK == ROCK
    ("A", "Y"): PAPER + WIN,      # ROCK << PAPER
    ("A", "Z"): SCISSOR + LOOSE,  # ROCK >> SCISSOR

    ("B", "X"): ROCK + LOOSE,     # PAPER >> ROCK
    ("B", "Y"): PAPER + DRAW,     # PAPER == PAPER
    ("B", "Z"): SCISSOR + WIN,    # PAPER << SCISSOR

    ("C", "X"): ROCK + WIN,       # SCISSOR << ROCK
    ("C", "Y"): PAPER + LOOSE,    # SCISSOR >> PAPER
    ("C", "Z"): SCISSOR + DRAW,   # SCISSOR == SCISSOR
}

STRAT_ENCODING_2 = {
    ("A", "X"): SCISSOR + LOOSE,
    ("A", "Y"): ROCK + DRAW,
    ("A", "Z"): PAPER + WIN,

    ("B", "X"): ROCK + LOOSE,
    ("B", "Y"): PAPER + DRAW,
    ("B", "Z"): SCISSOR + WIN,

    ("C", "X"): PAPER + LOOSE,
    ("C", "Y"): SCISSOR + DRAW,
    ("C", "Z"): ROCK + WIN,
}


def evaluate_match(strat: tuple[str], is_outcome=False) -> int:
    if is_outcome:
        return STRAT_ENCODING_2[strat]
    else:
        return STRAT_ENCODING_1[strat]


def main():
    with open("input_02.txt") as f:
        data = [tuple(line.split()) for line in f.readlines()]
    
    points = 0
    for strat in data:
        points += evaluate_match(strat)
    print(f"{points=}")

    #=== Part II ==============================================================

    points = 0
    for strat in data:
        points += evaluate_match(strat, is_outcome=True)
    print(f"{points=}")

if __name__ == "__main__":
    main()
