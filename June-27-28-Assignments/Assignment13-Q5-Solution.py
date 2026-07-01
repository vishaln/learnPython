# Python Programming Assignment - 13
# Solution for Question 5

def DisplayGrades(Val):
    if Val >= 75:
        return "Distinction"
    elif Val >= 60:
        return "First Class"
    elif Val >= 50:
        return "Second Class"
    elif Val <= 40:
        return "Fail"


def main():
    Marks = int(input("Enter The Number :"))
    Ret = DisplayGrades(Marks)
    print("Student Grades is : ", Ret)

    return Ret


if __name__ == "__main__":
    main()
