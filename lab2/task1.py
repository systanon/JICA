products = sorted(("milk", "bread", "oil", "cheese", "apple"))

user_products = set(input("Enter 3 products: ").split())

available_product = set()
for product in products:
    for user_product in user_products:
        if product == user_product:
            available_product.add(user_product)

for unavailable_product in user_products - available_product:
    print(f"This product is not available: {unavailable_product}")
print("Sorted products", products)