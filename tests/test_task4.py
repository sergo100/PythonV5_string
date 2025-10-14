import io, sys
from tasks.task4 import solve

def run_io(input_data):
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    solve()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    return output

def test_case1():
    assert run_io("Hello\n") == "HelloHelloHello"

def test_case2():
    assert run_io("Python is the best\n") == "Python is the bestPython is the bestPython is the best"
