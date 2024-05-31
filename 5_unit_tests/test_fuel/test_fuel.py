from fuel import convert
from fuel import gauge
import pytest

def main():
    test_correct()
    test_0()
    test_value()

def test_correct():
    assert convert('1/2') == 50 and gauge(50) == '50%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('100/100') == 100 and gauge(100) == 'F'

def test_0():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('a/b')


if __name__ == "__main__":
    main()
