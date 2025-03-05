"""Logger module for logging operations."""

import datetime
from datetime import timezone
from pathlib import Path


class Logger:
    """Logger - Records messages with timestamps."""

    def __init__(self, filename: str = "default.log") -> None:
        """Initialize logger with a filename."""
        self.filename = filename

    def log(self, message: str) -> None:
        """Record a message with a timestamp to a log file."""
        timestamp = datetime.datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        log_file = Path(self.filename)
        with log_file.open("a") as file:
            file.write(log_message)

    def log_error(self, error: str) -> None:
        """Specifically log errors."""
        self.log(f"Error: {error}")

    def log_calculation(
        self, operation: str, a: float, b: float, result: float
    ) -> None:
        """Log a calculation and its result."""
        message = f"{operation}({a}, {b}) = {result}"
        self.log(message)
