# ---------------------------------------------------------
# Question:
# Write a program which accepts a name from the user
# and displays the length of that name.
# ---------------------------------------------------------
def StringLength(name):

    return len(name)

def main():
    name = input("Enter a name : ")

    result = StringLength(name)

    print("Length of name :", result)

if __name__ == "__main__":
    main()