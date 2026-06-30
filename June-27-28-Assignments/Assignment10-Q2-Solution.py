# Python Programming Assignment - 10
# Solution for Question 2

def SumOfNaturalNumbers(Val):
    Sum = 0
    for i in range(1, Val + 1):
        Sum += i
        print(Sum, i)

    return Sum


def main():
    No = int(input("Enter Number : "))
    Ret = SumOfNaturalNumbers(No)
    print("Sum of first", No, "natural numbers is : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
