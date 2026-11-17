
class GhostState:

    def __init__(self, position: list[int, int]):
        self.x = position[0]
        self.y = position[1]
        self.scared: bool = False

