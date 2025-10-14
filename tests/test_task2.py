import io, sys
from tasks.task2 import solve

def run_io(input_data):
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    solve()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    return output

def test_case1():
    assert run_io("Один,два,три\n") == "12"

def test_case2():
    assert run_io("Python — это круто!\n") == "19"

def test_case3():
    assert run_io("123 456 789\n") == "11"
