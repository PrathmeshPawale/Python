# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts one number
# and returns True if number is odd otherwise False.
# ---------------------------------------------------------

CheckOdd = lambda number : number % 2 != 0

def main():
    number = int(input("Enter a number : "))

    result = CheckOdd(number)

    if result:
        print(f"{number} is odd")
    else:
        print(f"{number} is even")

if __name__ == "__main__":
    main()