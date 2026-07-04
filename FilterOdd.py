# ---------------------------------------------------------
# Question:
# Write a lambda function using filter() which accepts
# a list of numbers and returns a list of odd numbers.
# ---------------------------------------------------------
CheckOdd = lambda number: number % 2 != 0

def main():
    data = [10, 15, 20, 25, 30, 35]

    result = list(filter(CheckOdd, data))

    print("Original List :", data)
    print("Odd List      :", result)

if __name__ == "__main__":
    main()