from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8


class Maze:
    "Dinamic maze, track movements and pac-gum availabilities"

    # this tracks the moves availability, for ghosts to follow the player, for the player to move
    def __init__(self, grid: list[list[int]]):
        self.grid = grid


    def has_wall(self, x: int, y: int, direction: Direction) -> bool:
        "checks if the cell has a wall in a direction"
        cell = self.grid[x][y]
        return bool(cell & direction.value)

    def can_move(self, x: int, y: int, direction: Direction) -> bool:
        "checks movement availability for ghosts and player"
        return not self.has_wall(x, y, direction)

    def is_block(self, x: int, y: int) -> bool:
        return self.grid[x][y] == 15


if __name__ == "__main__":
    grid = [[ 9,  5,  5,  5,  1,  3,  9,  3,  9,  1,  1,  1,  5,  1,  3],
            [ 8,  5,  1,  1,  2, 12,  4,  2, 10, 12,  2, 12,  3, 10, 10],
            [10,  9,  6, 12,  2,  9,  5,  2, 10,  9,  0,  3,  8,  2, 10],
            [ 8,  4,  1,  1,  2,  8,  1,  4,  2, 10,  8,  2, 10, 10, 10],
            [ 8,  1,  4,  4,  4,  4,  2,  9,  6, 12,  4,  2, 12,  4,  2],
            [10,  8,  5,  3, 15,  9,  2, 10, 15, 15, 15, 12,  5,  1,  2],
            [ 8,  4,  1,  2, 15, 12,  6,  8,  5,  7, 15,  9,  5,  4,  2],
            [ 8,  5,  2, 10, 15, 15, 15, 10, 15, 15, 15,  8,  1,  1,  2],
            [ 8,  3,  8,  4,  5,  3, 15, 10, 15, 13,  5,  2, 12,  4,  6],
            [10, 10, 12,  5,  1,  2, 15, 10, 15, 15, 15,  8,  5,  1,  3],
            [10, 12,  1,  3, 10, 12,  5,  4,  5,  1,  5,  4,  1,  6, 10],
            [ 8,  1,  6, 10,  8,  1,  1,  5,  1,  2,  9,  1,  4,  1,  6],
            [ 8,  4,  1,  2, 10,  8,  4,  1,  4,  4,  6, 12,  1,  4,  3],
            [10,  9,  4,  2, 12,  4,  1,  0,  1,  1,  1,  3, 12,  3, 10],
            [12,  4,  5,  4,  5,  5,  6, 12,  6, 12,  4,  4,  5,  4,  6]]

    maze = Maze(grid)
    cell = [1, 13]
    print("cell:", grid[cell[0]][cell[1]])
    print("north:", maze.has_wall(*cell, Direction.NORTH))
    print("east:", maze.has_wall(*cell, Direction.EAST))
    print("south:", maze.has_wall(*cell, Direction.SOUTH))
    print("west:", maze.has_wall(*cell, Direction.WEST))


