import pytest
from testing import parse_tests, get_output, is_equal, DEFAULT_MAX_TIME
import B


@pytest.mark.timeout(DEFAULT_MAX_TIME)
@pytest.mark.parametrize(("inp", "expected"), parse_tests(B.__doc__))
def test_submission(inp, expected):
    result = get_output(inp, B.main)
    assert is_equal(result, expected)
