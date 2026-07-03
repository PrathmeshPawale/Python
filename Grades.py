# ---------------------------------------------------------
# Question:
# Write a program which accepts marks and displays grade.
# >= 75 : Distinction
# >= 60 : First Class
# >= 50 : Second Class
# < 50  : Fail
# ---------------------------------------------------------

def CalculateGrade(marks):
    if marks >= 75:
        return "Distinction"

    elif marks >= 60:
        return "First Class"

    elif marks >= 50:
        return "Second Class"

    else:
        return "Fail"

def main():
    marks = float(input("Enter marks : "))

    result = CalculateGrade(marks)

    print("Grade :", result)

if __name__ == "__main__":
    main()