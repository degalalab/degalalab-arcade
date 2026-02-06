import random


PREGUNTES = [
    {
        "q": "Quin tipus de dada retorna input() a Python?",
        "opcions": ["int", "str", "float", "bool"],
        "correcta": "str",
    },
    {
        "q": "Quina paraula clau surt d'un bucle abans d'hora?",
        "opcions": ["stop", "break", "exit", "return"],
        "correcta": "break",
    },
    {
        "q": "Quina estructura NO és mutable?",
        "opcions": ["list", "dict", "set", "tuple"],
        "correcta": "tuple",
    },
    {
        "q": "Quin operador comprova igualtat?",
        "opcions": ["=", "==", "!=", "<>"],
        "correcta": "==",
    },
    {
        "q": "Quina funció converteix a enter?",
        "opcions": ["str()", "int()", "float()", "bool()"],
        "correcta": "int()",
    },
    {
        "q": "Què fa len(x)?",
        "opcions": ["Suma elements", "Compta elements", "Ordena", "Copia"],
        "correcta": "Compta elements",
    },
    {
        "q": "Com s'afegeix un element al final d'una llista L?",
        "opcions": ["L.add(x)", "L.append(x)", "L.push(x)", "L.insert_end(x)"],
        "correcta": "L.append(x)",
    },
    {
        "q": "Quin mètode dona parelles (clau, valor) d'un dict?",
        "opcions": ["keys()", "values()", "items()", "pairs()"],
        "correcta": "items()",
    },
    {
        "q": "Quina llibreria fem servir per nombres aleatoris?",
        "opcions": ["math", "random", "stats", "numpy"],
        "correcta": "random",
    },
    {
        "q": "Què imprimeix print('a', 'b', sep='-')?",
        "opcions": ["ab", "a b", "a-b", "a--b"],
        "correcta": "a-b",
    },
        {
        "q": "Què fa l'operador % en Python?",
        "opcions": ["Divisió", "Mòdul (residu)", "Potència", "Percentatge"],
        "correcta": "Mòdul (residu)",
    },
    {
        "q": "Quin valor booleà retorna bool(0)?",
        "opcions": ["True", "False", "0", "None"],
        "correcta": "False",
    },
    {
        "q": "Com es defineix una funció en Python?",
        "opcions": ["function f():", "def f():", "func f():", "define f():"],
        "correcta": "def f():",
    },
    {
        "q": "Què retorna range(3)?",
        "opcions": [
            "[0, 1, 2]",
            "0, 1, 2",
            "Un objecte iterable",
            "Una llista"
        ],
        "correcta": "Un objecte iterable",
    },
    {
        "q": "Què fa break dins d'un bucle?",
        "opcions": [
            "Salta a la següent iteració",
            "Acaba el programa",
            "Surt del bucle",
            "Reinicia el bucle"
        ],
        "correcta": "Surt del bucle",
    },
    {
        "q": "Què fa continue dins d'un bucle?",
        "opcions": [
            "Surt del bucle",
            "Acaba el programa",
            "Salta a la següent iteració",
            "Reinicia el bucle"
        ],
        "correcta": "Salta a la següent iteració",
    },
    {
        "q": "Quin mètode elimina l'últim element d'una llista?",
        "opcions": ["remove()", "delete()", "pop()", "clear()"],
        "correcta": "pop()",
    },
    {
        "q": "Què retorna dict.get('clau') si la clau no existeix?",
        "opcions": ["Error", "None", "0", "False"],
        "correcta": "None",
    },
    {
        "q": "Quin tipus de dada és {'a', 'b', 'c'}?",
        "opcions": ["list", "tuple", "dict", "set"],
        "correcta": "set",
    },
    {
        "q": "Com s'accedeix al primer element d'una llista L?",
        "opcions": ["L(0)", "L[1]", "L[0]", "first(L)"],
        "correcta": "L[0]",
    },
    {
        "q": "Què fa el mètode split() en un string?",
        "opcions": [
            "Uneix strings",
            "Divideix un string en parts",
            "Elimina espais",
            "Converteix a llista"
        ],
        "correcta": "Divideix un string en parts",
    },
    {
        "q": "Quin operador s'utilitza per 'i lògic'?",
        "opcions": ["&&", "&", "and", "or"],
        "correcta": "and",
    },
    {
        "q": "Quin operador s'utilitza per 'o lògic'?",
        "opcions": ["||", "|", "or", "and"],
        "correcta": "or",
    },
    {
        "q": "Què fa len([])?",
        "opcions": ["None", "Error", "0", "1"],
        "correcta": "0",
    },
    {
        "q": "Quin tipus de dada retorna input() sempre?",
        "opcions": ["int", "float", "bool", "str"],
        "correcta": "str",
    },
    {
        "q": "Com s'escriu un comentari d'una sola línia?",
        "opcions": ["// comentari", "/* comentari */", "# comentari", "<!-- -->"],
        "correcta": "# comentari",
    },
    {
        "q": "Quin operador comprova desigualtat?",
        "opcions": ["<>", "!=", "==", "="],
        "correcta": "!=",
    },
    {
        "q": "Què fa pass en Python?",
        "opcions": [
            "Surt del programa",
            "No fa res",
            "Salta iteració",
            "Llença error"
        ],
        "correcta": "No fa res",
    },
    {
        "q": "Què retorna type(3.0)?",
        "opcions": ["int", "float", "str", "double"],
        "correcta": "float",
    },
    {
        "q": "Què fa enumerate(L)?",
        "opcions": [
            "Ordena la llista",
            "Retorna índex i valor",
            "Copia la llista",
            "Filtra la llista"
        ],
        "correcta": "Retorna índex i valor",
    },
        {
        "q": "Què fa el mètode upper() en un string?",
        "opcions": ["Converteix a minúscules", "Converteix a majúscules", "Elimina espais", "Divideix el string"],
        "correcta": "Converteix a majúscules",
    },
    {
        "q": "Què retorna 'abc'.upper()?",
        "opcions": ["'abc'", "'ABC'", "'Abc'", "Error"],
        "correcta": "'ABC'",
    },
    {
        "q": "Què fa el mètode strip()?",
        "opcions": ["Elimina tots els espais", "Elimina espais al principi i al final", "Divideix el string", "Converteix a llista"],
        "correcta": "Elimina espais al principi i al final",
    },
    {
        "q": "Què fa len('python')?",
        "opcions": ["5", "6", "7", "Error"],
        "correcta": "6",
    },
    {
        "q": "Quin error es produeix si accedeixes a un índex inexistent?",
        "opcions": ["KeyError", "TypeError", "IndexError", "ValueError"],
        "correcta": "IndexError",
    },
    {
        "q": "Què retorna [1, 2, 3][1]?",
        "opcions": ["1", "2", "3", "Error"],
        "correcta": "2",
    },
    {
        "q": "Què fa el mètode append()?",
        "opcions": ["Afegeix al principi", "Afegeix al final", "Elimina un element", "Ordena la llista"],
        "correcta": "Afegeix al final",
    },
    {
        "q": "Què fa el mètode sort()?",
        "opcions": ["Crea una còpia ordenada", "Ordena la llista in-place", "Retorna una nova llista", "No modifica res"],
        "correcta": "Ordena la llista in-place",
    },
    {
        "q": "Què retorna sorted([3, 1, 2])?",
        "opcions": ["[3, 1, 2]", "[1, 2, 3]", "None", "Error"],
        "correcta": "[1, 2, 3]",
    },
    {
        "q": "Què fa del L[0]?",
        "opcions": ["Elimina el primer element", "Elimina l'últim", "Buida la llista", "Retorna l'element"],
        "correcta": "Elimina el primer element",
    },
    {
        "q": "Què retorna dict.keys()?",
        "opcions": ["Una llista", "Un conjunt", "Una vista de claus", "Un diccionari"],
        "correcta": "Una vista de claus",
    },
    {
        "q": "Quin mètode comprova si una clau existeix en un dict?",
        "opcions": ["has()", "in", "exists()", "contains()"],
        "correcta": "in",
    },
    {
        "q": "Què fa 'a' in 'python'?",
        "opcions": ["True", "False", "Error", "None"],
        "correcta": "False",
    },
    {
        "q": "Què fa 't' in 'python'?",
        "opcions": ["True", "False", "Error", "None"],
        "correcta": "True",
    },
    {
        "q": "Què retorna range(1, 4)?",
        "opcions": ["[1, 2, 3, 4]", "[1, 2, 3]", "1, 2, 3", "Un iterable"],
        "correcta": "Un iterable",
    },
    {
        "q": "Quin és l'últim valor produït per range(5)?",
        "opcions": ["3", "5", "4", "Error"],
        "correcta": "4",
    },
    {
        "q": "Què fa list(range(3))?",
        "opcions": ["[1, 2, 3]", "Error", "[0, 1, 2, 3]","[0, 1, 2]"],
        "correcta": "[0, 1, 2]",
    },
    {
        "q": "Què fa input() si l'usuari no escriu res i prem Enter?",
        "opcions": ["Error", "None", "Cadena buida", "0"],
        "correcta": "Cadena buida",
    },
    {
        "q": "Què fa int('')?",
        "opcions": ["0", "None", "ValueError", "TypeError"],
        "correcta": "ValueError",
    },
    {
        "q": "Què fa try/except?",
        "opcions": ["Evita errors", "Gestiona excepcions", "Ignora el codi", "Atura el programa"],
        "correcta": "Gestiona excepcions",
    },
    {
        "q": "Què fa finally en un try/except?",
        "opcions": ["Només s'executa si hi ha error", "S'executa sempre", "Evita l'error", "Reintenta el codi"],
        "correcta": "S'executa sempre",
    },
    {
        "q": "Quin tipus de dada és None?",
        "opcions": ["int", "bool", "NoneType", "str"],
        "correcta": "NoneType",
    },
    {
        "q": "Què fa exit() en un programa?",
        "opcions": ["Surt del bucle", "Surt de la funció", "Tanca el programa", "No fa res"],
        "correcta": "Tanca el programa",
    },
    {
        "q": "Què retorna bool('')?",
        "opcions": ["True", "False", "None", "Error"],
        "correcta": "False",
    },
    {
        "q": "Què retorna bool('hola')?",
        "opcions": ["True", "False", "None", "Error"],
        "correcta": "True",
    },


]


