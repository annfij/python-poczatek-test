class Potato:

    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def calculate_price(self, quantity):
        return quantity * self.price

    def __repr__(self):
        return f"<Gatunek ziemniaków: {self.species_name}, rozmiar: {self.size}, cena: {self.price} zł/kg.>"