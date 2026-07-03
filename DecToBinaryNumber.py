# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# prints binary equivalent.
# ---------------------------------------------------------

def DecimalToBinary(number):
    binary = ""

    while number != 0:
        digit = number % 2
        binary = str(digit) + binary
        number = number // 2

    return binary

def main():
    number = int(input("Enter a number : "))

    result = DecimalToBinary(number)

    print("Binary equivalent :", result)

if __name__ == "__main__":
    main()