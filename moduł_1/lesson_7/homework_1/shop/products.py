products = {
    "chleb": {
        "quantity": 50,
        "price": 4.0
    },
    "jabłka": {
        "quantity": 100,
        "price": 3.49
    }
}

def update_product_quantity (product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity