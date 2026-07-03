# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and checks
# whether it is palindrome or not.
# ---------------------------------------------------------

def ReverseNumber(number):
    reverse = 0

    while number != 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = number // 10

    return reverse


def CheckPalindrome(number):

    return number == ReverseNumber(number)


def main():
    number = int(input("Enter a number : "))

    result = CheckPalindrome(number)

    if result:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()