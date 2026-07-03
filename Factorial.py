# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# factorial of that number.
# ---------------------------------------------------------

def Factorial(number):
    fact = 1
    for Value in range(1, number + 1):
        fact = fact * Value
    return fact

def main():
    number = int(input("Enter a number : "))

    result = Factorial(number)

    print("Factorial is :", result)

if __name__ == "__main__":
    main()