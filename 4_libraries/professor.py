import random

def main():
    score = 0
    level = get_level()
    for _ in range(0,10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == z:
                    score += 1
                    break
                else:
                    print("EEE")
            except:
                print("EEE")
        else:
            print(f"{x} + {y} = {z}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        return x
    elif level == 2:
        x = random.randint(10,99)
        return x
    elif level == 3:
        x = random.randint(100,999)
        return x

if __name__ == "__main__":
    main()