from seasons import calculate_minutes, convert_to_words
from datetime import date

def main():
    test_calculate_minutes()
    test_convert_to_words()

def test_calculate_minutes():
    assert calculate_minutes(date(2000, 1, 1)) == round((date.today() - date(2000, 1, 1)).total_seconds() / 60)
    assert calculate_minutes(date(2020, 2, 29)) == round((date.today() - date(2020, 2, 29)).total_seconds() / 60)

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand six hundred"
    assert convert_to_words(1440) == "One thousand four hundred forty"
    assert convert_to_words(0) == "Zero"

if __name__ == "__main__":
    main()
