import pytest
from working import convert

def test_valid_format_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:15 PM to 11:45 PM") == "22:15 to 23:45"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:30 AM to 2:20 PM") == "01:30 to 14:20"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_valid_format_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 PM to 2 PM") == "13:00 to 14:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 AM to 12 PM") == "01:00 to 12:00"
    assert convert("11 PM to 1 AM") == "23:00 to 01:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("0 AM to 12 PM")
    with pytest.raises(ValueError):
        convert("12 PM to 13 PM")
    with pytest.raises(ValueError):
        convert("12 PM to 12:60 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM to 1 PM")

if __name__ == "__main__":
    pytest.main()
