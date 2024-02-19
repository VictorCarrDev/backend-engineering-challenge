from typer.testing import CliRunner

from unbabel_cli.main import app

"""
Integration test for the CLI
"""

runner = CliRunner()


def test_cli():

    expected_output = [
        "{'date': '2018-12-26 18:11:00', 'average_delivery_time': 0}",
        "{'date': '2018-12-26 18:12:00', 'average_delivery_time': 20.0}",
        "{'date': '2018-12-26 18:13:00', 'average_delivery_time': 20.0}",
        "{'date': '2018-12-26 18:14:00', 'average_delivery_time': 20.0}",
        "{'date': '2018-12-26 18:15:00', 'average_delivery_time': 20.0}",
        "{'date': '2018-12-26 18:16:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:17:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:18:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:19:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:20:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:21:00', 'average_delivery_time': 25.5}",
        "{'date': '2018-12-26 18:22:00', 'average_delivery_time': 31.0}",
        "{'date': '2018-12-26 18:23:00', 'average_delivery_time': 31.0}",
        "{'date': '2018-12-26 18:24:00', 'average_delivery_time': 42.5}",
    ]

    result = runner.invoke(app, ["--input-file", "./tests/files/events.json"])
    assert result.exit_code == 0

    for output in expected_output:
        assert output in result.stdout

    result = runner.invoke(app, ["./tests/files/events.json"])
    assert result.exit_code == 2

    result = runner.invoke(app, ["--input-file", "./tests/files/wrongFile.json"])
    print(result.stdout)
    assert result.exit_code == 2
    assert (
        "Invalid value for '--input-file': Path './tests/files/wrongFile.json'"
        in result.stdout
    )
