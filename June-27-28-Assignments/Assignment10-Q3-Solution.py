# Python Programming Assignment - 10
# Solution for Question 3

def GetFactorial(Val):
    Factorial = 1
    for i in range(1, Val + 1):
        Factorial *= i
        print(Factorial, i)

    return Factorial


def main():
    No = int(input("Enter Number : "))
    Ret = GetFactorial(No)
    print("Factorial of", No, "is : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
