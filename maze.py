from random import shuffle
from typing import List

width: int = 16
height: int = 12

directions = shuffle([[0, 1], [1, 0], [0, -1], [-1, 0]])


def generate_maze(grid: List):
    pass


def display_grid(grid: List):
    for line in grid:
        print(" ".join(map(str, line)))


def main():
    grid = [[0] * width for _ in range(height)]
    display_grid(grid)


if __name__ == "__main__":
    main()
