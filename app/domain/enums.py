from enum import Enum
from app.domain.models.rover import Coordinates


class CardinalDirection(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class RoverControls(Enum):
    LEFT = "L"
    RIGHT = "R"
    MOVE_FORWARD = "M"


class RoverSpin(Enum):
    N = {
        RoverControls.LEFT.value: CardinalDirection.WEST.value,
        RoverControls.RIGHT.value: CardinalDirection.EAST.value,
        RoverControls.MOVE_FORWARD.value: Coordinates(0, 1),
    }
    E = {
        RoverControls.LEFT.value: CardinalDirection.NORTH.value,
        RoverControls.RIGHT.value: CardinalDirection.SOUTH.value,
        RoverControls.MOVE_FORWARD.value: Coordinates(1, 0),
    }
    S = {
        RoverControls.LEFT.value: CardinalDirection.EAST.value,
        RoverControls.RIGHT.value: CardinalDirection.WEST.value,
        RoverControls.MOVE_FORWARD.value: Coordinates(0, -1),
    }
    W = {
        RoverControls.LEFT.value: CardinalDirection.SOUTH.value,
        RoverControls.RIGHT.value: CardinalDirection.NORTH.value,
        RoverControls.MOVE_FORWARD.value: Coordinates(-1, 0),
    }
