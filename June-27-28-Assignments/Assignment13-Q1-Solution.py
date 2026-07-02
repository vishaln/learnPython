# Python Programming Assignment - 13
# Solution for Question 1

# GetRectangleArea = lambda Length, Width: Length * Width


def GetRectangleArea(Length, Width):
    Area = Length * Width
    return Area


def main():
    Length = int(input("Enter Length of the Rectangle :"))
    Width = int(input("Enter Width of the Rectangle :"))
    Ret = GetRectangleArea(Length, Width)
    print("Area of Rectangle is : ", Ret)

    return Ret


if __name__ == "__main__":
    main()
