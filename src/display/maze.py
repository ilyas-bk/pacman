"""Use the assigned maze package in the Pac-Man game.

A position is written as (x, y): x is the column and y is the row.
A cell number uses these wall bits: 1 north, 2 east, 4 south, 8 west.
"""

from dataclasses import dataclass


Position = tuple[int, int]

# change_x, change_y, current wall, wall on the next cell
DIRECTIONS = {
    "up": (0, -1, 1, 4),
    "right": (1, 0, 2, 8),
    "down": (0, 1, 4, 1),
    "left": (-1, 0, 8, 2),
}


class MazeGenerationError(RuntimeError):
    """The assigned maze package could not create a maze."""


@dataclass
class MazeGrid:
    """A checked maze grid returned by the assigned package.

    Attributes:
        cells: Maze data. Read a cell with cells[y][x].
        entry: Start cell as (x, y).
        exit: End cell as (x, y).
    """

    cells: list[list[int]]
    entry: Position
    exit: Position

    def __post_init__(self) -> None:
        """Reject empty, uneven, or invalid maze data."""
        if not self.cells or not self.cells[0]:
            raise ValueError("The maze must contain at least one cell.")

        width = len(self.cells[0])
        for row in self.cells:
            if len(row) != width:
                raise ValueError("Every maze row must have the same width.")
            for cell in row:
                if isinstance(cell, bool) or not isinstance(cell, int):
                    raise ValueError("Every maze cell must be an integer.")
                if not 0 <= cell <= 15:
                    raise ValueError("Every maze cell must be from 0 to 15.")

        if not self.inside(self.entry) or not self.inside(self.exit):
            raise ValueError(
                "The maze entry and exit must be inside the maze."
            )

    @property
    def width(self) -> int:
        """Return the number of columns."""
        return len(self.cells[0])

    @property
    def height(self) -> int:
        """Return the number of rows."""
        return len(self.cells)

    def inside(self, position: Position) -> bool:
        """Return whether position is inside the grid.

        Args:
            position: A coordinate written as (x, y).
        """
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def cell(self, position: Position) -> int | None:
        """Return a cell's wall number, or None outside the grid.

        Args:
            position: A coordinate written as (x, y).
        """
        if not self.inside(position):
            return None
        x, y = position
        return self.cells[y][x]

    def is_open(self, position: Position) -> bool:
        """Return whether a player or ghost can stand in the cell.

        Cell 15 is the package's fully closed cell, used by its ``42`` shape.
        """
        value = self.cell(position)
        return value is not None and value != 15

    def can_move(self, position: Position, direction: str) -> bool:
        """Return whether one step is possible in direction.

        Args:
            position: Starting coordinate as (x, y).
            direction: ``up``, ``right``, ``down``, or ``left``.
        """
        if direction not in DIRECTIONS or not self.is_open(position):
            return False

        change_x, change_y, wall, opposite_wall = DIRECTIONS[direction]
        next_position = (position[0] + change_x, position[1] + change_y)
        if not self.is_open(next_position):
            return False

        current_cell = self.cell(position)
        next_cell = self.cell(next_position)
        if current_cell is None or next_cell is None:
            return False

        return not (current_cell & wall) and not (next_cell & opposite_wall)

    def available_moves(
        self,
        position: Position,
    ) -> list[tuple[str, Position]]:
        """Return every open direction and its destination from position.

        Args:
            position: Starting coordinate as (x, y).
        """
        moves: list[tuple[str, Position]] = []
        for direction, values in DIRECTIONS.items():
            change_x, change_y, _, _ = values
            if self.can_move(position, direction):
                destination = (
                    position[0] + change_x,
                    position[1] + change_y,
                )
                moves.append((direction, destination))
        return moves


def generate_maze(width: int, height: int, seed: int = 0) -> MazeGrid:
    """Generate a maze with the assigned external package.

    Args:
        width: Maze width, from 15 through 25.
        height: Maze height, from 15 through 25.
        seed: A positive seed repeats a maze. Zero makes a random maze.

    Returns:
        A checked MazeGrid ready for the game.

    Raises:
        ValueError: If a size or seed is invalid.
        MazeGenerationError: If the package is missing or fails.
    """
    if isinstance(width, bool) or not isinstance(width, int):
        raise ValueError("Maze width must be an integer.")
    if isinstance(height, bool) or not isinstance(height, int):
        raise ValueError("Maze height must be an integer.")
    if not 15 <= width <= 25 or not 15 <= height <= 25:
        raise ValueError("Maze width and height must be from 15 to 25.")
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError("Maze seed must be a non-negative integer.")

    try:
        from mazegenerator import MazeGenerator

        generator = MazeGenerator(
            size=(width, height),
            perfect=False,
            seed=seed,
        )
        cells = [list(row) for row in generator.maze]
        return MazeGrid(
            cells=cells,
            entry=generator.maze_entry,
            exit=generator.maze_exit,
        )
    except Exception as error:
        raise MazeGenerationError(
            f"Could not generate the maze: {error}"
        ) from error


# def main() -> None:
#     """Generate a maze and test its functions."""

#     # Generate a maze with 15 columns and 15 rows.
#     maze = generate_maze(width=15, height=15, seed=42)

#     # Display maze information.
#     print("=== MAZE INFORMATION ===")
#     print("Width:", maze.width)
#     print("Height:", maze.height)
#     print("Entry:", maze.entry)
#     print("Exit:", maze.exit)

#     # Display the generated cells.
#     print("\n=== MAZE CELLS ===")
#     for row in maze.cells:
#         print(row)

#     # Test one position.
#     position = maze.entry

#     print("\n=== MOVEMENT TEST ===")
#     print("Current position:", position)
#     print("Is inside maze:", maze.inside(position))
#     print("Is cell open:", maze.is_open(position))
#     print("Cell value:", maze.cell(position))

#     # Show possible moves.
#     moves = maze.available_moves(position)
#     print("Available moves:", moves)

#     # Test each direction.
#     for direction in ("up", "right", "down", "left"):
#         result = maze.can_move(position, direction)
#         print("Can move", direction + ":", result)


# if __name__ == "__main__":
#     main()
