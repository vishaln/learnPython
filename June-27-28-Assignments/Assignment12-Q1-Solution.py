# Python Programming Assignment - 12
# Solution for Question 1


def CheckCharacter(Val):
    charArray = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    if len(Val) == 1:
        if Val in charArray:
            print(Val, "is a Vowel")
        else:
            print(Val, "is a Consonant")
    else:
        print("Invalid Input, Add only one character")


def main():
    Char = input("Enter Number : ")
    Ret = CheckCharacter(Char)

    return Ret


if __name__ == "__main__":
    main()
