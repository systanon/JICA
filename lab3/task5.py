from utils.utils import prettifyDict


def rectangleCalculator(a, b):
    a = float(a)
    b = float(b)
    return {"area": a * b, "circuit": 2 * (a + b)}


prettifyDict(rectangleCalculator(input("Enter side a: "), input("Enter side b: ")))
