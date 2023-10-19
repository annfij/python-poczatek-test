# Zabezpiecz listę pozycji w zamówieniu i łączną wartość zamówienia przed utratą spójności.
#
# W tym celu:
#
# Zamień listę pozycji w zamówieniu na zmienną prywatną.
# Zamień również metodę obliczającą łączny koszt zamówienia na prywatną.
# Dodaj metodę publiczną umożliwiającą dodanie nowego produktu do zamówienia (potrzebne będą informacje o produkcie i ilości).
# Pamiętaj wywołać ponownie przeliczenie łącznej wartości zamówienia.


from shop.order import generate_order
from shop.product import Product

def run_homework():
    first_order = generate_order()
    print(first_order)

    chocolate = Product(name="czekolada", category_name="słodycze", unit_price=5)
    first_order.add_product_to_order(chocolate, quantity=5)
    print(first_order)


if __name__ == '__main__':
    run_homework()