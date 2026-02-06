# menu.py - Menú principal per a jocs
# Aquest fitxer serveix com a punt d'entrada per a diferents jocs.
# Importem els jocs que volem incloure al menú.

import endevina
import rps
import penjat
import quiz
import web_app

def main() -> None:
    while True:
        print("\n🎮 Menú de jocs")
        print("1) Endevina el nombre")
        print("2) Pedra, paper o tisores")
        print("3) Mini Penjat")
        print('4) Quiz Python')
        print('5) Quina falta?')  # Missing number game
        print("0) Sortir")

        op = input("Tria una opció: ").strip()

        if op == "1":
            endevina.run()
        elif op == "2":
            rps.run()
        elif op == "3":
            penjat.run()
        elif op == "4":
            quiz.run()
        elif op == "5":
            web_app.render_missing_number_game()
        elif op == "0":
            print("👋 Adéu!")
            break
        else:
            print("⚠️ Opció no vàlida.")


if __name__ == "__main__":
    main()
