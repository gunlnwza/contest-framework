import pytest
from tests.utils import parse_tests, get_output
import F


@pytest.mark.parametrize(("input_", "expected"), parse_tests(F.__doc__))
def test_all(input_, expected):
    assert get_output(input_, F.main) == expected
