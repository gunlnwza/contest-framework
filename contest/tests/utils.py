import io
import sys
from contextlib import redirect_stdout

MAX_TIME = 2


def parse_tests(tests_string: str | None):
    """
    Tests must be in the following format:
    ```
    Input
    ===
    Output

    Input
    ===
    Output
    
    ...
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
