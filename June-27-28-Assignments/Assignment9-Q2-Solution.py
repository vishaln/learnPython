# Python Programming Assignment - 9
# Solution for Question 2

def ChkGreater(Val1, Val2):
    if Val1 > Val2:
        print(Val1, "is greater")
    elif Val2 > Val1:
        print(Val2, "is greater")
    else:
        print("Both values are equal")


def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    Ret = ChkGreater(No1, No2)
    return Ret

if __name__ == "__main__":
    main()
