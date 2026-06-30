# Python Programming Assignment - 10
# Solution for Question 1


def Multiplication(Val):
    Output = []
    for i in range(1, 11):
        Output.append(Val * i)
    return Output


def main():
    No = int(input("Enter Number : "))
    Ret = Multiplication(No)
    print("Multiplication Table of", No, "is : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
