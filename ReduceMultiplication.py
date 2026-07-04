# ---------------------------------------------------------
# Question:
# Write a lambda function using reduce() which accepts
# a list of numbers and returns the product of all elements.
# ---------------------------------------------------------
from functools import reduce

Multiplication = lambda first, second: first * second

def main():
    data = [1, 2, 3, 4, 5]

    result = reduce(Multiplication, data)

    print("Original List :", data)
    print("Product       :", result)

if __name__ == "__main__":
    main()