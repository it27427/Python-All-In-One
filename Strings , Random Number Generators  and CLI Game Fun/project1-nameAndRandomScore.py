import random

name1 = input("Enter first name: ")
name1RandomNumber = random.randint(0, 10)

name2 = input("Enter second name: ")
name2RandomNumber = random.randint(0, 10)

name3 = input("Enter third name: ")
name3RandomNumber = random.randint(0, 10)

print(name1, "Got a value of:", name1RandomNumber)
print(name2, "Got a value of:", name2RandomNumber)
print(name3, "Got a value of:", name3RandomNumber)
