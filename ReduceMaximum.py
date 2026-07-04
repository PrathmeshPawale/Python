# ---------------------------------------------------------
# Question:
# Write a lambda function using reduce() which accepts
# a list of numbers and returns the maximum element.
# ---------------------------------------------------------
from functools import reduce

Maximum = lambda first, second: first if first > second else second

def main():
    data = [10, 25, 70, 15, 40]

    result = reduce(Maximum, data)

    print("Original List :", data)
    print("Maximum       :", result)

if __name__ == "__main__":
    main()