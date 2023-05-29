import time
from machine import Pin



przycisk = Pin(0, Pin.IN, Pin.PULL_UP)

def manual():
    while True:
        time.sleep(10)
        print("przycisk")
        print(przycisk.value())


def auto():
    pass


while True:
    #print("Przekaźnik czasowy PCR-515 Duo z opóźnionym załączeniem\n")
    #print("Po podaniu napięcia zasilającego styk pozostaje w pozycji 11-10 i następuje odmierzanie nastawionego czasu pracy. ")
    #print("Po odmierzeniu czasu następuje przełączenie styku w pozycję 11-12. ")
    #print("Ponowna realizacja trybu pracy przekaźnika możliwa jest po odłączeniu napięcia zasilającego i ponownym jego załączeniu. \n")
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

