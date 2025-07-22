list = list(map(int, input("Input numbers: ").split()))

sum = 0
for i in list:
    sum += i

if sum / len(list) >= 3:
    print("Zaliczone")
else:
    print("Nie zaliczone")
