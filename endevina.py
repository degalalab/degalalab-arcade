# 1️⃣ Endevina el nombre 🎯
# En aquest joc, el programa genera un nombre aleatori entre 1 i 100, i tu has d'endevinar-lo. El programa et donarà pistes si el teu intent és massa alt o massa baix. Quan encertis, et dirà quants intents has necessitat. Bona sort!🍀

''' CODE ORIGINAL (sense funcions) '''
"""
=======================================
import random

secret = random.randint(1, 100)
intents = 0

while True:
    try:
        print("👉 Estic esperant que escriguis un número...")
        guess = int(input("Endevina el nombre (1-100): "))
    except ValueError:
        print("⚠️ Introdueix un nombre vàlid.")
        continue   # torna a començar el bucle

    intents += 1

    if guess < secret:
        print("És més gran")
    elif guess > secret:
        print("És més petit")
    else:
        print(f"Correcte! {intents} intents.")
        break
"""
# Refactoring amb funcions
'''
Anem a refactoritzar amb funcions. L’objectiu és que el joc quedi més net, més fàcil de mantenir i “professional”.

1) Idea: què separarem en funcions?

Llegir un enter de l’usuari (amb validació) → llegir_enter(...)
Jugar una partida → jugar_partida(...)
(Opcional) main per arrencar el programa

'''
import random


def llegir_enter(missatge: str) -> int:
    while True:
        valor = input(missatge).strip()
        try:
            return int(valor)
        except ValueError:
            print("⚠️ Introdueix un nombre enter vàlid.")


def llegir_si_no(missatge: str) -> bool:
    resposta = input(missatge).strip().lower()
    return resposta == "s"


def jugar_partida(min_n: int = 1, max_n: int = 100) -> int:
    secret = random.randint(min_n, max_n)
    intents = 0

    while True:
        guess = llegir_enter(f"Endevina el nombre ({min_n}-{max_n}): ")

        if not (min_n <= guess <= max_n):
            print(f"⚠️ Ha de ser un nombre entre {min_n} i {max_n}.")
            continue

        intents += 1

        if guess < secret:
            print("És més gran")
        elif guess > secret:
            print("És més petit")
        else:
            print(f"Correcte! {intents} intents.")
            return intents


def run() -> None:
    print("🎯 Endevina el nombre!")

    partides = 0
    intents_totals = 0
    millor = None

    while True:
        intents = jugar_partida(1, 100)
        partides += 1
        intents_totals += intents
        millor = intents if (millor is None or intents < millor) else millor

        mitjana = intents_totals / partides
        print("\n📊 Estadístiques")
        print(f"  Partides: {partides}")
        print(f"  Intents totals: {intents_totals}")
        print(f"  Mitjana intents/partida: {mitjana:.2f}")
        print(f"  Millor partida: {millor} intents\n")

        if not llegir_si_no("Vols tornar a jugar? (s/n): "):
            break

    print("👋 Tornant al menú...")


if __name__ == "__main__":
    run()
