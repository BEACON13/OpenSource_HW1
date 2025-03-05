from unittest.mock import MagicMock, patch

import pytest

from src.calculator import add, multiply, subtract
from src.logger import create_logger
from src.notifier import create_notifier


class TestEndToEnd:
    @patch("pathlib.Path.open", new_callable=MagicMock)
    @patch("datetime.datetime")
    def test_complete_calculation_workflow(
        self,
        mock_datetime: MagicMock,
        mocked_file: MagicMock,
    ) -> None:
        """
        Test the complete calculation, logging, and notification workflow.

        This test simulates the full scenario of a user using the calculator,
        the system logging the operations.
        """
        mock_datetime.now.return_value.strftime.return_value = "2025-02-13 15:30:00"

        logger = create_logger("end_to_end_test.log")
        notifier = create_notifier(threshold=10)

        # Test scenario 1: calculation with a result below the threshold
        small_result = add(3, 4)
        logger.log_calculation("add", 3, 4, small_result)
        notification_sent = notifier.send_alert(small_result)

        assert small_result == 7
        assert not notification_sent  # Confirm no notification was sent

        # Test scenario 2: calculation with a result above the threshold
        large_result = multiply(5, 3)
        logger.log_calculation("multiply", 5, 3, large_result)
        notification_sent = notifier.send_alert(large_result)

        assert large_result == 15
        assert notification_sent  # Confirm a notification was sent

        # Verify logs
        handle = mocked_file.return_value.__enter__.return_value
        log_calls = handle.write.call_args_list

        expected_logs = [
            "2025-02-13 15:30:00 - add(3, 4) = 7\n",
            "2025-02-13 15:30:00 - multiply(5, 3) = 15\n",
        ]
        assert len(log_calls) == 2
        assert log_calls[0][0][0] == expected_logs[0]
        assert log_calls[1][0][0] == expected_logs[1]

    @pytest.mark.parametrize(
        ("operation", "a", "b", "expected", "should_notify"),
        [
            pytest.param("add", 5, 3, 8, False, id="addition_below_threshold"),
            pytest.param(
                "multiply",
                6,
                2,
                12,
                True,
                id="multiplication_above_threshold",
            ),
            pytest.param("subtract", 15, 5, 10, False, id="subtraction_at_threshold"),
        ],
    )
    @patch("pathlib.Path.open", new_callable=MagicMock)
    def test_multiple_operations_workflow(
        self,
        mocked_file: MagicMock,
        operation: str,
        a: int,
        b: int,
        expected: int,
        *,
        should_notify: bool,
    ) -> None:
        # Test the complete workflow of different types of operations.
        logger = create_logger("operations_test.log")
        notifier = create_notifier(threshold=10)
        result = None

        if operation == "add":
            result = add(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "subtract":
            result = subtract(a, b)

        logger.log_calculation(operation, a, b, result)

        assert result == expected

        notification_sent = notifier.send_alert(result)
        assert notification_sent == should_notify

        handle = mocked_file.return_value.__enter__.return_value
        log_content = handle.write.call_args_list[-1][0][0]
        assert f"{operation}({a}, {b}) = {result}" in log_content
