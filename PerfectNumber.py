# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and checks
# whether it is a perfect number or not.
# ---------------------------------------------------------

def CheckPerfect(number):
    sum = 0

    for value in range(1, number):
        if number % value == 0:
            sum = sum + value

    return sum == number

def main():
    number = int(input("Enter a number : "))

    result = CheckPerfect(number)

    if result:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()