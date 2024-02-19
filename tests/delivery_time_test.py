from datetime import datetime, timedelta
from typing import List
from unittest.mock import Mock, call, patch
import os

import pytest

from unbabel_cli.utils.delivery_time import (
    AverageCalculator,
    display_average_delivery_time,
    process_avg_delivery_time,
)

"""
Test for the delivery_time module and his functions, that are used to calculate the moving average of the delivery time
"""


@pytest.fixture
def mock_display():
    return Mock()


@patch("unbabel_cli.utils.delivery_time.display_average_delivery_time")
def test_calculate_delivery_time_avg(mock_display):
    events = [
        {"timestamp": datetime(2018, 12, 26, 18, 11, 8, 509654), "duration": 20},
        {"timestamp": datetime(2018, 12, 26, 18, 15, 19, 903159), "duration": 31},
        {"timestamp": datetime(2018, 12, 26, 18, 23, 19, 903159), "duration": 54},
    ]
    window_size = 10

    process_avg_delivery_time(events, window_size)

    expected_calls = [
        call(datetime(2018, 12, 26, 18, 11), 0, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 12), 20, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 13), 20, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 14), 20, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 15), 20, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 16), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 17), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 18), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 19), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 20), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 21), 25.5, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 22), 31.0, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 23), 31.0, "output.jsonl"),
        call(datetime(2018, 12, 26, 18, 24), 42.5, "output.jsonl"),
    ]

    mock_display.assert_has_calls(expected_calls, any_order=True)


def test_display_average_delivery_time(capsys):
    date = datetime(2018, 12, 26, 18, 11)
    average_delivery_time = 20

    expected_output = "{'date': '2018-12-26 18:11:00', 'average_delivery_time': 20}\n"
    output_file = "./tests/files/testing_display_output.jsonl"

    display_average_delivery_time(date, average_delivery_time, output_file)

    captured = capsys.readouterr()
    assert captured.out == (expected_output)

    with open(output_file, "r") as f:
        output = f.readlines()
        assert output == [expected_output]

    os.remove(output_file)


def test_average_calculator():
    average_calculator = AverageCalculator(10)
    value1 = 20
    value2 = 30
    value3 = 40
    average_calculator.add_active_value(0, value1)
    average_calculator.add_active_value(1, value2)

    assert average_calculator.get_average() == (value1 + value2) / 2

    average_calculator.add_active_value(2, value3)

    assert average_calculator.get_average() == (value1 + value2 + value3) / 3

    average_calculator.remove_active_value(10)

    assert average_calculator.get_average() == (value2 + value3) / 2

    average_calculator = AverageCalculator(10)

    assert average_calculator.get_average() == 0
    assert not average_calculator.active_values
    assert average_calculator.remove_active_value(1) is None
