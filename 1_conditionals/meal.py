def main():
    time = input("What time is it? (24hr format: ##:##) ")
    x = convert(time)
    
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    hour, minute = time.split(":")
    minute2 = float(minute) / 60
    time2 = float(hour) + minute2
    return time2

if __name__ == "__main__":
    main()