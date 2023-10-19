# Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001,
# tzn. zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.

import random
def run_example():
    number = random.randint(1,99999)
    identifier = str(number).zfill(5)

    print(f"Your id number is: {identifier}.")



if __name__ == '__main__':
    run_example()