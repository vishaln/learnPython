# Python Programming Assignment - 12
# Solution for Question 3

Addition = lambda No1, No2: No1 + No2
Substraction = lambda No1, No2: No1 - No2
Multiplication = lambda No1, No2: No1 * No2
Division = lambda No1, No2: No1 / No2


def main():
    No1 = int(input("Enter First Number  : "))
    No2 = int(input("Enter Second Number : "))

    Add = Addition(No1, No2)
    Sub = Substraction(No1, No2)
    Mult = Multiplication(No1, No2)
    Div = Division(No1, No2)

    print("Addition : ", Add)
    print("Substraction : ", Sub)
    print("Multiplication : ", Mult)
    print("Division : ", Div)


if __name__ == "__main__":
    main()
