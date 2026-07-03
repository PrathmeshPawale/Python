# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and checks
# whether it is divisible by 3 and 5.
# ---------------------------------------------------------
def ChkDivisible(Number : int):
    return Number % 3 == 0 and Number % 5 == 0
def main():
    No = int(input("Enter a Number : "))
    Result = ChkDivisible(No)
    if Result == True :
        print(f"{No} is Divible by 3 and 5")
    else:
        print(f"{No} is not Divible by 3 and 5")
if __name__ == "__main__":
    main()