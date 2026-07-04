# ---------------------------------------------------------
# Question:
# Write a lambda function using filter() which accepts
# a list of numbers and returns a list of numbers
# divisible by both 3 and 5.
# ---------------------------------------------------------
CheckDivisible = lambda number: number % 3 == 0 and number % 5 == 0

def main():
    data = [10, 15, 18, 30, 45, 50, 60]

    result = list(filter(CheckDivisible, data))

    print("Original List :", data)
    print("Filtered List :", result)

if __name__ == "__main__":
    main()