from dataclasses import dataclass

from .ghost import GhostState
from .player import Position


# this inits after program run

@dataclass
class GameState:
    maze: list[list[int]]
    player: Position
    ghosts: list[GhostState]
    score: int
    lives: int
    level: int
    remaining_time: float
