# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts two numbers
# and returns addition.
# ---------------------------------------------------------
Multiplication = lambda No1,No2 : No1 * No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    result = Multiplication(No1,No2)

    print("Multiplication is :", result)

if __name__ == "__main__":
    main()