# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts one number
# and returns True if number is even otherwise False.
# ---------------------------------------------------------

CheckEven = lambda number : number % 2 == 0

def main():
    number = int(input("Enter a number : "))

    result = CheckEven(number)

    if result:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if __name__ == "__main__":
    main()