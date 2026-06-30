# Python Programming Assignment - 11
# Solution for Question 3

def GetSumOfDigits(Val):
    Sum = 0
    No = abs(Val)

    while No > 0:
        Sum = Sum + (No % 10)
        No = No // 10

    return Sum


def main():
    No = int(input("Enter Number : "))
    Ret = GetSumOfDigits(No)
    print("Sum of Digits :", Ret)


if __name__ == "__main__":
    main()
