import pytest
from tests.utils import parse_tests, get_output
import E


@pytest.mark.parametrize(("input_", "expected"), parse_tests(E.__doc__))
def test_all(input_, expected):
    assert get_output(input_, E.main) == expected
