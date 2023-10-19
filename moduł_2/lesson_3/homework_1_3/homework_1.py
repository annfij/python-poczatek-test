# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
# Product: nazwa, nazwa kategorii, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta),
# łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg
# Utwórz kilka obiektów każdej klasy.

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

def run_homework():
    red_apple = Apple(apple_name="Czerwone", apple_size="średnie", apple_price=3)
    green_apple = Apple(apple_name="Zielone", apple_size="duże", apple_price=3.5)
    print(red_apple.apple_name, red_apple)
    print(green_apple.apple_name, green_apple)

    young_potato = Potato(potato_name="młode ziemniaki", potato_size="małe", potato_price=2)
    print(young_potato.potato_name, young_potato)

    cos = Product(name="coś", category="coś", price=1)
    print(cos.name, cos)

    empty_order = Order(first_name="Anna", last_name="x")
    order = Order(first_name="Anna", last_name="X", products=[cos])
    print(cos)
    print(empty_order)
    print(order)

if __name__ == '__main__':
    run_homework()






