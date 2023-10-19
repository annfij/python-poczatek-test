#  Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać formatowanie z procentem


def run_example():
    name = input("Jak masz na imię? ")
    last_name = input("Jak masz na nazwisko? ")
    name = name.lstrip()
    last_name = last_name.lstrip()

    print("You are %(name)s %(last_name)s, nice to meet you!" %{"name": name, "last_name": last_name})



if __name__ == '__main__':
    run_example()