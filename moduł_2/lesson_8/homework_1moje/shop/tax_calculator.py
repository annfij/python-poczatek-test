
class TaxRates:

    FRUIT_AND_VEGGIES = 0.05
    FOOD = 0.08
    REST = 0.2

class TaxCalculator:
    @staticmethod
    def tax_for_order_element(order_element):
        product_category = order_element.product.category_name
        if product_category == "Owoce i warzywa":
            tax_rate = TaxRates.FRUIT_AND_VEGGIES
        elif product_category == "Jedzenie":
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.REST
        return tax_rate * order_element.calculate_price()