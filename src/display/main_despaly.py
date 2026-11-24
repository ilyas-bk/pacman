from pathlib import Path
import pygame

from .config import load_config
from .maze import generate_maze
from .maze_display import draw_maze


def des_main():
    """Load the configuration, generate mazes, and display each level."""
    config_path = Path("config.json")
    config = load_config(config_path)

    mazes = []
    for level in config["level"]:
        maze_des = generate_maze(
            width=level["width"],
            height=level["height"],
            seed=config["seed"],
        )
        mazes.append(maze_des)

    current_level = 0
    cell_size = 30
    margin = 4

    pygame.init()
    window_level = None
    clock = pygame.time.Clock()
    running = True

    while running:
        current_maze = mazes[current_level]
        screen_width = current_maze.width * cell_size + 2 * margin
        screen_height = current_maze.height * cell_size + 2 * margin

        if window_level != current_level:
            screen = pygame.display.set_mode((screen_width, screen_height))
            window_level = current_level

        screen.fill((0, 0, 0))
        draw_maze(screen, current_maze, cell_size, margin)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    if current_level < len(mazes) - 1:
                        current_level = current_level + 1
                elif event.key == pygame.K_p and current_level > 0:
                    current_level = current_level - 1
                # Quit the game
                elif event.key == pygame.K_q:
                    running = False

    pygame.quit()


if __name__ == "__main__":
    des_main()
