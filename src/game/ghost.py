from src.common.models import GhostState
from src import GameState
import time

# I can modify this to change the ghosts behaviour
class GhostController:

    def __init__(self, game_state: GameState):
        self.game_state = game_state


    def follow_player(self): # the ghosts action, all ghosts share the same behaviour for now
        time.sleep(.5)
        for idx, ghost in enumerate(self.game_state.ghosts):
            self.move_to_player(ghost)
            print(f"ghost {idx}: ({ghost.x}, {ghost.y})")


    def move_to_player(self, ghost: GhostState):
        "generic ghost follow player - to be improved based on self.game_state.maze"
        player = self.game_state.player

        if ghost.scared:
            return

        if player.x < ghost.x:
            ghost.x -= 1
        elif player.x > ghost.x:
            ghost.x += 1
        elif player.y < ghost.y:
            ghost.y -= 1
        elif player.y > ghost.y:
            ghost.y += 1
