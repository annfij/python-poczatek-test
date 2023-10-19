
# Klasy Apple oraz Potato są prostymi pojemnikami na dane.
# Zastąp ich dotychczasowe implementacje wariantem dataclass.

from shop.apple import Apple
from shop.potato import Potato
def run_homework():
    red_apple = Apple(species_name="czerwone", size="duży", price=4)
    yellow_apple = Apple(species_name="żółty", size="mały", price=3.49)
    print(red_apple.species_name, red_apple)
    print(yellow_apple.species_name, yellow_apple)

    potato = Potato(species_name="młody", size="mały", price=3)
    print(potato.species_name, potato)



if __name__ == '__main__':
    run_homework()