def triar_preguntes(n: int = 10) -> list[dict]:
    # barreja i agafa n (si n > disponibles, agafa totes)
    copia = PREGUNTES[:]
    random.shuffle(copia)
    return copia[: min(n, len(copia))]


def llegir_opcio(num_opcions: int) -> int:
    while True:
        x = input(f"Resposta (1-{num_opcions}) o 'q' per sortir: ").strip().lower()
        if x == "q":
            return -1
        if x.isdigit():
            k = int(x)
            if 1 <= k <= num_opcions:
                return k
        print("⚠️ Tria un número vàlid.")


def jugar_quiz(vides: int = 3, n_preguntes: int = 10) -> None:
    preguntes = triar_preguntes(n_preguntes)
    punts = 0
    fetes = 0

    print("\n🧠 Quiz Python (3 vides). Som-hi!\n")

    for p in preguntes:
        if vides == 0:
            break

        fetes += 1
        print(f"— Pregunta {fetes}/{len(preguntes)} —")
        print(p["q"])

        opcions = p["opcions"]
        for i, op in enumerate(opcions, start=1):
            print(f"  {i}) {op}")

        idx = llegir_opcio(len(opcions))
        if idx == -1:
            print("👋 Surts del quiz.")
            return

        resposta = opcions[idx - 1]

        if resposta == p["correcta"]:
            punts += 1
            print("✅ Correcte!\n")
        else:
            vides -= 1
            print(f"❌ Incorrecte. La bona era: {p['correcta']}")
            print(f"❤️ Vides restants: {vides}\n")

    percent = (punts / fetes * 100) if fetes else 0
    print("🏁 Final del quiz!")
    print(f"✅ Punts: {punts}/{fetes} ({percent:.1f}%)")

