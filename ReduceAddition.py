# ---------------------------------------------------------
# Question:
# Write a lambda function using reduce() which accepts
# a list of numbers and returns the addition of all elements.
# ---------------------------------------------------------
from functools import reduce

Addition = lambda first, second: first + second

def main():
    data = [10, 20, 30, 40, 50]

    result = reduce(Addition, data)

    print("Original List :", data)
    print("Addition      :", result)

if __name__ == "__main__":
    main()