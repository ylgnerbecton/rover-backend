class CommandError(Exception):
    def __init__(self, command: str, message=None) -> None:
        super().__init__()
        self.command = command
        self.message = message or f"Invalid command {self.command}"
