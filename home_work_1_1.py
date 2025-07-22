tickets_prices = {
"normal": 45,
"reduced": 35,
}

while True:
  try:
    AGE = int(input("Input your age: "))
    break
  except ValueError:
    print("Input only integer")

def calculating_ticket(tickets_prices, age): 
  if age < 4 or age >= 70:
    print("Free ticket")
  elif (age <= 26): 
    print('Ticket reduced', tickets_prices["reduced"])
  else:
    print('Normal ticket', tickets_prices["normal"])

def init():
  calculating_ticket(tickets_prices, AGE)

init()