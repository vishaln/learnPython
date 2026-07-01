# Python Programming Assignment - 13
# Solution for Question 4


def GetBinaryEquivalent(Val):
    return bin(Val)[2:]


def main():
    No = int(input("Enter The Number :"))
    Ret = GetBinaryEquivalent(No)
    print("Binary Equivalent is : ", Ret)

    return Ret


if __name__ == "__main__":
    main()
