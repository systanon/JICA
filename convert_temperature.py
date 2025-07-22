input = int(input("input temperature: "))

def convert_temperature(temperature):
    return int(temperature * 9/5 + 32)



temp = convert_temperature(input)
print(f"{temp}F")