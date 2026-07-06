# ---------------------------------------------------------
# Question:
# Write a program which accepts one number from the
# user and returns the number of digits in that number.
# ---------------------------------------------------------
def CountDigits(number):
    
    count = 0

    while number != 0:
        count = count + 1
        number //= 10

    return count

def main():
    number = int(input("Enter a number : "))

    result = CountDigits(number)

    print("Number of digits :", result)

if __name__ == "__main__":
    main()