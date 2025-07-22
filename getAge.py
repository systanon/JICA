from datetime import datetime
current_year = datetime.now().year
birht = int(input("Input your birth year: "))

def getAge(birth_year, current_year):
    return current_year - birth_year

age = getAge(birht, current_year)
if age >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")

