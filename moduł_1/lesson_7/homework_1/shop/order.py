from shop.products import products, update_product_quantity

orders = [
    {
        "product": "chleb",
        "quantity": 3,
        "total_price": 12
    }
]

def create_new_order (product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Brak takiej ilości towaru.")
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_product_quantity (product_name, quantity)
    orders.append(new_order)
    return new_order