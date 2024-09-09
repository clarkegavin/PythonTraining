def findCharacterInString(someString, position):
    print("In findCharacterInString")
    a = someString[position]
    b = someString[1:4] #used instead of substr
    print(a)
    print(b)

def main():
    print("In main function")
    findCharacterInString("Some random text", 3)


main()

