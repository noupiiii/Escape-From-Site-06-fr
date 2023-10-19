import random as rd

from Position import Position
from Map import Map


class Entity:
    def __init__(self, position: Position, name: str) -> None:

        self.position: Position = position
        self.name: str = name

        self.inaccessible_cases = ['X', 'A']

    def move(self, new_position: Position) -> None:
        self.position: Position = new_position

    def auto_move(self, distance: int) -> None:
        # for deplacement in range(rd.randint(0, distance)):
        pass
