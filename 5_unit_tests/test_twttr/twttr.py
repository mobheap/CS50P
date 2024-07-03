def main():
    word = input("Input: ")
    print("Output: ", end="")
    shorten(word)

def shorten(word):
    vowels = ["a","e","i","o","u"]
    for letter in word:
        if letter.lower() not in vowels:
            print(letter, end="")
    print()

if __name__ == "__main__":
    main()