import io
import sys
from contextlib import redirect_stdout

DEFAULT_MAX_TIME = 2


def parse_tests(tests_string: str | None):
    """
    Tests must be in the following format:
    ```
    Input
    ===
    Output

    ...

    Input
    ===
    Output
    ```
    """
    if not tests_string:
        return []
    tests = []
    for block in tests_string.strip().split("\n\n"):
        if "===" in block:
            input_, expected = block.split("===")
            tests.append((input_.strip(), expected.strip()))
    return tests


def get_output(input_, main):
    sys.stdin = io.StringIO(input_.strip())
    f = io.StringIO()
    with redirect_stdout(f):
        main()
    sys.stdin = sys.__stdin__
    return f.getvalue().strip()


def is_equal(result: str, expected: str, tol: float = 1e-9):
    """
    Compare outputs numerically if possible, otherwise fall back to string comparison.
    
    Supports single numbers or whitespace-separated lists of numbers.

    `*` is a wildcard, used for when the problem answer is not to be compared.
    """
    try:
        a_vals = [float(x) for x in result.split()]
        e_vals = [float(x) for x in expected.split()]
        if len(a_vals) != len(e_vals):
            return False
        return all(abs(a - e) <= tol for a, e in zip(a_vals, e_vals))
    except ValueError:
        pass
    
    if expected == "*":
        return True

    return result.strip() == expected.strip()
