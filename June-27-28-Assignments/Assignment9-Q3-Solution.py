# Python Programming Assignment - 9
# Solution for Question 3

GetSquare = lambda val: val * val

# def GetSquare(Val):
#    Square = Val * Val
#    return Square      

    
def main():
    No = int(input("Enter Number : "))
    Ret = GetSquare(No)
    print("Square of Given Number is : ", Ret)
    return Ret    

if __name__ == "__main__":
    main()