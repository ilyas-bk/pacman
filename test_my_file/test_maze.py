"""Test the Pac-Man maze generator."""

# from src.display.maze import generate_maze
from src.display.maze import generate_maze


def main() -> None:
    """Generate a maze and test its functions."""

    # Generate a maze with 15 columns and 15 rows.
    maze = generate_maze(width=15, height=15, seed=42)

    # Display maze information.
    print("=== MAZE INFORMATION ===")
    print("Width:", maze.width)
    print("Height:", maze.height)
    print("Entry:", maze.entry)
    print("Exit:", maze.exit)

    # Display the generated cells.
    print("\n=== MAZE CELLS ===")
    for row in maze.cells:
        print(row)

    # Test one position.
    position = maze.entry

    print("\n=== MOVEMENT TEST ===")
    print("Current position:", position)
    print("Is inside maze:", maze.inside(position))
    print("Is cell open:", maze.is_open(position))
    print("Cell value:", maze.cell(position))

    # Show possible moves.
    moves = maze.available_moves(position)
    print("Available moves:", moves)

    # Test each direction.
    for direction in ("up", "right", "down", "left"):
        result = maze.can_move(position, direction)
        print("Can move", direction + ":", result)


if __name__ == "__main__":
    main()