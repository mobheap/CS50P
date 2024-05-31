vowels = ["a","e","i","o","u"]
sentence = input("Input: ")
print("Output: ", end="")
for letter in sentence:
    if letter.lower() not in vowels:
        print(letter, end="")
print()