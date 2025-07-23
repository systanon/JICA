tekst = sorted(input("Input text: ").split())


lizcnik = {}

for litera in tekst:
    print(litera)
    if litera.isalpha():
        if litera in lizcnik:
            lizcnik[litera] += 1
        else:
            lizcnik[litera] = 1

print(lizcnik)
