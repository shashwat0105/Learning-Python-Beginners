import random

print("This is a dice simulator")
x = "y"

while x =="y":
    num = random.randint(1, 6) # generating random integers between 1 & 6
    if num == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        ("----------")

    if num == 2:
        print("----------")
        print("|        |")
        print("|  0  0  |")
        print("|        |")
        print("----------")

    if num == 3:
        print("----------")
        print("|    0   |")
        print("|        |")
        print("|  0   0 |")
        print("----------")

    if num == 4:
        print("----------")
        print("|  0   0 |")
        print("|        |")
        print("|  0   0 |")
        print("----------")

    if num == 5:
        print("----------")
        print("|  0   0 |")
        print("|    0   |")
        print("|  0   0 |")
        print("----------")

    if num == 6:
        print("----------")
        print("|  0   0 |")
        print("|  0   0 |")
        print("|  0   0 |")
        print("----------")

    x = input("Press y to roll again")
