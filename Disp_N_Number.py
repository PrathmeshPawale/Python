# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# that many numbers starting from 1.
# ---------------------------------------------------------

def DisplayNumbers(number):
    for value in range(1, number + 1):
        print(value, end=" ")

def main():
    number = int(input("Enter a number : "))

    DisplayNumbers(number)

if __name__ == "__main__":
    main()