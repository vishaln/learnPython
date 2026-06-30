# Python Programming Assignment - 9
# Solution for Question 5

Division = lambda val: val % 3 == 0 and val % 5 == 0


# def Division(Val):
#     if Val % 3 == 0 and Val % 5 == 0:
#         return True
#     else:
#         return False


def main():
    No = int(input("Enter Number : "))
    Ret = Division(No)
    print("Given Number is divisible by 3 and 5 : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
