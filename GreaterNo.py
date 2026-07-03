# ---------------------------------------------------------
# Question:
# Write a program which contains one function ChkGreater() that 
# accepts two number and prints greatest number.
# ---------------------------------------------------------
def ChkGreater(No1 : int,No2 : int):
    if No1 > No2 :
        print(f"{No1} is greater")
    elif No2 > No1 :
        print(f"{No2} is greater")
    else:
        print("Both are equal")

def main():
    No1 = int(input("Enter 1st Number : "))
    No2 = int(input("Enter 2nd Number : "))
    ChkGreater(No1,No2)

if __name__ == "__main__":
    main()