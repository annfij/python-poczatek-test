# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.

# Wczytaj od użytkownika informacje o:

# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations, a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.

# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import calculations.value

def ask_initial_value(message):
    input_value = input(message)
    return int(input_value)

print("Kalkulator wartości z roczną kapitalizacją.")

initial_value = ask_initial_value("Jaką kwotę wpłaciłeś/łaś? ")
percentage = ask_initial_value("Jakie jest oprocentowanie lokaty? ")
years = ask_initial_value("Na ile lat jest lokata? ")

final_value = calculations.value.investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}.")
