from typing import Any

from .models import GameState

class Game:
    "Game class for the game logic (player movement, maze status, ghosts...)"

    def update(self) -> None:
        "update the maze status"
        pass

    def get_status(self) -> "GameState":
        "returns the state of the game"
        pass

    def move_player(self, Direction: Any) -> None:
        "move the player to the indicated direction"
        pass
