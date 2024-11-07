# Nano_appstore_tictactoe/tictactoe.py

def print_bord(bord):
    print(f"{bord[0]} | {bord[1]} | {bord[2]}")
    print("--+---+--")
    print(f"{bord[3]} | {bord[4]} | {bord[5]}")
    print("--+---+--")
    print(f"{bord[6]} | {bord[7]} | {bord[8]}")

def check_win(bord, speler):
    winnende_combinaties = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combi in winnende_combinaties:
        if bord[combi[0]] == bord[combi[1]] == bord[combi[2]] == speler:
            return True
    return False

def tic_tac_toe():
    bord = [" " for _ in range(9)]
    huidige_speler = "X"

    print("Welkom bij Tic Tac Toe!")

    for ronde in range(9):
        print_bord(bord)
        print(f"Speler {huidige_speler} is aan de beurt.")

        try:
            keuze = int(input("Kies een vakje (1-9): ")) - 1
            if bord[keuze] == " ":
                bord[keuze] = huidige_speler
            else:
                print("Dat vakje is al bezet. Probeer opnieuw.")
                continue
        except (ValueError, IndexError):
            print("Ongeldige invoer, kies een nummer tussen 1 en 9.")
            continue

        if check_win(bord, huidige_speler):
            print_bord(bord)
            print(f"Gefeliciteerd! Speler {huidige_speler} wint!")
            return

        huidige_speler = "O" if huidige_speler == "X" else "X"

    print_bord(bord)
    print("Het is gelijkspel!")
