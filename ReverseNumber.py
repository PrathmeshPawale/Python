# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# reverse of that number.
# ---------------------------------------------------------

def ReverseNumber(number):

    reverse = 0

    while number != 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = number // 10

    return reverse


def main():
    number = int(input("Enter a number : "))

    result = ReverseNumber(number)

    print("Reverse Number is :", result)


if __name__ == "__main__":
    main()