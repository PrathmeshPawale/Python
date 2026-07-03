# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and prints
# sum of first N natural numbers.
# ---------------------------------------------------------
def SumNatural(Number):
    Sum = 0
    for Value in range(1,Number + 1):
        Sum = Sum + Value
    
    return Sum


def main():
    number = int(input("Enter a number : "))

    result = SumNatural(number)

    print("Sum is :", result)


if __name__ == "__main__":
    main()