from unittest.mock import MagicMock, patch

import pytest

from src.logger import create_logger
from src.notifier import create_notifier


class TestLoggerNotifierIntegration:
    @pytest.mark.parametrize(
        ("value", "threshold", "should_notify"),
        [
            (15, 10, True),
            (5, 10, False),
            (10, 10, False),
        ],
    )
    @patch("pathlib.Path.open", new_callable=MagicMock)
    def test_notification_based_on_calculation(
        self,
        mocked_file: MagicMock,
        value: int,
        threshold: int,
        *,
        should_notify: bool,
    ) -> None:

        # Test notification based on calculation results
        logger = create_logger("notifier_test.log")
        notifier = create_notifier(threshold=threshold)

        logger.log_calculation("test_operation", value, 0, value)

        assert notifier.send_alert(value) == should_notify

        handle = mocked_file.return_value.__enter__.return_value
        assert "test_operation" in handle.write.call_args_list[-1][0][0]

    @patch("pathlib.Path.open", new_callable=MagicMock)
    def test_error_notification(
        self,
        mocked_file: MagicMock,
    ) -> None:
        """Test notification based on error message."""
        logger = create_logger("error_test.log")
        notifier = create_notifier(threshold=10)

        error_message = "Critical calculation error"
        logger.log_error(error_message)

        assert notifier.send_alert(float("inf"))

        handle = mocked_file.return_value.__enter__.return_value
        assert "Error:" in handle.write.call_args_list[-1][0][0]
