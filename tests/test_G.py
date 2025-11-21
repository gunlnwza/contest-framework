import pytest
from tests.utils import parse_tests, get_output
import G


@pytest.mark.parametrize(("input_", "expected"), parse_tests(G.__doc__))
def test_all(input_, expected):
    assert get_output(input_, G.main) == expected
