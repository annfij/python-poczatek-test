
# Zastąp dotychczasową implementację polityk rabatowych wykorzystującą funkcje
# rozwiązaniem opartym o klasy, dziedziczenie i polimorfizm.
# Utwórz klasę DiscoutPolicy i zaimplementuj w niej metodę apply_discount przyjmującą wartość zamówienia
# i zwracającą kwotę pomniejszoną o rabat. W klasie DiscountPolicy metoda ta po prostu zwróci otrzymaną wartość
# (tak samo jak wcześniej robiła to funkcja default_policy.
# Następnie utwórz dwie klasy dziedziczące po DiscoutPolicy:
# - PercentageDiscount, która przyjmuje w konstruktorze wartość procentową rabatu jaki ma udzielić
#   i odpowiednio przelicza wartość w apply_discount
# - AbsoluteDiscount, która przyjmuje w konstruktorze wartość o którą zmniejsza zamówienie,
#   dbając przy tym by zwrócony wynik nie był poniżej zera.
# W skrypcie main utwórz kilka wariantów zamówienia z tymi samymi produktami ale innymi politykami rabatowymi.
# Pamiętaj żeby dostosować użycie polityki rabatowej wewnątrz klasy Order.


from shop import data_generator
from shop.discount_policy import PercentageDiscount, Absolute_Discount
from shop.order import Order

def run_homework():
    order_elements = data_generator.generate_order_elements()
    seven_percent_discount = PercentageDiscount(discount_percentage=7)
    fifty_pln_discount = Absolute_Discount(discount_value=50)

    no_discount_order = Order(
        client_first_name = "Anna",
        client_last_name = "X",
        order_elements = order_elements
    )

    order_with_percentage_discount = Order(
        client_first_name="Anna",
        client_last_name="X",
        order_elements = order_elements,
        discount_policy=seven_percent_discount,
    )

    order_with_pln_discount = Order(
        client_first_name="Anna",
        client_last_name="X",
        order_elements=order_elements,
        discount_policy=fifty_pln_discount,
    )

    print(no_discount_order)
    print(order_with_percentage_discount)
    print(order_with_pln_discount)

if __name__ == '__main__':
    run_homework()
