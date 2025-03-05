"""API for the Logger component."""

from typing import Optional

from .logger import Logger


def create_logger(filename: str = "default.log") -> Logger:
    """
    Create a new logger instance.

    Args:
        filename: The name of the log file

    Returns:
        A new Logger instance
    """
    return Logger(filename)


def log_message(message: str, logger: Optional[Logger] = None) -> None:
    """
    Log a message using the specified or default logger.

    Args:
        message: The message to log
        logger: The logger to use, or None to create a default one
    """
    if logger is None:
        logger = create_logger()
    logger.log(message)


def log_error(error: str, logger: Optional[Logger] = None) -> None:
    """
    Log an error message using the specified or default logger.

    Args:
        error: The error message to log
        logger: The logger to use, or None to create a default one
    """
    if logger is None:
        logger = create_logger()
    logger.log_error(error)


def log_calculation(
    operation: str, a: float, b: float, result: float, logger: Optional[Logger] = None
) -> None:
    """
    Log a calculation using the specified or default logger.

    Args:
        operation: The operation name
        a: The first operand
        b: The second operand
        result: The calculation result
        logger: The logger to use, or None to create a default one
    """
    if logger is None:
        logger = create_logger()
    logger.log_calculation(operation, a, b, result)
