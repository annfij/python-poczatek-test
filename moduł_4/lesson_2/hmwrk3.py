# Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
# Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.

def run_example():
    colours = input("Jakie są Twoje ulubione kolory? ")

    if colours.lower().find("niebieski") != -1:
        print ("Jest niebieski!")
    else:
        print("Nie ma niebieskiego.")

if __name__ == '__main__':
    run_example()