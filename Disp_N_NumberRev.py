# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# that many numbers in reverse order.
# ---------------------------------------------------------

def DisplayReverse(number):
    for value in range(number, 0, -1):
        print(value, end=" ")

def main():
    number = int(input("Enter a number : "))

    DisplayReverse(number)

if __name__ == "__main__":
    main()