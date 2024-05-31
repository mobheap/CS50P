months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

while True:
    date = input("Date: ").lower().strip()
    try:
        month, day, year = date.capitalize().split("/")
        month = int(month)
        day = int(day)
        if 0 < day < 32 and 0 < month < 13:
            break
    except:
        try:
            month, day, year = date.capitalize().split(" ")
            day = day.replace(",","")
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
            month = int(month)
            day = int(day)
            if 0 < day < 32 and 0 < month < 13:
                break
        except:
            pass

print(f"{year}-{month:02d}-{day:02d}")