TICKETS_PRICES = {"normal": 30, "student": 20, "senior": 15, "free": 0}


age = int(input("Input your age: "))
student_input = input("Input your is Student(yes/no): ")
week_day = input("Input day of week: ")

USER_INFO = {
    "age": age,
    "isStudent": student_input == "yes",
    "isWednesday": week_day == "wednesday",
}

DISCOUNT = 5


def getDiscount(discount, isWednesday):
    if isWednesday:
        return discount
    else:
        return 0



def calculating_ticket(ticketsPrices, user_info, discount):
    if user_info["age"] < 4:
        return ticketsPrices["free"]
    if user_info["age"] >= 65:
        return ticketsPrices["senior"] - getDiscount(discount, user_info["isWednesday"])
    if user_info["isStudent"] and user_info["age"] <= 26:
        return ticketsPrices["student"] - getDiscount(discount, user_info["isWednesday"])
    else:
        return ticketsPrices["normal"] - getDiscount(discount, user_info["isWednesday"])


amount = calculating_ticket(TICKETS_PRICES, USER_INFO, DISCOUNT)

print(f"Total to pay: { amount }zł")
