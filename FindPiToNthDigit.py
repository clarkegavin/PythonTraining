import math


def getUserInput():
    nthDigit = input("Enter Nth digit to display Pi to: ")
    return nthDigit


def checkNthValidity(nthDigit):
    if int(nthDigit) >=0 and int(nthDigit) <=10:
        return True
    else:
        print("Error: number is outside acceptable range: 0 - 10")
        return False


def main():
    nthDigit = getUserInput()
    if checkNthValidity(nthDigit):
        print(round(math.pi, int(nthDigit)))


main()
