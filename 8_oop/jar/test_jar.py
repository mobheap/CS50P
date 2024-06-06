import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0
    
    with pytest.raises(ValueError):
        jar = Jar(-1)
        
    with pytest.raises(ValueError):
        jar = Jar("a")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12
    
    with pytest.raises(ValueError):
        jar.deposit(1)  # Exceeds capacity

    with pytest.raises(ValueError):
        jar.deposit(-1)  # Invalid deposit
    
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    
    with pytest.raises(ValueError):
        jar.deposit(6)  # Exceeds capacity

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    
    with pytest.raises(ValueError):
        jar.withdraw(1)  # Not enough cookies to withdraw

    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Invalid withdrawal

    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)  # Not enough cookies to withdraw