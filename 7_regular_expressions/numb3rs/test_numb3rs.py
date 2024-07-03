from numb3rs import validate

def main():
    test_valid_ip()
    test_invalid_ip_format()
    test_invalid_ip_range()
    test_edge_cases()
    

def test_valid_ip():
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid_ip_format():
    assert validate("192.168.0") == False
    assert validate("192.168.0.1.1") == False
    assert validate("192.168.0.abc") == False
    assert validate("192.168..1") == False
    assert validate("...") == False
    assert validate("256.256.256.256") == False
    assert validate("192.168.0.256") == False

def test_invalid_ip_range():
    assert validate("256.100.50.25") == False
    assert validate("192.300.0.1") == False
    assert validate("192.168.0.999") == False
    assert validate("999.999.999.999") == False

def test_edge_cases():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("01.02.03.04") == True

if __name__ == "__main__":
    main()