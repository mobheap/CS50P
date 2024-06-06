from datetime import date, datetime
import inflect
import sys

def main():
    birthdate = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birth_date)
    print(f"{convert_to_words(minutes)} minutes")

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return round(delta.total_seconds() / 60)

def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")   # Converting the number to words without "and"
    words = words[0].upper() + words[1:]    # Capitalize first letter
    return words

if __name__ == "__main__":
    main()
