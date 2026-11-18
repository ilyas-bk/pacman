from dataclasses import dataclass

try:
    from src.game import GhostState
except ImportError:
    class GhostState:
        pass

try:
    from src.game import Position
except ImportError:
    class Position:
        pass




@dataclass
class GameState:
    maze: list[list[int]]
    player: Position
    ghosts: list[GhostState]
    score: int
    lives: int
    level: int
    remaining_time: float
