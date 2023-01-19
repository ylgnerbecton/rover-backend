import sys

from app.domain.services.file_reader import FileReaderService
from app.domain.services.rover_execution import RoverExecution

file_reader = FileReaderService()
rover_execution = RoverExecution()

if __name__ == "__main__":
    if len(sys.argv) > 0:
        filename = sys.argv[1]
    else:
        filename = input("Please, input your rover combinations file name: ")

    try:
        with open(filename, "rt", encoding="utf-8") as file:
            rover = file_reader.get_file_coordinates(file)
        results = rover_execution.execute_rover_positions(rover)

        for rover_position in results:
            print(rover_position)

    except FileNotFoundError:
        print(f"Your file '{filename}' could not be found.")
