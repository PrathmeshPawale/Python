# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# all odd numbers till that number.
# ---------------------------------------------------------

def DisplayOdd(number):
    for Value in range(1, number + 1, 2):
        print(Value, end = " ")

def main():
    number = int(input("Enter a number : "))

    DisplayOdd(number)

if __name__ == "__main__":
    main()