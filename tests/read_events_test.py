from datetime import datetime
from pathlib import Path
from typing import List

from unbabel_cli.utils.interfaces import TranslationEvent
from unbabel_cli.utils.read_events import parse_event, read_event

"""
Simple test for the read_event module and his functions
"""


def assert_event(events: List[TranslationEvent]):
    # sample json, with the first event in the file
    sample_json = {
        "timestamp": "2018-12-26 18:11:08.509654",
        "translation_id": "5aa5b2f39f7254a75aa5",
        "source_language": "en",
        "target_language": "fr",
        "client_name": "airliberty",
        "event_name": "translation_delivered",
        "nr_words": 30,
        "duration": 20,
    }

    # Check that the function returns a list
    assert isinstance(events, list)

    # 3 events in the file
    assert len(events) == 3

    assert events[0]["duration"] == sample_json["duration"]

    parsed_timestamp = datetime.strptime(
        sample_json["timestamp"], "%Y-%m-%d %H:%M:%S.%f"
    )
    # confirm the read and parsed correctly
    assert events[0]["timestamp"] == parsed_timestamp


def test_parse_event():

    # sample json, with the first event in the file
    sample_json = {
        "timestamp": "2018-12-26 18:11:08.509654",
        "translation_id": "5aa5b2f39f7254a75aa5",
        "source_language": "en",
        "target_language": "fr",
        "client_name": "airliberty",
        "event_name": "translation_delivered",
        "nr_words": 30,
        "duration": 20,
    }

    event = parse_event(sample_json)

    assert isinstance(event["timestamp"], datetime)
    assert event["duration"] == 20


def test_read_event_json():
    test_file_path = Path("./tests/files/events.json")

    # Call the function with the test file
    events = read_event(test_file_path)

    # assert events
    assert_event(events)


def test_read_event_jsonl():
    test_file_path = Path("./tests/files/events.jsonl")

    events = read_event(test_file_path)

    assert_event(events)
