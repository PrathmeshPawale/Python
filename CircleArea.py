# ---------------------------------------------------------
# Question:
# Write a program which accepts radius of circle
# and prints area of circle.
# ---------------------------------------------------------

PI = 3.141592653589793

def CalculateArea(radius):
    return PI * radius * radius

def main():
    radius = float(input("Enter radius : "))

    result = CalculateArea(radius)

    print("Area of circle :", result)

if __name__ == "__main__":
    main()