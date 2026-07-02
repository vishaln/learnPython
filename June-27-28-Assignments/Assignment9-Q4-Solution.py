# Python Programming Assignment - 9
# Solution for Question 4

# GetCubeNumber = lambda val: val * val * val

def GetCubeNumber(Val):
   Cube = Val * Val * Val
   return Cube      

    
def main():
    No = int(input("Enter Number : "))
    Ret = GetCubeNumber(No)
    print("Cube of Given Number is : ", Ret)
    return Ret    

if __name__ == "__main__":
    main()