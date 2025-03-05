"""API for the Notifier component."""

from typing import Optional

from .notifier import Notifier


def create_notifier(threshold: int = 0) -> Notifier:
    """
    Create a new notifier instance.

    Args:
        threshold: The threshold value for notifications

    Returns:
        A new Notifier instance
    """
    return Notifier(threshold=threshold)


def notify(message: str, notifier: Optional[Notifier] = None) -> None:
    """
    Send a notification using the specified or default notifier.

    Args:
        message: The message to notify
        notifier: The notifier to use, or None to create a default one
    """
    if notifier is None:
        notifier = create_notifier()
    notifier.notify(message)
