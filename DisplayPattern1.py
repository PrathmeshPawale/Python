# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and display below pattern 
# Input : 5
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    * 
# ---------------------------------------------------------
def DisplayPattern(rows):

    for _ in range(rows):
        for _ in range(rows):
            print("*", end="\t")
        print()

def main():
    rows = int(input("Enter number of rows : "))

    DisplayPattern(rows)

if __name__ == "__main__":
    main()