# ---------------------------------------------------------
# Question:
# Create one module named Arithmetic which contains
# Add(), Sub(), Mult() and Div().
# Imported Module : ArithmeticX
# ---------------------------------------------------------
import ArithmeticX

def main():

    first_no = int(input("Enter first number : "))
    second_no = int(input("Enter second number : "))

    print("Addition       :", ArithmeticX.Add(first_no, second_no))
    print("Subtraction    :", ArithmeticX.Sub(first_no, second_no))
    print("Multiplication :", ArithmeticX.Mult(first_no, second_no))
    print("Division       :", ArithmeticX.Div(first_no, second_no))

if __name__ == "__main__":
    main()