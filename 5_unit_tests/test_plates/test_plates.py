from plates import is_valid


def main():
    test_num_char()
    test_start_2_letters()
    test_num_middle()
    test_0_first()
    test_punctuation()


def test_num_char():
    assert is_valid('KKKK') == True
    assert is_valid('k') == False
    assert is_valid('kkkkkkkkkkk') == False

def test_start_2_letters():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False

def test_num_middle():
    assert is_valid('AA12') == True
    assert is_valid('AA1B') == False

def test_0_first():
    assert is_valid('AA10') == True
    assert is_valid('AA01') == False

def test_punctuation():
    assert is_valid('AA!123') == False
    assert is_valid('AA.123') == False
    assert is_valid('AA 123') == False

if __name__ == '__main__':
    main()
