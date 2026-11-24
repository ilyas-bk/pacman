import pygame

# from maze import generate_maze


def draw_maze(screen, maze, cell_size):

    for y in range(maze.height):
        for x in range(maze.width):

            cell = maze.cells[y][x]
            pixel_x = x * cell_size
            pixel_y = y * cell_size

            has_top_wall = bool(cell & 1)
            has_right_wall = bool(cell & 2)
            has_bottom_wall = bool(cell & 4)
            has_left_wall = bool(cell & 8)

            # Draw top wall if it exists
            # Draw right wall if it exists
            # Draw bottom wall if it exists
            # Draw left wall if it exists

            if has_top_wall == True:
                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (pixel_x, pixel_y),
                    (pixel_x + cell_size, pixel_y),
                    2,
                )

            if has_right_wall == True:
                # Draw right wall
                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (pixel_x + cell_size, pixel_y),
                    (pixel_x + cell_size, pixel_y + cell_size),
                    2,
                )

            if has_bottom_wall == True:
                # Draw bottom wall
                                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (pixel_x, pixel_y + cell_size),
                    (pixel_x + cell_size, pixel_y + cell_size),
                    2,
                )
            if has_left_wall== True:
                # Draw left wall
                                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (pixel_x, pixel_y),
                    (pixel_x, pixel_y + cell_size),
                    2,
                )