# Python Programming Assignment - 12
# Solution for Question 2


def GetFactors(Val):
    for i in range(1, Val + 1):
        if Val % i == 0:
            print(i)


def main():
    No = int(input("Enter Number : "))
    Ret = GetFactors(No)

    return Ret


if __name__ == "__main__":
    main()
