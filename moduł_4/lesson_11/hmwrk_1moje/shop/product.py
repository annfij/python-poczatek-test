from dataclasses import dataclass
from enum import Enum

class ProductCategory(Enum):
    FOOD = "Jedzenie"
    OTHER = "Inne"
    DRINKS = "NAPOJE"

@dataclass
class Product:
    name: str
    category_name: str
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt"

@dataclass
class Expiration(Product):
    production_year: int
    validation_years: int


    def does_expire(self, current_year):
        return current_year > self.production_year + self.validation_years
