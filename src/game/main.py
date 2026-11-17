from models import GameState

from player import Position
from ghost import GhostState
from mazegenerator import MazeGenerator
from tui_display import MazeRenderer


if __name__ == "__main__":
    pos = Position([8, 8])
    g1 = GhostState([0, 0])
    g2 = GhostState([-1, 0])
    g3 = GhostState([0, -1])
    g4 = GhostState([-1, -1])
    generator = MazeGenerator()
    maze = generator.maze
    renderer = MazeRenderer(maze)
    renderer.display_maze(renderer.maze, False, False, [])


    game = GameState()
    game.maze = []
    game.player = pos
    game.ghosts = [g1, g2, g3, g4]
    game.score = 0
    game.lives = 3
    game.level = 0
    game.remaining_time = 90

