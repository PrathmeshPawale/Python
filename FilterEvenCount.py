# ---------------------------------------------------------
# Question:
# Write a lambda function using filter() which accepts
# a list of numbers and returns the count of even numbers.
# ---------------------------------------------------------
CheckEven = lambda number: number % 2 == 0

def main():
    data = [10, 15, 20, 25, 30, 35, 40]

    even_numbers = list(filter(CheckEven, data))

    print("Original List :", data)
    print("Count of Even Numbers :", len(even_numbers))

if __name__ == "__main__":
    main()