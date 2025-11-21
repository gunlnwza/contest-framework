import pytest
from tests.utils import parse_tests, get_output
import D


@pytest.mark.parametrize(("input_", "expected"), parse_tests(D.__doc__))
def test_all(input_, expected):
    assert get_output(input_, D.main) == expected
