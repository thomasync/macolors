from unittest.mock import MagicMock, call
from macolors.macolors import Macolors


# get_from_stdin should call input.format for each line
def test_get_from_stdin():
    macolors = Macolors()
    macolors.input.format = MagicMock()
    stdin = ["line1\n", "line2\n", "line3\n"]

    macolors.get_from_stdin(stdin)

    macolors.input.format.assert_has_calls(
        [call("line1\n", 1), call("line2\n", 2), call("line3\n", 3)]
    )
    assert macolors.input.format.call_count == 3


# get_from_command should create a subprocess and call input.format with the output
def test_get_from_command():
    macolors = Macolors()
    macolors.input.format = MagicMock()
    command = "echo 'test line'"
    macolors.get_from_command(command)

    macolors.input.format.assert_called_once_with("test line\n", 1)
