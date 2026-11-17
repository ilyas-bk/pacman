
class Position:

    def __init__(self, start: list[int, int]):
        self.x = start[0]
        self.y = start[1]

    # move methods should check for boundries.. or only when I call them?
    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1
