# Python Programming Assignment - 13
# Solution for Question 3


def GetPerfectNumber(Val):
    Sum = 0
    for i in range(1, Val):
        if Val % i == 0:
            Sum += i
    return Sum == Val


def main():
    No = int(input("Enter The Number :"))
    Ret = GetPerfectNumber(No)
    print("Perfect Number is : ", Ret)

    return Ret


if __name__ == "__main__":
    main()
