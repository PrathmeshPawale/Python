# ---------------------------------------------------------
# Question:
# Write a program which accepts two numbers and prints
# addition, subtraction, multiplication and division.
# ---------------------------------------------------------

def ArithmeticOperations(No1,No2):
    
    addition = No1 + No2
    subtraction = No1 - No2
    multiplication = No1 * No2
    division = No1 / No2

    return addition, subtraction, multiplication, division


def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    addition, subtraction, multiplication, division = ArithmeticOperations(No1 , No2)

    print("Addition       :", addition)
    print("Subtraction    :", subtraction)
    print("Multiplication :", multiplication)
    print("Division       :", division)


if __name__ == "__main__":
    main()