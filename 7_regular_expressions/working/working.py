import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = re.compile(r'^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$')
    
    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid format")
    
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
    
    start_minute = start_minute if start_minute else "00"
    end_minute = end_minute if end_minute else "00"
    
    start_24_hour = to_24_hour_format(start_hour, start_minute, start_period)
    end_24_hour = to_24_hour_format(end_hour, end_minute, end_period)
    
    return f"{start_24_hour} to {end_24_hour}"

def to_24_hour_format(hour, minute, period):
    hour = int(hour)
    minute = int(minute)
    
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12
    
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()