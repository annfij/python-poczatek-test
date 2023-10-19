# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.

def print_call_str(**kwargs):
    call_str = "print_call_str("
    for argument_name, argument_value in kwargs.items():
        call_str += f"{argument_name}={argument_value}, "
    call_str += ")"
    print(call_str)


def run_example():
    english_polish ={
        "name" : "imię",
        "blue" : "niebieski",
        "gold" : "złoty",
    }

    polish_english ={
        "coś" : "something",
        "książka" : "book",
        "jabłko" : "apple",

    }

    all_words = {**english_polish, **polish_english}
    print(all_words)

    print_call_str(**all_words)

if __name__ == '__main__':
    run_example()