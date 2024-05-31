def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():                                #start with two letters
        return False
    if len(s) < 2 or len(s) > 6:                            # 1 < characters < 7
        return False
    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == "0" or s[i:].isdigit() == False:     #first num not 0 no num in middle
                return False
            else:
                break
    for i in s:                                             #no punctuation
        if i.isalnum() == False:
            return False
    else:
        return True

if __name__ == "__main__":
    main()
