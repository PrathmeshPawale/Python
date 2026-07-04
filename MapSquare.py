# ---------------------------------------------------------
# Question:
# Write a lambda function using map() which accepts a
# list of numbers and returns a list of squares.
# ---------------------------------------------------------

Square = lambda number: number * number

def main():
    data = [1,2,3,4,5]

    result = list(map(Square, data))

    print("Original List : ",data)
    print("Square List   : ",result)

if __name__ == "__main__":
    main()

