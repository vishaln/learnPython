# Python Programming Assignment - 10
# Solution for Question 5

CheckOdd = lambda No: (No % 2 != 0)


def GetOddNumbers(Val):
    OddNumbers = []
    for i in range(1, Val + 1):
        if CheckOdd(i):
            OddNumbers.append(i)
    return OddNumbers


def main():
    No = int(input("Enter Number : "))
    Ret = GetOddNumbers(No)
    print("Odd numbers up to", No, "are : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
