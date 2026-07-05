# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts one number
# and return cube of that number.
# ---------------------------------------------------------

Cube = lambda number : number * number * number

def main():
    number = int(input("Enter a number : "))

    result = Cube(number) 

    print("Square of a number is : ", result)

if __name__ == "__main__":
    main()