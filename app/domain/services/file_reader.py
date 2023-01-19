import sys
from abc import ABC
from typing import TextIO

from app.domain.models.rover import Rover, Position


class FileReaderService(ABC):
    def get_file_coordinates(self, file_handle: TextIO) -> list[Rover]:
        x, y = file_handle.readline().strip().split()
        combinations = []

        try:
            for i, line in enumerate(file_handle.readlines()):
                if i % 2 == 0:
                    x, y, direction = line.strip().split()
                    start_position = Position(int(x), int(y), direction)
                else:
                    command_sequence = line.strip()
                    combinations.append(Rover(start_position, command_sequence))
        except:
            print("An error occurred.")

        return combinations
