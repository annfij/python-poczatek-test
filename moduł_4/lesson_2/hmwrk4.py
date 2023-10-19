# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format.

def run_example():
    name = input("Jak masz na imię? ")
    last_name = input("Jak masz na nazwisko? ")
    name = name.lstrip()
    last_name = last_name.lstrip()

    print("You are {} {}, nice to meet you!".format(name, last_name))
    print("You are {name} {last_name}, nice to meet you!".format(name=name, last_name=last_name))


if __name__ == '__main__':
    run_example()