"""Notifier module for sending notifications."""


class Notifier:
    """Notifier - Sends notifications."""

    def __init__(self, threshold: int = 0) -> None:
        """
        Initialize the notifier with a threshold.

        Args:
            threshold: The threshold value for notifications
        """
        self.threshold = threshold

    def notify(self, message: str) -> None:
        """Send a notification."""
        print(f"NOTIFICATION: {message}")

    def send_alert(self, value: float) -> bool:
        """
        Send an alert if the value exceeds the threshold.

        Args:
            value: The value to check against the threshold

        Returns:
            True if an alert was sent, False otherwise
        """
        if value > self.threshold:
            self.notify(f"Alert: Value {value} exceeds threshold {self.threshold}")
            return True
        return False
