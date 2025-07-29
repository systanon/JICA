import json
from datetime import datetime
import os

filename = "history.json"

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, filename)


if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)



def getDate():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def saveHistory(history, user_name, user_input):
    if user_name in history:
        history[user_name][getDate()] = user_input
    else:
        history[user_name] = {getDate(): user_input}

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def readHistory():
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def showHistory(history, userName):
    if userName in history:
            print(history[userName])
    else:
            print("Empty history!!!")

def calculate(history, user_name):
    inputCalculate = input("Input calculate: ")
    try:
        res = eval(inputCalculate)
        saveHistory(history, user_name, inputCalculate)
        print(res)
    except:
        print("Error calculate !!!")
    

def main():
    user_name = input("Enter user name: ")
    print("Options: ")
    print("1 - show history: ")
    print("2 - show active user: ")
    print("3 - calculate: ")
    print("4 - show all history: ")
    print("0 - exit: ")

    while True:
        history = readHistory()
        option = input("Choose option: ")
        match option:
            case "1":
                showHistory(history, user_name)
            case "2":
                print(user_name)
            case "3":
                calculate(history,user_name)
            case "4":
                print(history)
            case "0":
                print("Program is closed bye bye")
                break
            case _:
                print("Option not in list")


if __name__ == "__main__":
    main()
