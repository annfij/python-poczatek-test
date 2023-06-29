# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta
# na podstawie otrzymanych długości przyprostokątnych.

# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:

# sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
# pow(x, y) - podnosi x do potęgi y

import math

def calculate_c (a ,b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

a = float(input("Jaka jest długość boku a? "))
b = float(input("Jaka jest długość boku b? "))

c = calculate_c(a, b)

print(f"Długość przeciwprostokątnej to: {c}.")
