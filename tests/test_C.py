import pytest
from tests.utils import parse_tests, get_output
import C


@pytest.mark.parametrize(("input_", "expected"), parse_tests(C.__doc__))
def test_all(input_, expected):
    assert get_output(input_, C.main) == expected
