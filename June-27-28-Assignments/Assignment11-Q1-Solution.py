# Python Programming Assignment - 11
# Solution for Question 1

def GetPrimeNumbers(Val):
    if Val < 2:
        return False

    if Val == 2:
        return True

    if Val % 2 == 0:
        return False

    for i in range(3, int(Val**0.5) + 1, 2): 
        if Val % i == 0:
            return False

    return True


def main():
    No = int(input("Enter Number : "))
    Ret = GetPrimeNumbers(No)

    if Ret == True:
        print(No, "is a Prime Number")
    else:
        print(No, "is not a Prime Number")


if __name__ == "__main__":
    main()
