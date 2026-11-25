from ..common.models import Position
from .maze import Maze, Direction
import time


class Player:
    def __init__(self, position: Position):
        self.position = position

    def move(self, maze: Maze, direction: Direction):
        allowed = maze.can_move(self.position, direction)

        if allowed:
            match direction:
                case Direction.NORTH:
                    self.move_north()
                case Direction.EAST:
                    self.move_east()
                case Direction.SOUTH:
                    self.move_south()
                case Direction.WEST:
                    self.move_west()

    def move_north(self):
        self.position.y -= 1

    def move_east(self):
        self.position.x += 1

    def move_south(self):
        self.position.y += 1

    def move_west(self):
        self.position.x -= 1


# ---------------- tests
import curses

def draw_maze(stdscr, maze, player, top=0, left=32):
    grid = maze.grid
    h, w = len(grid), len(grid[0])

    def put(y, x, s, attr=0):
        try:
            stdscr.addstr(y, x, s, attr)
        except curses.error:
            pass

    for r in range(h + 1):
        for c in range(w + 1):
            put(top + 2 * r, left + 4 * c, "+")

    for y in range(h):
        for x in range(w):
            cell = grid[y][x]
            row, col = top + 2 * y, left + 4 * x

            put(row,     col + 1, "---" if cell & Direction.NORTH.value else "   ")
            put(row + 2, col + 1, "---" if cell & Direction.SOUTH.value else "   ")
            put(row + 1, col,     "|"   if cell & Direction.WEST.value  else " ")
            put(row + 1, col + 4, "|"   if cell & Direction.EAST.value  else " ")
            put(row + 1, col + 1, "   ") 

    px, py = player.position.x, player.position.y
    put(top + 2 * py + 1, left + 4 * px + 2, "@", curses.A_BOLD)


def main(stdscr):
    player = Player(Position(7, 7))
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

    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.timeout(50)

    moves = {
        ord('w'): Direction.NORTH,
        ord('a'): Direction.WEST,
        ord('s'): Direction.SOUTH,
        ord('d'): Direction.EAST,
    }

    stdscr.addstr(0, 0, "WASD to move (q to quit)")

    def redraw():
        x, y = player.position.x, player.position.y
        stdscr.addstr(3, 0, f"Position: {player.position}     ")
        stdscr.addstr(4, 0, f"Cell value: {maze.grid[y][x]:2}  ")
        for i, d in enumerate(Direction):
            stdscr.addstr(5 + i, 0, f"{d.name:<5}: {maze.can_move(player.position, d)}   ")
        draw_maze(stdscr, maze, player)
        stdscr.refresh()

    redraw()

    while True:
        key = stdscr.getch()
        if key == -1:
            continue
        if key == ord('q'):
            break
        if key in moves:
            while maze.can_move(player.position, moves[key]): # this controlls the automatic movement - it shouldn't..
                time.sleep(.2)
                player.move(maze, moves[key])
                redraw()


if __name__ == "__main__":
    curses.wrapper(main)

