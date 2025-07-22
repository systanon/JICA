import random

USER_INT = int(input("Input number: "))

while True:
    random_number = random.randint(1, 10)
    print(random_number)
    if USER_INT > random_number:
        print("Za dyzo")
        continue
    if USER_INT < random_number:
        print("Za malo")
        continue
    if USER_INT == random_number:
        print("bingo")
        break