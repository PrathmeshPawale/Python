# ---------------------------------------------------------
# Question:
# Write a program which accepts one character and checks
# whether it is vowel or consonant.
# ---------------------------------------------------------

def CheckVowel(character):
    
    return character.lower() in ('a', 'e', 'i', 'o', 'u')


def main():
    character = input("Enter a character : ")

    result = CheckVowel(character)

    if result:
        print("Vowel")
    else:
        print("Consonant")


if __name__ == "__main__":
    main()