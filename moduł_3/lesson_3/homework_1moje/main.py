
# Stwórz klasę reprezentującą produkt z terminem ważności (dziedziczącą po klasie Product).
# Rozszerz implementację bazową o dodatkowe pola: rok produkcji oraz liczbę lat ważności i metodę does_expire.
# Metoda ta przyjmuje jako argument aktualny rok oraz sprawdza czy od daty produkcji do podanego roku minęła liczba lat
# większa od tej podanej jako lata ważności.

from shop.product import Expiration


def run_homework():

    popcorn = Expiration(
        name="Popcorn",
        category_name="przekąski",
        unit_price=1.50,
        production_year = 2023,
        validation_years = 1
    )

    print(popcorn.does_expire(2000))
    print(popcorn.does_expire(2025))

if __name__ == '__main__':
    run_homework()
