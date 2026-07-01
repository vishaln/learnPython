# Python Programming Assignment - 13
# Solution for Question 2

GetCircleArea = lambda Pi, Radius: Pi * Radius * Radius


# def GetCircleArea(Pi, Radius):
#    Area = Pi * Radius * Radius
#    return Area


def main():
    Pi = 3.14
    Radius = int(input("Enter Radius of the Circle :"))
    Ret = GetCircleArea(Pi, Radius)
    print("Area of Circle is : ", Ret)

    return Ret


if __name__ == "__main__":
    main()
