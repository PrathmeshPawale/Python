# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# sum of digits.
# ---------------------------------------------------------

def SumDigits(number):
    Sum = 0
    while number != 0:
        digit = number % 10
        Sum = Sum + digit
        number = number // 10
    return Sum


def main():
    number = int(input("Enter a number : "))

    result = SumDigits(number)

    print("Sum of digits :", result)


if __name__ == "__main__":
    main()