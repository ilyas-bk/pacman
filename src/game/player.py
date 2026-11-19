from src.common.models import Movement
from src.common.models import Position


class Player:
    def __init__(self, position: Position):
        self.position = position


    def move(self, input: Movement):
        match input:
            case Movement.UP:
                pass
            case Movement.RIGHT:
                pass
            case Movement.DOWN:
                pass
            case Movement.LEFT:
                pass


    def move_right(self):
        self.position.x += 1


    def move_left(self):
        self.position.x -= 1


    def move_up(self):
        self.position.y += 1


    def move_down(self):
        self.position.y -= 1
