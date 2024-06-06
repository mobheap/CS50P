import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1

def test_multiple_um():
    assert count("um, um, UM!") == 3
    assert count("um um um") == 3

def test_um_in_text():
    assert count("hello, um, world") == 1
    assert count("Um, excuse me, um, do you know where um is?") == 3

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_no_um():
    assert count("hello world") == 0
    assert count("this is a test") == 0

if __name__ == "__main__":
    pytest.main()