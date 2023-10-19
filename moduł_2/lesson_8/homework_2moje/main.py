
# Dodaj do programu obsługę polityki rabatowej.
# Zaimplementuj funkcje reprezentujące politykę rabatową i przekaż je do konstruktora zamówienia.
# Jeżeli polityka została przekazana to podczas liczenia łącznej kwoty zamówienia należy naliczyć rabat.
# Jeżeli nie - obliczamy łączną kwotę jak dotychczas.
# Zaimplementuj dwie polityki rabatowe:
#
# Dla stałych klientów: 5% rabatu na każdą pozycję
# Rabat świąteczny: rabat 20 PLN dla zamówień o łącznej kwocie powyżej 100 PLN

import random

from shop.order_element import OrderElement
from shop.product import Product
from shop.discount_policy import loyal_customer, holiday_season
from shop.order import Order

def generate_order_elements ():
    order_elements =[]
    for product_number in range(5):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))

    return order_elements

def run_homework():
    first_name = "Anna"
    last_name = "X"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    loyal_customer_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer)
    holiday_season_order = Order(first_name, last_name, order_elements, discount_policy=holiday_season)

    print(normal_order)
    print(loyal_customer_order)
    print(holiday_season_order)

if __name__ == '__main__':
    run_homework()
