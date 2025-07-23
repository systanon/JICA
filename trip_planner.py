DISTANCE = float(input("How many kilometers need drive: "))
FUEL_CONSUMPTION = float(input("Fuel consumption per 100 kilometers: "))
PETROL_PRICE = float(input("Petrol cost: "))
PASSENGER_COUNT = int(input("Passenger count: "))


def calculate_distance(distance, petrol_price, fuel_consumption, passenger_count):
    petrol_count = (fuel_consumption * distance) / 100

    amount = petrol_price * petrol_count

    return amount / passenger_count


total_price = calculate_distance(DISTANCE, PETROL_PRICE, FUEL_CONSUMPTION, PASSENGER_COUNT)

if DISTANCE > 500:
    print("It`s a long way need to rest!")
if isinstance(total_price, float) and total_price.is_integer():
    total_price = int(total_price)
else:
    total_price = round(total_price, 2)


print(f"Tolal price: {total_price}")