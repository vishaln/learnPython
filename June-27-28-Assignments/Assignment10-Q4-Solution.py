# Python Programming Assignment - 10
# Solution for Question 4

CheckEven = lambda No: (No % 2 == 0)


def GetEvenNumbers(Val):
    EvenNumbers = []
    for i in range(1, Val + 1):
        if CheckEven(i):
            EvenNumbers.append(i)
    return EvenNumbers


def main():
    No = int(input("Enter Number : "))
    Ret = GetEvenNumbers(No)
    print("Even numbers up to", No, "are : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
