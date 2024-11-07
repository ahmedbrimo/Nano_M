

# Nano_appstore_raadhetnummer/raadhetnummer.py

import random

def raad_het_nummer():
    print("Welkom bij Raad het Nummer!")

    max_num = int(input("Wat is het maximale getal waaruit geraden kan worden? "))
    attempts = int(input("Hoeveel pogingen wil je hebben om het getal te raden? "))

    geheim_nummer = random.randint(1, max_num)

    for poging in range(1, attempts + 1):
        gok = int(input(f"Poging {poging}: Raad het getal: "))

        if gok < geheim_nummer:
            print("Te laag!")
        elif gok > geheim_nummer:
            print("Te hoog!")
        else:
            print(f"Gefeliciteerd! Je hebt het juiste getal {geheim_nummer} geraden in {poging} pogingen.")
            break
    else:
        print(f"Helaas! Je hebt het juiste getal niet geraden. Het juiste getal was {geheim_nummer}.")
# dit is mijn raadspel om te pushen
