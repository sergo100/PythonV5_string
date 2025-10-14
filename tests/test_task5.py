import io, sys
from tasks.task5 import solve

def run_io(input_data):
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    solve()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    return output

def test_case1():
    assert run_io("A B C\n") == "Код символа A равен 65\nКод символа B равен 66\nКод символа C равен 67"

def test_case2():
    assert run_io("q w e\n") == "Код символа q равен 113\nКод символа w равен 119\nКод символа e равен 101"

def test_case3():
    assert run_io("L o L\n") == "Код символа L равен 76\nКод символа o равен 111\nКод символа L равен 76"
