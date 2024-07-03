import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

number = random.randint(0,level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too Large!")
    except:
        pass