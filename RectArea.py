# ---------------------------------------------------------
# Question:
# Write a program which accepts length and width of a
# rectangle and prints its area.
# ---------------------------------------------------------

def CalculateArea(length, width):
    return length * width

def main():
    length = float(input("Enter length : "))
    width = float(input("Enter width : "))

    result = CalculateArea(length, width)

    print("Area of rectangle :", result)

if __name__ == "__main__":
    main()