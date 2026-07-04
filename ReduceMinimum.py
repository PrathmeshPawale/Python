# ---------------------------------------------------------
# Question:
# Write a lambda function using reduce() which accepts
# a list of numbers and returns the minimum element.
# ---------------------------------------------------------
from functools import reduce

Minimum = lambda first, second: first if first < second else second

def main():
    data = [10, 25, 70, 15, 40]

    result = reduce(Minimum, data)

    print("Original List :", data)
    print("Minimum       :", result)

if __name__ == "__main__":
    main()