# ---------------------------------------------------------
# Question:
# Write a program which displays
# first 10 even numbers on the screen.
# ---------------------------------------------------------
def Display():

    for value in range(2, 21, 2):
        print(value, end=" ")

def main():
    Display()

if __name__ == "__main__":
    main()