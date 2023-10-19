# Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30 podzielne kolejno przez 3 oraz przez 5.
# To znaczy, że na pierwszej liście powinny znaleźć się liczby od 1 do 30 podzielne przez 3, a na drugiej liście liczby
# od 1 do 30 podzielne przez 5.
# Następnie, połącz obie listy w jedną i wypisz wynik.

def run_example():
    numbers = [number for number in range (31) if number % 3 == 0]
    numbers1 = [number for number in range (31) if number % 5 == 0]

    # print(numbers)
    # print(numbers1)
    all = numbers + numbers1
    print(all)


if __name__ =='__main__':
    run_example()