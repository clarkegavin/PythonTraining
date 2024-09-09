def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    choice = input("Do you want to compare based on ASCII (enter 1) or length (enter 2)")

    if choice == "1":
        first = string1>string2
        second = string1<string2
    elif choice == "2":
        first = len(string1) >len(string2)
        second = len(string1) <len(string2)

    if first:
        print ("First string is longer")
    elif second:
        print("Second string is longer")
    else:
        print("They are equal")


main()


