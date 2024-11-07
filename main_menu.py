# Nano_appstore_menu/hoofdmenu
# Ahamd
from Nano_raadspel import raad_het_nummer
from tictactoe import tic_tac_toe
from galgje import galgje

def hoofdmenu():
    while True:
        print("\nWelkom bij GameWorld!")
        print("1: Raad het Nummer")
        print("2: Tic Tac Toe")
        print("3: Galgje")
        print("4: Afsluiten")

        keuze = input("Kies een optie: ")

        if keuze == '1':
            raad_het_nummer()
        elif keuze == '2':
            tic_tac_toe()
        elif keuze == '3':
            galgje()
        elif keuze == '4':
            print("Bedankt voor het spelen! Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    hoofdmenu()
#