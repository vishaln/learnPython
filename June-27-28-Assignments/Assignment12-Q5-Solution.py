# Python Programming Assignment - 12
# Solution for Question 5


def PrintNumbers(No):
    Arr = list()
    for i in range(No, 0, -1):
        Arr.append(i)
    return ", ".join(str(num) for num in Arr)


def main():
    No = int(input("Enter First Number  : "))
    Ret = PrintNumbers(No)
    print("Show Numbers till the number : ", Ret)
    return Ret


if __name__ == "__main__":
    main()
