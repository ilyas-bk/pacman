from mazegenerator import MazeGenerator
from tui_display import MazeRenderer


class Maze:
    "Dinamic maze, tracks player, ghost and pac-gum stats"

    def __init__(self, maze: list[list[int]]):
        self.maze = maze



if __name__ == "__main__":
    def test_maze():
        generator = MazeGenerator()
        maze = generator.maze
        renderer = MazeRenderer(maze)
        renderer.display_maze(renderer.maze, False, False, [])

    test_maze()
