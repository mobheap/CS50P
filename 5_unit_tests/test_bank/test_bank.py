from bank import value

def main():
    test_0()
    test_20()
    test_100()


def test_0():
    assert value('hello gi ') == 0
    assert value('Hello') == 0

def test_20():
    assert value('hi') == 20
    assert value('haha') == 20

def test_100():
    assert value('salam') == 100
    assert value('wsg') == 100

if __name__ == '__main__':
    main()
