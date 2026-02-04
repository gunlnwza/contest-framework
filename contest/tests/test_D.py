import pytest
from testing import parse_tests, get_output, is_equal, DEFAULT_MAX_TIME
import D


@pytest.mark.timeout(DEFAULT_MAX_TIME)
@pytest.mark.parametrize(("inp", "expected"), parse_tests(D.__doc__))
def test_submission(inp, expected):
    result = get_output(inp, D.main)
    assert is_equal(result, expected)
