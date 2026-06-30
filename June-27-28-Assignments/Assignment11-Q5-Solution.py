# Python Programming Assignment - 11
# Solution for Question 5


def CheckPalindrome(Val):
    rev = 0
    temp = abs(Val)

    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    return rev == abs(Val)


def main():
    No = int(input("Enter Number : "))
    Ret = CheckPalindrome(No)
    if Ret == True:
        print("It is a Palindrome Number :", Ret)
    else:
        print("It is Not a Palindrome Number :", Ret)


if __name__ == "__main__":
    main()
