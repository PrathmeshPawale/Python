# ---------------------------------------------------------
# Question:
# Write a program which contains one function named
# Add() which accepts two numbers and returns
# addition of those numbers.
# ---------------------------------------------------------
def Add(first_no, second_no):
    
    return first_no + second_no

def main():
    first_number = int(input("Enter first number : "))
    second_number = int(input("Enter second number : "))

    result = Add(first_number, second_number)

    print("Addition is :", result)

if __name__ == "__main__":
    main()