# Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi,
# pomijając pierwszy sport z listy.

def run_example():
    print("Jakie są Twoje ulubione sporty? ")

    fave_sports = []
    while True:
        sport = input("Podaj ulubiony sport lub zakończ 'X': ")
        if sport == "X":
            break
        fave_sports.append(sport)

    print(fave_sports[1::2])

if __name__ == '__main__':
    run_example()
