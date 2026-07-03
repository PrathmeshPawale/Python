# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# prints the square of that number.
# ---------------------------------------------------------
def SquareX(Number : int):
    return Number * Number
def main():
    No = int(input("Enter a number : "))
    Result = SquareX(No)
    print("Square of number is : ", Result)
if __name__ == "__main__":
    main()