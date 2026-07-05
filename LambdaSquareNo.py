# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts one number
# and returns square of that number.
# ---------------------------------------------------------

Square = lambda number : number * number

def main():
    number = int(input("Enter a number : "))

    result = Square(number) 

    print("Square of a number is : ", result)

if __name__ == "__main__":
    main()