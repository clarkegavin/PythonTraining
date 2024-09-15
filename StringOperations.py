def findCharacterInString(someString, position):
    print("In findCharacterInString")
    a = someString[position]
    b = someString[1:4]  # used instead of substr
    print(a)
    print(b)


def findSubstr(someString, find):
    if find in someString:
        print("'" + find + "' is in '" + someString + "'")
    else:
        print("'" + find + "' is not in '" + someString + "'")


def stringSlicer(someString, start, end):
    return someString[start:end]




def main():
    print("In main function")
    findCharacterInString("Some random text", 3)
    print("find substring")
    findSubstr("This is a random string", "random")
    print("string slicer")
    sliced = stringSlicer("Hello World", 0, 5)
    print(sliced)

    #strips whitespace from a string beginning or end
    a = " Hello World! "
    print(a.strip())

    #use f-strings to format strings
    age = 43
    name = "Gavin"
    txt = f"My name is {name}, I am {age}"
    print(txt)
    salary = 1000000
    txt = f"My salary will soon be €{salary:,.2f}"
    print(txt)

    txt = "some RANDOM text to perform operations on "
    print(txt)
    print(txt.capitalize())
    print(txt.lower())
    print(txt.casefold())
    print(txt.center(20))
    print(txt.endswith("on "))
    x = txt.partition("text")
    print(x)
    x = txt.rpartition("text")
    print(x)
    print(txt.title())

    #bools
    a = "Hello"
    b = 15
    print(bool(a))
    print(bool(b))

    a = 5
    b = 2
    print(a**b)

main()
