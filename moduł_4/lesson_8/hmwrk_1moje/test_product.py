
# - Napisz test sprawdzający poprawność wykonanej w poprzednim module metody magicznej __eq__ w klasie Product
# - czyli porównywania produktów.
# - Dla przypomnienia, dwa produkty są sobie równe, gdy mają taką samą nazwę, taką samą kategorię i taką samą cenę jednostkową.
# - Wykorzystaj tuple do przygotowania różnych zestawów parametrów danych do algorytmu testującego.

from shop.product import Product

def test_product():
    parameters = [
        ("Owoce", "Jedzenie", 3, "Owoce", "Jedzenie", 3, True),
        ("Owoce", "Jedzenie", 3, "Warzywa", "Jedzenie", 3, False),
        ("Owoce", "Jedzenie", 3, "Owoce", "Żelki", 3, False),
        ("Owoce", "Jedzenie", 3, "Owoce", "Jedzenie", 4, False)
    ]

    for params in parameters:
        name, category, price, other_name, other_category, other_price, expected_result = params

        result = Product(name, category, price) == Product(other_name, other_category, other_price)
        if result == expected_result:
            print("OK")
        else:
            print(f"Coś się nie zgadza. Dla {params} wynik równania: {result}, powinien być taki: {expected_result}.")

def run_test():
    test_product()

if __name__ == '__main__':
    run_test()