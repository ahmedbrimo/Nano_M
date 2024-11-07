import random
import os

def kies_random_woord():
    # Gebruik os.path om het absolute pad naar galgje_woorden.txt te verkrijgen
    huidige_map = os.path.dirname(__file__)  # Map waarin galgje.py staat
    bestand_pad = os.path.join(huidige_map, "galgje_woorden.txt")

    with open(bestand_pad, "r") as bestand:
        woorden = [woord.strip() for woord in bestand.readlines()]
    return random.choice(woorden)

def toon_status(woord, geraden_letters):
    return ' '.join([letter if letter in geraden_letters else '_' for letter in woord])

def galgje():
    print("Welkom bij Galgje!")
    naam = input("Wat is je naam? ")
    woord = kies_random_woord()
    geraden_letters = set()
    foute_pogingen = 0
    max_pogingen = 6

    while foute_pogingen < max_pogingen:
        print("\nHuidige status van het woord:", toon_status(woord, geraden_letters))
        print(f"Foute pogingen: {foute_pogingen}/{max_pogingen}")

        gok = input("Raad een letter: ").lower()

        if gok in geraden_letters:
            print("Je hebt deze letter al geraden.")
            continue

        geraden_letters.add(gok)

        if gok in woord:
            print(f"Goed gedaan! De letter '{gok}' zit in het woord.")
        else:
            print(f"Helaas, de letter '{gok}' zit niet in het woord.")
            foute_pogingen += 1

        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd {naam}, je hebt het woord '{woord}' geraden!")
            break
    else:
        print(f"Helaas, je hebt verloren! Het juiste woord was '{woord}'.")
