# ---------------------------------------------------------
# Question:
# Write a program which accepts N numbers from user
# and returns the addition of all prime numbers.
# Prime checking function should be present
# inside MarvellousNum module.
# ---------------------------------------------------------
import MarvellousNum

def ListPrime(data):
    sum = 0
    for no in data:
        if MarvellousNum.ChkPrime(no):
            sum = sum + no

    return sum

def main():

    size = int(input("Enter the no of elements : "))

    data = []

    print("Enter the elements : ")
    for _ in range(size):
        data.append(int(input()))

    result = ListPrime(data)

    print("Addition of prime numbers : ",result)

if __name__ == "__main__":
    main()