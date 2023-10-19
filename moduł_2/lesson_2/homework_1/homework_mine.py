# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ
# za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą
# nazwy produktów, a wartościami instancje klasy produkt.

class Product:
    pass

class Order:
    pass

class Apples:
    pass

class Potatoes:
    pass

if __name__ == '__main__':
    jablko_angielskie = Apples()
    jablko_polskie = Apples()
    jablko_hiszpanskie = Apples()

    ziemniak_wloski = Potatoes()
    ziemniak_francuski = Potatoes()

    print("jablko angielskie type:", type(jablko_angielskie))
    print("jablko polskie type:", type(jablko_polskie))
    print("jablko hiszpanskie type:", type(jablko_hiszpanskie))

    print("ziemniak wloski type:", type(ziemniak_wloski))
    print("ziemniak francuski type:", type(ziemniak_francuski))

    orders = []
    for _ in range(5):
        orders.append(Order())
    print(orders)

    products = {
        "banan": Product(),
        "chleb": Product(),
        "woda": Product(),
        "żelki": Product(),
    }
    print(products)



