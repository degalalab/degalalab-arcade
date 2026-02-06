import random

OPCIONS = ["pedra", "paper", "tisores"]
GUANYA_A = {
    "pedra": "tisores",
    "paper": "pedra",
    "tisores": "paper",
}

DRECERES = {
    "p": "pedra",
    "pa": "paper",
    "t": "tisores",
}


def llegir_opcio() -> str:
    while True:
        x = input("Tria pedra/paper/tisores (p/pa/t) o 'q' per sortir: ").strip().lower()

        if x == "q":
            return "q"
        if x in DRECERES:
            return DRECERES[x]
        if x in OPCIONS:
            return x

        print("⚠️ Opció no vàlida.")


def resultat(jugador: str, ordinador: str) -> str:
    if jugador == ordinador:
        return "empat"
    if GUANYA_A[jugador] == ordinador:
        return "guanya"
    return "perd"


def jugar_partida_best_of_3() -> str:
    """Juga una partida (millor de 3). Retorna 'tu', 'pc' o 'sortir'."""
    vict_jugador = 0
    vict_pc = 0
    ronda = 1

    print("\n🏁 Comença la partida (millor de 3)!\n")

    while vict_jugador < 2 and vict_pc < 2:
        print(f"— Ronda {ronda} —")

        jugador = llegir_opcio()
        if jugador == "q":
            print("👋 Has sortit de la partida.")
            return "sortir"

        ordinador = random.choice(OPCIONS)
        print(f"Ordinador tria: {ordinador}")

        r = resultat(jugador, ordinador)

        if r == "guanya":
            vict_jugador += 1
            print("✅ Guanyes la ronda!")
        elif r == "perd":
            vict_pc += 1
            print("❌ Perds la ronda.")
        else:
            print("🤝 Empat.")

        print(f"Marcador → Tu {vict_jugador} - {vict_pc} PC\n")
        ronda += 1

    if vict_jugador > vict_pc:
        print("🏆 Has guanyat la partida!")
        return "tu"
    else:
        print("💻 L'ordinador guanya la partida.")
        return "pc"


def run() -> None:
    """Mode 'app': permet jugar múltiples partides i mostra estadístiques globals."""
    print("✂️ Pedra, Paper o Tisores")

    stats = {"partides": 0, "tu": 0, "pc": 0}

    while True:
        guanyador = jugar_partida_best_of_3()
        if guanyador == "sortir":
            break

        stats["partides"] += 1
        stats[guanyador] += 1

        print("\n📊 Estadístiques globals")
        print(f"  Partides jugades: {stats['partides']}")
        print(f"  Partides guanyades (tu): {stats['tu']}")
        print(f"  Partides guanyades (pc): {stats['pc']}\n")

        tornar = input("Vols jugar una altra partida? (s/n): ").strip().lower()
        if tornar != "s":
            break

    print("👋 Tornant al menú...")


if __name__ == "__main__":
    run()
