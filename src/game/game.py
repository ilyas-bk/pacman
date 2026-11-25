from typing import Any
from .. import GameState


class Game:
    "the main Game class for the game logic (player movement, maze status, ghosts...)"
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def start(self):
        while True:
            for ghost in self.game_state.ghosts:
                if ghost.x == self.game_state.player.x and ghost.y == self.game_state.player.y:
                    print("PLAYER EATEN BY GHOST!!!")
                    return
            self.ghost_controller.follow_player()


    def update(self) -> None:
        "update the whole game status, (time, ghosts, postion)"
        pass


    def get_status(self) -> "GameState":
        "returns the current state of the game"
        pass


    def move_player(self, direction: Any) -> None:
        "move the player to the indicated direction"
        pass
