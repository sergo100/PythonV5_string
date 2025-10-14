import io, sys
from tasks.task3 import solve

def run_io(input_data):
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    solve()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    return output

def test_case1():
    assert run_io("Один\nДва\n") == "ДваОдин"

def test_case2():
    assert run_io("12345\n67890\n") == "6789012345"

def test_case3():
    assert run_io("Как дела?\nХорошо!\n") == "Хорошо!Как дела?"
