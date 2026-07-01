# Python Programming Assignment - 11
# Solution for Question 3


def GetSumOfDigits(Val):
    Sum = 0
    No = Val

    for digit in No:
        Sum = Sum + int(digit)

    return Sum


def main():
    No = input("Enter Number : ")
    Ret = GetSumOfDigits(No)
    print("Sum of Digits :", Ret)


if __name__ == "__main__":
    main()
