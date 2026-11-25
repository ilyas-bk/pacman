from dataclasses import dataclass
from enum import Enum

try:
    from src.game.maze import Maze
except Exception:
    class Maze:
        pass


class Movement(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class Position:
    x: int
    y: int


@dataclass
class GhostState:
    x: int
    y: int
    scared: bool


@dataclass
class GameState:
    maze: list[list[int]]
    player: Position
    ghosts: list[GhostState]
    score: int
    lives: int
    level: int
    remaining_time: float
