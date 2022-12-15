import numpy as np
from aoc_utility import get_puzzle_input


TEST = """30373
25512
65332
33549
35390"""


def main():
    tree_rows = [list(row) for row in get_puzzle_input(8).split()]
    trees = np.array(tree_rows, dtype="int")
    
    # Test:
    trees = np.array([list(row) for row in TEST.split()], dtype="int")
    
    print(trees, trees.shape)

    visible = np.full(trees.shape, False)
    visible[0] = True
    visible[visible.shape[0] - 1] = True
    visible[:, 0] = True
    visible[:, visible.shape[1] - 1] = True

    for row in range(1, trees.shape[0] - 1):
        for col in range(1, trees.shape[1] - 1):
            height = trees[row, col]
            up_higher = (trees[:row, col] >= height).sum() > 0
            left_higher = (trees[row, :col] >= height).sum() > 0
            down_higher = (trees[row + 1:, col] >= height).sum() > 0
            right_higher = (trees[row, col + 1:] >= height).sum() > 0
            
            visible[row, col] = not up_higher \
                or not left_higher \
                or not down_higher \
                or not right_higher

    print(visible)
    print(f"{visible.sum()=}")

    #=== Part II ==============================================================

    for row in range(trees.shape[0]):
        for col in range(trees.shape[1]):
            height = trees[row, col]

            if row > 0:
                up = trees[row - 1::-1, col] >= height
            else:
                up = np.array([])

            if col > 0:
                left = trees[row, col - 1::-1] >= height
            else:
                left = np.array([])
            
            down = trees[row + 1:, col] >= height
            right = trees[row, col + 1:] >= height

            dirs = [up, left, down, right]
            distances = []
            for dir in dirs:
                for index, el in enumerate(dir):
                    if el:
                        distances.append(index + 1)
                        break
            print(f"{distances=}")


if __name__ == "__main__":
    main()
