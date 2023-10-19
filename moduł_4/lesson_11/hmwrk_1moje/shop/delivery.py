import random

def products_delivery():
    available_products = [
        "rolls",
        "apples",
        "carrots",
        "yoghurt",
        "milk",
        "cheese",
        "ham",
        "chicken",
        "tooth paste",
        "crisps"
    ]

    return [available_products[random.randint(0,9)]for _ in range(5)]
