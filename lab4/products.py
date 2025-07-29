import json
import os
import random
import time

FILE = "products.json"

current_dir = os.path.dirname(__file__)
FILE_PATH = os.path.join(current_dir, FILE)

print(FILE_PATH)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)


def loadProducts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Error load products")
    else:
        print("Products is loaded")


def getRandomId():
    return f"{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


def addProduct(products):
    name = input("Input product name: ")
    count = input("Input count of product: ")
    price = input("Input price of product: ")
    if isExist(products, name):
        print("Product already exist")
        return
    new_product = {"name": name, "count": count, "price": price, "id": getRandomId()}
    products.append(new_product)
    saveProducts(products)


def saveProducts(products):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
    except:
        print("Error save products")
    else:
        print("Product is saved")


def isExist(products, name):
    for product in products:
        if product["name"] == name:
            return True
    return False


def editProduct(products):
    productName = input("Input product name which need changing: ")
    newName = input("Input new name: ")
    newCount = input("Input new count: ")
    newPrice = input("Input new price: ")
    if isExist(products, newName):
        print("New name is already exist")
        return
    for product in products:
        if product["name"] == productName:
            if newName is not None and len(newName) > 0:
                product["name"] = newName
            if newCount is not None and len(newCount) > 0:
                product["count"] = newCount
            if newPrice is not None and len(newPrice) > 0:
                product["price"] = newPrice
            saveProducts(products)
            print("Product is updated")
            return
    print("Product is not find")
    return


def removeProduct(products):
    productName = input("Input product name: ")
    if not isExist(products, productName):
        print("Product does not exist")
        return
    filtered_products = [
        product for product in products if product["name"] != productName
    ]
    saveProducts(filtered_products)


def showProducts(products):
    if not products:
        print("Products list is empty")
        return
    for product in products:
        print(
            f"name: {product['name']}, count: {product['count']}, price: {product['price']} zł"
        )


def main():
    print("Options: ")
    print("1 - add Product: ")
    print("2 - show all products: ")
    print("3 - remove product: ")
    print("4 - edit product: ")
    print("0 - exit: ")
    while True:
        option = input("Choose option: ")
        products = loadProducts()
        match option:
            case "1":
                addProduct(products)
            case "2":
                showProducts(products)
            case "3":
                removeProduct(products)
            case "4":
                editProduct(products)
            case "0":
                print("Program is closed bye bye")
                break
            case _:
                print("Option not in list")


if __name__ == "__main__":
    main()
