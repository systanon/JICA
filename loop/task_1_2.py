COUNT = int(input("Input number: "))
i = 0
while i <= COUNT:
    if COUNT < 0 and COUNT > 100:
        print("Count must from 0 to 99")
        break
    i += 1
    print(i)

