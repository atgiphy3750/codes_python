from random import shuffle
from time import sleep
from os import system


class Wall(object):
    def __init__(self):
        self.up = True
        self.down = True
        self.left = True
        self.right = True

    def remove_wall(self, direction: str):
        if direction == "up":
            self.up == False
        elif direction == "down":
            self.down = False
        elif direction == "left":
            self.left = False
        elif direction == "right":
            self.right = False
        else:
            print("Not a valid direction")

    def get_walls(self) -> int:
        result: int = 0
        if self.up:
            result += 8
        if self.down:
            result += 4
        if self.left:
            result += 2
        if self.right:
            result += 1
        return result


class Grid(object):
    characters = list("┼┤├│┴┘└╵┬┐┌╷─╴╶ ")

    def __init__(self):
        self.visited = False
        self.walls = Wall()

    def __str__(self):
        walls = self.walls.get_walls()
        return Grid.characters[walls]


class Point(object):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Board(object):
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.board = [Grid() for _ in range(x_size * y_size)]
        self.__directions = [Board.UP, Board.DOWN, Board.LEFT, Board.RIGHT]
        self.stack = [Point(0, 0)]

        self.board[self.get_grid_index(Point(0, 0))].visited = True

    def get_grid_index(self, point: Point) -> int:
        """
        Returns actual index of given Point(x, y).
        """
        return (self.x_size) * point.y + point.x

    def step(self) -> None:
        shuffle(self.__directions)
        direction: Point
        current_point: Point = self.stack[-1]
        for direction in self.__directions:
            next_point: Point = current_point + direction
            if self.is_valid_position(next_point):
                self.board[self.get_grid_index(next_point)].visited = True

                self.handle_remove_wall(direction, current_point)

                self.stack.append(next_point)
                break
        else:
            self.stack.pop()

    def is_valid_position(self, point: Point) -> bool:
        if 0 <= point.x < self.x_size and 0 <= point.y < self.y_size:
            if not self.board[self.get_grid_index(point)].visited:
                return True
        return False

    def handle_remove_wall(self, direction: Point, point: Point):
        if direction == Board.UP:
            self.board[self.get_grid_index(point)].walls.up = False
            self.board[self.get_grid_index(point + Board.UP)].walls.down = False
        elif direction == Board.DOWN:
            self.board[self.get_grid_index(point)].walls.down = False
            self.board[self.get_grid_index(point + Board.DOWN)].walls.up = False
        elif direction == Board.LEFT:
            self.board[self.get_grid_index(point)].walls.left = False
            self.board[self.get_grid_index(point + Board.LEFT)].walls.right = False
        elif direction == Board.RIGHT:
            self.board[self.get_grid_index(point)].walls.right = False
            self.board[self.get_grid_index(point + Board.RIGHT)].walls.left = False
        else:
            print(f"{direction} error")

    def __str__(self):
        result: str = ""
        for y in range(self.y_size):

            result += (
                "".join(
                    map(
                        str,
                        self.board[0 + self.x_size * y : self.x_size + self.x_size * y],
                    )
                )
                + "\n"
            )
        return result


def main():
    board = Board(40, 30)
    while True:
        system("clear")
        board.step()
        print(board)
        sleep(0.016)


if __name__ == "__main__":
    main()
