import pytest
from tests.utils import parse_tests, get_output
import B


@pytest.mark.parametrize(("input_", "expected"), parse_tests(B.__doc__))
def test_all(input_, expected):
    assert get_output(input_, B.main) == expected
