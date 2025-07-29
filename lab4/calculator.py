import json
from datetime import datetime
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "history.json")


def isCloseCalculator(str):
    str = str.lower()
    return str == "exit" or str == "quit" or str == "q"


def isShowHistory(str):
    str = str.lower()
    return str == "history" or str == "h"


def calculateFun(str):
    return eval(str)


def isShowUserName(str):
    return str == "username"


def getDate():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def saveHistory(history, user_name):
    _history = readHistory()
    if len(history) == 0:
        return
    if user_name in _history:
        _history[user_name][getDate()] = history
    else:
        _history[user_name] = {getDate(): history}

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(_history, f, ensure_ascii=False, indent=2)


def readHistory():
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    user_name = input("Enter user name: ")
    user_history_list = []

    while True:
        user_input = input("Input values: ")

        if isCloseCalculator(user_input):
            print("Exit")
            saveHistory(user_history_list, user_name)
            break

        elif isShowHistory(user_input):
            his = readHistory()
            if user_name in his:
                print(his[user_name])
            else:
                print("Empty history!!!")

        elif isShowUserName(user_input):
            print(user_name)
        else:
            try:
                res = calculateFun(user_input)
                user_history_list.append(user_input)
                print(res)
            except:
                print("Error calculate !!!")
                continue


if __name__ == "__main__":
    main()
