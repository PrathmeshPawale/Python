# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# prints its factors.
# ---------------------------------------------------------

def DisplayFactors(number):
    for value in range(1, number + 1):
        if number % value == 0:
            print(value, end=" ")


def main():
    number = int(input("Enter a number : "))

    DisplayFactors(number)


if __name__ == "__main__":
    main()