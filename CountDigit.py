# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# count of digits in that number.
# ---------------------------------------------------------

def CountDigits(number):
    count = 0

    while number != 0:
        count = count + 1
        number = number // 10

    return count


def main():
    number = int(input("Enter a number : "))

    result = CountDigits(number)

    print("Number of digits :", result)


if __name__ == "__main__":
    main()