
#Zaimplementuj metodę __repr__ dla klas Apple oraz Potato.

from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    big_apple = Apple(species_name="green", size="duże", price=3.49)
    small_apple = Apple(species_name="czerwone", size="małe", price=2.99)

    print(big_apple)
    print(small_apple)

    mlode_ziemniaki = Potato(species_name="młode", size="małe", price=1.99)

    print(mlode_ziemniaki)


if __name__ == '__main__':
    run_homework()
