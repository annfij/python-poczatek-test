
#Zaimplementuj metodę __len__ dla klasy Order, zwracając jako wynik liczbę pozycji w zamówieniu.

from shop.order import generate_order


def run_homework():
    first_order = generate_order()
    print(f"Liczba pozycji w zamówieniu wynosi: {len(first_order)}")
    second_order = generate_order()
    print(f"Liczba pozycji w zamówieniu wynosi: {len(second_order)}")


if __name__ == '__main__':
    run_homework()
