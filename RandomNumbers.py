import random

#a = random.random()
#print(a)
#print(random.random())

#random() provides a random number between 0 and 1

#rolling dice
print(1 + int(6 * random.random()))

letter = 'abcdefjhijklmnopqrstuvwxyz'
print(random.choice(letter))

fruits = ["Apple", "Orange", "Banana", "Kiwi", "Grape"]
print(random.choice(fruits))

#fixed random numbers
random.seed(37)
print(random.random())
print(random.random())
print(random.random())

