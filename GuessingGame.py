import random

def main():
    target_number = 1 + int(20*random.random())


    guessed_number = int(input("Guess the number between 1 and 20: "))

    if guessed_number == target_number:
        print("Correct!")
    elif guessed_number > target_number:
        print("go lower")
    elif guessed_number < target_number:
        print("go higher")
    elif guessed_number == "exit":
        exit(0)

    print("Target Number: " + str(target_number))


main()
