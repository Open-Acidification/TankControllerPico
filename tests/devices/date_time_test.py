"""
Test suite for the DateTime class
"""

from datetime import datetime, timedelta
from unittest import mock

from src.devices.date_time import DateTime


def test_datetime_initialization():
    """
    Test that the DateTime class initializes with zero offset and correct uptime start.
    """
    instance = DateTime()

    assert instance._offset == timedelta(0)

    assert abs(datetime.now() - instance._uptime_start) < timedelta(seconds=1)


@mock.patch("src.devices.date_time.datetime")
def test_datetime_current(mock_datetime):
    """
    Test that the current() method returns the correct adjusted time.
    """
    mock_now = datetime(2025, 12, 10, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()
    assert instance.current() == mock_now

    instance._offset = timedelta(hours=1)
    assert instance.current() == mock_now - timedelta(hours=1)


@mock.patch("src.devices.date_time.datetime")
def test_datetime_offset(mock_datetime):
    """
    Test that the offset() method calculates and sets the correct offset.
    """
    mock_now = datetime(2025, 12, 10, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()
    new_time = datetime(2025, 12, 10, 14, 30)
    offset = instance.offset(new_time)

    assert offset == timedelta(hours=1)
    assert instance._offset == timedelta(hours=1)

    assert instance.offset() == timedelta(hours=1)


@mock.patch("src.devices.date_time.datetime")
def test_datetime_uptime(mock_datetime):
    """
    Test that the uptime() method returns the correct elapsed time since initialization.
    """
    mock_start = datetime(2025, 12, 10, 15, 30)
    mock_now = datetime(2025, 12, 10, 16, 30)
    mock_datetime.now.side_effect = [mock_start, mock_now]

    instance = DateTime()

    # Assert uptime() returns the correct elapsed time
    uptime = instance.uptime()
    assert uptime == timedelta(hours=1)