def jugar_examen(n_preguntes: int = 10) -> None:
    preguntes = triar_preguntes(n_preguntes)
    respostes = []  # guardem (pregunta, resposta_usuari)

    print("\n📝 Mode EXAMEN")
    print("Respon totes les preguntes. No tindràs feedback fins al final.\n")

    for i, p in enumerate(preguntes, start=1):
        print(f"— Pregunta {i}/{len(preguntes)} —")
        print(p["q"])

        opcions = p["opcions"]
        for j, op in enumerate(opcions, start=1):
            print(f"  {j}) {op}")

        idx = llegir_opcio(len(opcions))
        if idx == -1:
            print("👋 Examen cancel·lat.")
            return

        resposta = opcions[idx - 1]
        respostes.append((p, resposta))
        print()  # línia en blanc

    # Correcció
    encerts = 0
    errors = []

    for p, r in respostes:
        if r == p["correcta"]:
            encerts += 1
        else:
            errors.append((p["q"], r, p["correcta"]))

    percent = encerts / len(respostes) * 100

    print("\n📊 RESULTAT EXAMEN")
    print(f"Encerts: {encerts}/{len(respostes)}")
    print(f"Percentatge: {percent:.1f}%")

    if errors:
        print("\n❌ Errors:")
        for q, r_user, r_ok in errors:
            print(f"- {q}")
            print(f"  La teva resposta: {r_user}")
            print(f"  Resposta correcta: {r_ok}\n")
    else:
        print("\n🎉 Perfecte! Cap error.")

def run() -> None:
    while True:
        print("\n🧠 Quiz Python")
        print("1) Mode normal")
        print("2) Mode examen")
        print("0) Sortir")

        op = input("Tria una opció: ").strip()

        if op == "1":
            jugar_quiz(vides=3, n_preguntes=10)
        elif op == "2":
            jugar_examen(n_preguntes=10)
        elif op == "0":
            print("👋 Tornant al menú...")
            break
        else:
            print("⚠️ Opció no vàlida.")


if __name__ == "__main__":
    run()

