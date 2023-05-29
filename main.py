import time
from machine import Pin



przycisk = Pin(0, Pin.IN, Pin.PULL_UP)
dioda = Pin(2, Pin.OUT)


def manual():
    while True:
        if przycisk.value()==1:
            dioda.value(0)
        else:
            dioda.value(1)


def auto():
    dioda.value(0)
    print("Nastaw zakresy czasowe:")
    try: q = int(input("0.1 s, zakres: 0.1-1.2"))
    except:
        print("Zły zakres, poprawny zakres to 0.1-1.2")
        auto()
        return 0
    try: w = int(input("1s, zakres: 1-12"))
    except:
        print("Zły zakres, poprawny zakres to 1-12")
        auto()
        return 0
    try: e = int(input("10 s, zakres: 10-120"))
    except:
        print("Zły zakres, poprawny zakres to 10-120")
        auto()
        return 0
    try: r = int(input("1 m, zakres: 1-12"))
    except:
        print("Zły zakres, poprawny zakres to 1-12")
        auto()
        return 0
    try: t = int(input("10 m, zakres: 10-120"))
    except:
        print("Zły zakres, poprawny zakres to 10-120")
        auto()
        return 0
    try: y = int(input("2 h, zakres: 2-24"))
    except:
        print("Zły zakres, poprawny zakres to 2-24")
        auto()
        return 0
    try: u = int(input("1 d, zakres: 1-12"))
    except:
        print("Zły zakres, poprawny zakres to 1-12")
        auto()
        return 0
    try: i = int(input("2 m, zakres: 2-24"))
    except:
        print("Zły zakres, poprawny zakres to 2-24")
        auto()
        return 0
    print("Wczyśnij przycisk żeby zacząc odliczanie")
    time_to_sleep = q+w+e+60*r+60*t+360*y+86400*u+86400*i
    while True:
        if przycisk.value()==1:
            time.sleep(time_to_sleep)
            dioda.value(1)
    pass


while True:
    print("Przekaźnik czasowy PCR-515 Duo z opóźnionym załączeniem\n")
    print("Po podaniu napięcia zasilającego styk pozostaje w pozycji 11-10 i następuje odmierzanie nastawionego czasu pracy. ")
    print("Po odmierzeniu czasu następuje przełączenie styku w pozycję 11-12. ")
    print("Ponowna realizacja trybu pracy przekaźnika możliwa jest po odłączeniu napięcia zasilającego i ponownym jego załączeniu. \n")
    while True:
        print("1. MANUAL")
        print("2. AUTO")
        x = input("Wybierz opcję: ")
        if x == "1":
            manual()
            pass
        elif x == "2":
            auto()
            pass
        else:
            print("Nie ma takiej opcji, wpisz ponownie.\n")

