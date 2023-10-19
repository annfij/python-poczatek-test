# Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko, “wyczyści je” z białych znaków na początku
# i końcu tekstu, a następnie wypisze jakieś zdanie z tymi danymi np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)

def run_example():
    name = input("Jak masz na imię? ")
    last_name = input("Jak masz na nazwisko? ")
    name = name.lstrip()
    last_name = last_name.lstrip()

    print(f"You are {name} {last_name}, nice to meet you!")



if __name__ == '__main__':
    run_example()