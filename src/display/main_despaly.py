from pathlib import Path
import pygame

from .config import load_config
from .maze import generate_maze
from .maze_display import draw_maze


def des_main():
    """Load the configuration, generate mazes, and display each level."""

    # 1. Load the configuration
    config_path = Path("config.json")
    config = load_config(config_path)

    # 2. Generate all mazes
    mazes = []

    for level in config["level"]:
        maze_des = generate_maze(
            width=level["width"],
            height=level["height"],
            seed=config["seed"],
        )
        mazes.append(maze_des)

    # 3. Set the initial level
    current_level = 0

    # 4. Set the size of each maze cell
    cell_size = 30

    # 5. Initialize Pygame
    pygame.init()

    # # Draw the current maze
    # screen.fill((0, 0, 0))
    # draw_maze(screen, current_maze, cell_size)

    # pygame.display.flip()

    # Remember which level the window was sized for, and limit the speed
    window_level = None
    clock = pygame.time.Clock()

    # 6. Keep the game running
    running = True

    while running:

        # Get the maze for the current level
        current_maze = mazes[current_level]

        # Calculate the window dimensions
        screen_width = current_maze.width * cell_size
        screen_height = current_maze.height * cell_size

        # Create or resize the window only when the level changes
        if window_level != current_level:
            screen = pygame.display.set_mode((screen_width, screen_height))
            window_level = current_level

        # Draw the current maze
    # Draw the current maze
        screen.fill((0, 0, 0))
        draw_maze(screen, current_maze, cell_size)

        pygame.display.flip()
        clock.tick(60)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Press N to move to the next level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    if current_level < len(mazes) - 1:
                        current_level = current_level + 1

    pygame.quit()


if __name__ == "__main__":
    des_main()
