from dataclasses import dataclass

class Position:
    pass

class GhostState:
    pass

class GameStatus:
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
    status: GameStatus