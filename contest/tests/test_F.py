import pytest
from testing import parse_tests, get_output, is_equal, DEFAULT_MAX_TIME
import F


@pytest.mark.timeout(DEFAULT_MAX_TIME)
@pytest.mark.parametrize(("inp", "expected"), parse_tests(F.__doc__))
def test_submission(inp, expected):
    result = get_output(inp, F.main)
    assert is_equal(result, expected)
