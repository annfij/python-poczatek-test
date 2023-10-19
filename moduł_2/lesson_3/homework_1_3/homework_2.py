# Napisz funkcję wypisującą produkt i zamówienie.
# Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class Order:

    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.price
        self.total_price = total_price

class Apple:

    def __init__(self, apple_name, apple_size, apple_price):
        self.apple_name = apple_name
        self.apple_size = apple_size
        self.apple_price = apple_price

class Potato:

    def __init__(self, potato_name, potato_size, potato_price):
        self.potato_name = potato_name
        self.potato_size = potato_size
        self.potato_price = potato_price


def print_product(product):
    print(f"Nazwa: {product.name} | Kategoria: {product.category} | Cena: {product.price}/szt")


def print_order(order):
    print("=" * 20)
    print(f"Zamówienie złożone przez: {order.first_name} {order.last_name}")
    print(f"O łącznej wartości: {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("=" * 20)
    print()


def run_homework():
    cookies = Product(name="Cookies", category="Food", price=4)
    empty_order = Order(first_name="Anna", last_name="X")
    order = Order(first_name="Anna", last_name="X", products=[cookies, cookies, cookies])
    print_order(empty_order)
    print_order(order)


if __name__ == '__main__':
    run_homework()