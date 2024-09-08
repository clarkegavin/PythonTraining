# basic operations
def main():
    width = input("Enter the rectangles width: ")
    height = input("Enter the rectangles height: ")

    if width.isdecimal() and height.isdecimal():
        if width.isdecimal() and height.isdecimal() > 0:
            area = int(width) * int(height)
            perimeter = 2 * area
            output(area, perimeter)
        else:
            print("Width and height must be a positive integer")
    else:
        print("Width and height must be a positive integer")


def output(area, perimeter):
    print("Area: " + str(area))
    print("Perimeter: " + str(perimeter))


main()
