# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# all even numbers till that number.
# ---------------------------------------------------------

def DisplayEven(number):
    for Value in range(2, number + 1, 2):
        print(Value, end = " ")

def main():
    number = int(input("Enter a number : "))

    DisplayEven(number)

if __name__ == "__main__":
    main()