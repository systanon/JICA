tekst = input("Input text: ")

print(tekst.strip().strip(" ,.:;"))

lizcnik = {}

for litera in tekst:
    print(litera)
    if litera in lizcnik:
        lizcnik[litera] += 1
    else:
        lizcnik[litera] = 1

print(lizcnik)
