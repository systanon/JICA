TICKETS_PRICES = {"normal": 30, "student": 20, "senior": 15, "free": 0}


age = int(input("Input your age: "))
student_input = input("Input your is Student(yes/no): ")
week_day = input("Input day of week: ")

USER_INFO = {
    "age": age,
    "isStudent": student_input == "yes",
    "isWednesday": week_day == "wednesday",
}

DISCONT = 5


def getDiscount(tickets_prices, discont, isWednesday):
    prices_copy = tickets_prices.copy()
    if not isWednesday:
        return prices_copy
    for key in prices_copy:
        if key == "free":
            continue
        prices_copy[key] -= discont
    return prices_copy


def calculating_ticket(ticketsPrices, user_info, discont):
    tickets_prices = getDiscount(ticketsPrices, discont, user_info["isWednesday"])
    if user_info["age"] < 4:
        return tickets_prices["free"]
    if user_info["age"] >= 65:
        return tickets_prices["senior"]
    if user_info["isStudent"] and user_info["age"] <= 26:
        return tickets_prices["student"]
    else:
        return tickets_prices["normal"]


amount = calculating_ticket(TICKETS_PRICES, USER_INFO, DISCONT)

print(f"Total to pay: { amount }zł")
