def main():
    greeting = input("Greeting: ")
    val = value(greeting)

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
