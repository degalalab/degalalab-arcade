# Joc del penjat
# És un joc d’endevinar una paraula secreta, lletra a lletra, amb un nombre limitat d’intents.
    # La paraula la tria l’ordinador
    # Tu proposes lletres
    # Si la lletra és a la paraula → 👍 bé
    # Si no hi és → ❌ perds un intent
    # Guanyes si completes tota la paraula
    # Perds si et quedes sense intents
import random

PENJAT = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =======""",
]


PARAULES = [
    "python", "variables", "funcio", "bucle", "llista",
    "diccionari", "programa", "terminal", "notebook", "debug"
]


def triar_paraula() -> str:
    return random.choice(PARAULES)


def mostrar_paraula(paraula: str, encertades: set[str]) -> str:
    # mostra l'estat: p _ t h o n
    return " ".join([c if c in encertades else "_" for c in paraula])


def llegir_lletra(usades: set[str]) -> str:
    while True:
        x = input("Lletra (o 'q' per sortir): ").strip().lower()

        if x == "q":
            return "q"

        if len(x) != 1 or not x.isalpha():
            print("⚠️ Escriu una sola lletra (a-z).")
            continue

        if x in usades:
            print("⚠️ Aquesta lletra ja l'has provada.")
            continue

        return x


def jugar_partida(intents_max: int = 7) -> None:
    paraula = triar_paraula()
    encertades: set[str] = set()
    usades: set[str] = set()
    intents = intents_max

    print("\n🔤 Mini Penjat!")
    # Debug opcional: descomenta per veure la paraula
    # print("[DEBUG] Paraula:", paraula)

    while True:
        # DIBUIX DEL PENJAT
        errors = intents_max - intents
        idx = min(errors, len(PENJAT) - 1)
        print(PENJAT[idx])

        # ESTAT DEL JOC
        estat = mostrar_paraula(paraula, encertades)
        print("\nParaula:", estat)
        print("Lletres usades:", " ".join(sorted(usades)) if usades else "(cap)")
        print("Intents restants:", intents)

        if "_" not in estat:
            print("🏆 Has guanyat! La paraula era:", paraula)
            return

        if intents == 0:
            print("💀 Has perdut! La paraula era:", paraula)
            return

        lletra = llegir_lletra(usades)
        if lletra == "q":
            print("👋 Surts de la partida.")
            return

        usades.add(lletra)

        if lletra in paraula:
            encertades.add(lletra)
            print("✅ Bona!")
        else:
            intents -= 1
            print("❌ No hi és.")


def run() -> None:
    while True:
        jugar_partida(intents_max=7)
        tornar = input("\nVols jugar una altra partida? (s/n): ").strip().lower()
        if tornar != "s":
            print("👋 Tornant al menú...")
            break


if __name__ == "__main__":
    run()
