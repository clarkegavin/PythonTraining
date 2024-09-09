# basic operations

def main():
    width = input("Enter the rectangles width: ")
    height = input("Enter the rectangles height: ")

    if width.isdecimal() and height.isdecimal():
        if width.isdecimal() and height.isdecimal() > 0:
            area = calc_area(width, height)
            perimeter = calc_perimeter(width, height)
            output(area, perimeter)
        else:
            print("Error: Width and height must be a positive integer")
    else:
        print("Error: Width and height must be a positive integer")


def output(area, perimeter):
    print("Area: " + str(area))
    print("Perimeter: " + str(perimeter))


def calc_area(width, height):
    area = int(width) * int(height)
    return area


def calc_perimeter(width, height):
    perimeter = 2 * (int(width) * int(height))
    return perimeter


main()
