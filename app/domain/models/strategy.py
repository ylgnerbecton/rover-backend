from abc import abstractmethod, ABC

from app.domain.enums import RoverControls, RoverSpin
from app.domain.models.rover import Position


class Strategy(ABC):
    @abstractmethod
    def move_rover(self, position: Position) -> Position:
        pass


class MoveRight(Strategy):
    def move_rover(self, position: Position) -> Position:
        return Position(
            position.x,
            position.y,
            RoverSpin[position.direction].value[RoverControls.RIGHT.value],
        )


class MoveLeft(Strategy):
    def move_rover(self, position: Position) -> Position:
        return Position(
            position.x,
            position.y,
            RoverSpin[position.direction].value[RoverControls.LEFT.value],
        )


class MoveForward(Strategy):
    def move_rover(self, position: Position) -> Position:
        movement = RoverSpin[position.direction].value[RoverControls.MOVE_FORWARD.value]

        return Position(
            position.x + movement.x, position.y + movement.y, position.direction
        )
