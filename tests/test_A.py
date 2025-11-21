import pytest
from tests.utils import parse_tests, get_output
import A


@pytest.mark.parametrize(("input_", "expected"), parse_tests(A.__doc__))
def test_all(input_, expected):
    assert get_output(input_, A.main) == expected
