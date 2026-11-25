from src.common.models import Position
from src.common.models import GhostState
from mazegenerator import MazeGenerator
from src import GameState

# for seing the maze - testing
from src.game.tui_display import MazeRenderer

# the game logic
from src.game import Game


# this should be the initial state.
# after that the ghosts + time should start moving.


def back():
    position = Position(7, 7)
    g1 = GhostState(0, 0, False)
    g2 = GhostState(14, 0, False)
    g3 = GhostState(0, 14, False)
    g4 = GhostState(14, 14, False)
    generator = MazeGenerator()
    maze = generator.maze
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
    renderer = MazeRenderer(grid)
    renderer.display_maze(grid, False, False, [])

    # game_state = GameState(
    #     grid,
    #     position,
    #     [g1, g2, g3, g4],
    #     0,
    #     3,
    #     0,
    #     90
    #     )

    # the ghosts should follow :o
    # must implement the maze represenation, now the ghosts will have to find a path to the player
    # game = Game(game_state)
    # game.start()


if __name__ == "__main__":
    back()


