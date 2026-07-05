# ---------------------------------------------------------
# Question:
# Write a lambda function which accepts two numbers
# and returns minimum number.
# ---------------------------------------------------------
Maximum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    result = Maximum(No1,No2)

    print("Minimum number is :", result)

if __name__ == "__main__":
    main()