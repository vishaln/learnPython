# Python Programming Assignment - 11
# Solution for Question 2

# GetCountOfDigits = lambda Val: len(str(abs(Val)))


def GetCountOfDigits(Val):
   Count = len(str(abs(Val)))
   return Count

def main():
    No = int(input("Enter Number : "))
    Ret = GetCountOfDigits(No)
    print("Count of Digits :", Ret)


if __name__ == "__main__":
    main()
