import io, sys
from tasks.task1 import solve

def run_io(input_data):
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    solve()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    return output

def test_case1():
    assert run_io("ХА\n") == "ХА ХА ХА ХА"

def test_case2():
    assert run_io("Кот\n") == "Кот Кот Кот Кот"
