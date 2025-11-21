import pytest
from tests.utils import parse_tests, get_output, MAX_TIME
import B


@pytest.mark.timeout(MAX_TIME)
@pytest.mark.parametrize(("input_", "expected"), parse_tests(B.__doc__))
def test_all(input_, expected):
    assert get_output(input_, B.main) == expected
