from abc import ABC

from app.application.exceptions import CommandError
from app.domain.enums import RoverControls
from app.domain.models.rover import Rover, Position
from app.domain.models.strategy import MoveRight, MoveLeft, MoveForward


class RoverExecution(ABC):
    right = MoveRight()
    left = MoveLeft()
    forward = MoveForward()

    def execute_rover_positions(self, rover: list[Rover]) -> list[Position]:
        rover_positions = list(
            [combination.start_position for combination in rover]
        )
        print(rover, 'start')
        for combination in rover:
            print('combination.start_position ', combination.start_position)

        for i, (_, command_sequence) in enumerate(rover):
            for command in command_sequence.upper():
                rover_positions[i] = self.control_rover(
                    command,
                    rover_positions[i],
                )
        return rover_positions

    def control_rover(self, control: str, position: Position) -> Position:
        if control == RoverControls.RIGHT.value:
            return self.right.move_rover(position)
        elif control == RoverControls.LEFT.value:
            return self.left.move_rover(position)
        elif control == RoverControls.MOVE_FORWARD.value:
            return self.forward.move_rover(position)
        raise CommandError(control)
