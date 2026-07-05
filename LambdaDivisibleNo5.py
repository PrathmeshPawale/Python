# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts one number
# and returns True if it is divisible by 5.
# ---------------------------------------------------------
CheckDivisible = lambda number: number % 5 == 0

def main():
    number = int(input("Enter a number : "))

    result = CheckDivisible(number)

    print(result)

if __name__ == "__main__":
    main()