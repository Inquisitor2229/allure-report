import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 4) == -4

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

#def test_failure():
#    assert calculator.add(2, 2) == 5  # Intentional failure

if __name__ == "__main__":
    pytest.main(["--html=report.html"])
