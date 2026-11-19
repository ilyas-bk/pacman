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
    # renderer = MazeRenderer(maze)
    # renderer.display_maze(renderer.maze, False, False, [])

    game_state = GameState(
        maze,
        position,
        [g1, g2, g3, g4],
        0,
        3,
        0,
        90
        )

    # the ghosts should follow :o
    # must implement the maze represenation, now the ghosts will have to find a path to the player
    # game = Game(game_state)
    # game.start()
    print(maze)


if __name__ == "__main__":
    back()


