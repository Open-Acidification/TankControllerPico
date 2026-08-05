"""
Test suite for the DateTime class.
"""

from datetime import datetime, timedelta
from unittest import mock

from src.devices.date_time import DateTime


def test_datetime_initialization():
    """
    Test that DateTime initializes correctly.
    """
    instance = DateTime()

    assert instance._offset == timedelta(0)
    assert abs(datetime.now() - instance._uptime_start) < timedelta(seconds=1)


@mock.patch("src.devices.date_time.datetime")
def test_current(mock_datetime):
    """
    Test that current() returns the correct adjusted time.
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    # No offset, should return current time
    assert instance.current() == mock_now

    # Add one hour offset
    instance._offset = timedelta(hours=1)

    assert instance.current() == mock_now - timedelta(hours=1)


@mock.patch("src.devices.date_time.datetime")
def test_offset(mock_datetime):
    """
    Test that offset() correctly calculates time difference.
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    new_time = datetime(2026, 7, 29, 14, 30)

    offset = instance.offset(new_time)

    assert offset == timedelta(hours=1)
    assert instance._offset == timedelta(hours=1)


@mock.patch("src.devices.date_time.datetime")
def test_set_as_current(mock_datetime):
    """
    Test that set_as_current() updates the simulated clock.
    Equivalent to C++ setAsCurrent().
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    new_time = datetime(2026, 7, 29, 12, 0)

    instance.set_as_current(new_time)

    assert instance.current() == new_time


@mock.patch("src.devices.date_time.datetime")
def test_now(mock_datetime):
    """
    Test that now() returns the current simulated time.
    Equivalent to C++ DateTime_TC::now().
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    assert instance.now() == mock_now


@mock.patch("src.devices.date_time.datetime")
def test_as16_character_string(mock_datetime):
    """
    Test LCD date/time formatting.

    Equivalent to C++ as16CharacterString().
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    assert instance.as16_character_string() == "2026-07-29 15:30"


@mock.patch("src.devices.date_time.datetime")
def test_year_month_as_path(mock_datetime):
    """
    Test directory path formatting.

    Equivalent to C++ yearMonthAsPath().
    """
    mock_now = datetime(2026, 7, 29, 15, 30)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    assert instance.year_month_as_path() == "/2026/07"


@mock.patch("src.devices.date_time.datetime")
def test_print_to_serial(mock_datetime, capsys):
    """
    Test serial output formatting.

    Equivalent to C++ printToSerial().
    """
    mock_now = datetime(2026, 7, 29, 15, 30, 45)
    mock_datetime.now.return_value = mock_now

    instance = DateTime()

    instance.print_to_serial()

    captured = capsys.readouterr()

    assert captured.out.strip() == "2026-07-29 15:30:45"


@mock.patch("src.devices.date_time.datetime")
def test_uptime(mock_datetime):
    """
    Test uptime calculation.
    """
    start_time = datetime(2026, 7, 29, 15, 30)
    current_time = datetime(2026, 7, 29, 16, 30)

    mock_datetime.now.side_effect = [start_time, current_time]

    instance = DateTime()

    assert instance.uptime() == timedelta(hours=1)