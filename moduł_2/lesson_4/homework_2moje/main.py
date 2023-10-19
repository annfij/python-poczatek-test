# Napisz metodę obliczającą łączną cenę jabłek,
# dla konkretnego obiektu Apple oraz łączną cenę ziemniaków
# dla konkretnego obiektu Potato na podstawie przekazanej w argumencie informacji o liczbie kilogramów.

from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    big_apple = Apple(species_name="green", size="duże", price=3.49)
    small_apple = Apple(species_name="czerwone", size="małe", price=2.99)

    print(f"5kg dużych jabłek kosztuje: {big_apple.calculate_price(5):.2f} zł.")
    print(f"5kg małych jabłek kosztuje: {small_apple.calculate_price(5):.2f} zł.")

    mlode_ziemniaki = Potato(species_name="młode", size="małe", price=1.99)

    print(f"5kg młodych ziemniaków kosztuje: {mlode_ziemniaki.count_price(5):.2f} zł.")


if __name__ == '__main__':
    run_homework()
