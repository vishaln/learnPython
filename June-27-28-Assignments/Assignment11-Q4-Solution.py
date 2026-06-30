# Python Programming Assignment - 11
# Solution for Question 4

GetReverseNumber = lambda Val: int(str(str(Val)[::-1]))

# def GetReverseNumber(Val):
#    rev = int(str(str(Val)[::-1]))
#    return rev


def main():
    No = int(input("Enter Number : "))
    Ret = GetReverseNumber(No)
    print("Reverse Number :", Ret)


if __name__ == "__main__":
    main()
