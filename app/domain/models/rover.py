from typing import NamedTuple


class Position:
    x: int
    y: int
    direction: str

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def get_coordinates(self):
        return Coordinates(self.x, self.y)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction}"


class Coordinates:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Rover(NamedTuple):
    start_position: Position
    command_sequence: str

    def __str__(self) -> str:
        return f"({self.start_position}, {self.command_sequence})"
