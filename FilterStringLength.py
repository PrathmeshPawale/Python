# ---------------------------------------------------------
# Question:
# Write a lambda function using filter() which accepts
# a list of strings and returns a list of strings
# having length greater than 5.
# ---------------------------------------------------------
CheckLength = lambda word: len(word) > 5

def main():
    data = ["Python", "C", "Java", "Marvellous", "PPA", "Developer"]

    result = list(filter(CheckLength, data))

    print("Original List :", data)
    print("Filtered List :", result)

if __name__ == "__main__":
    main()