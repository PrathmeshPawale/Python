# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# prints the cube of that number.
# ---------------------------------------------------------
def CubeX(Number : int):
    return Number * Number * Number
def main():
    No = int(input("Enter a number : "))
    Result = CubeX(No)
    print("Square of number is : ", Result)
if __name__ == "__main__":
    main()