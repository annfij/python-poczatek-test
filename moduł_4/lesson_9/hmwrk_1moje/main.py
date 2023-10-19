
# Stwórz odpowiednik klasy Apple jako named tuple.
# Stwórz instancję takiej krotki a następnie wypisz zawarte w niej dane na trzy sposoby:
# a) korzystając z nazw
# b) odwołując się do kolejnych indeksów
# c) za pomocą pętli.

from collections import namedtuple

Apple = namedtuple("Apple", ["species_name", "size", "price"])

def run_example():
    apple = Apple(species_name="czerwone", size="Big", price=3.49)

    print(apple.species_name, apple.size, apple.price)
    print(apple[0], apple[1], apple[2])

    for value in apple:
        print(value)

if __name__ == '__main__':
    run_example()