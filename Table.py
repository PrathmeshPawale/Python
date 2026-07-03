# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# multiplication table of that number.
# ---------------------------------------------------------
def DisplayTable(No : int):
    for i in range(1,11):
        print(No * i,end = " ")
def main():
    number = int(input("Enter a number : "))

    DisplayTable(number)

if __name__ == "__main__":
    main()