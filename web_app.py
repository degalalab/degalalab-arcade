import random
import string
import streamlit as st

st.set_page_config(page_title="Jocs Python", page_icon="🎮", layout="centered")

# ---------------------------
# Utilitats
# ---------------------------
def init_state_once():
    # Endevina
    if "endevina_secret" not in st.session_state:
        st.session_state.endevina_secret = random.randint(1, 100)
        st.session_state.endevina_intents = 0

    # RPS
    if "rps_stats" not in st.session_state:
        st.session_state.rps_stats = {"tu": 0, "pc": 0, "empat": 0}

    # Penjat
    if "penjat_paraula" not in st.session_state:
        reset_penjat()

    # Quiz
    if "quiz_mode" not in st.session_state:
        st.session_state.quiz_mode = "Normal"
    if "quiz_i" not in st.session_state:
        reset_quiz()


def reset_endevina():
    st.session_state.endevina_secret = random.randint(1, 100)
    st.session_state.endevina_intents = 0


def reset_penjat():
    paraules = [
        "python", "variables", "funcio", "bucle", "llista",
        "diccionari", "programa", "terminal", "notebook", "debug",
        "modul", "paquet", "classe", "objecte"
    ]
    st.session_state.penjat_paraula = random.choice(paraules)
    st.session_state.penjat_usades = set()
    st.session_state.penjat_encertades = set()
    st.session_state.penjat_intents_max = 6
    st.session_state.penjat_intents = 6
    st.session_state.penjat_msg = ""


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


def penjat_mostrar_paraula(paraula: str, encertades: set[str]) -> str:
    return " ".join([c if c in encertades else "_" for c in paraula])


# Preguntes Quiz (posa-hi totes les teves; aquí hi ha una base)
PREGUNTES = [
    {"q": "Quin tipus de dada retorna input() a Python?", "opcions": ["int", "str", "float", "bool"], "correcta": "str"},
    {"q": "Quina paraula clau surt d'un bucle abans d'hora?", "opcions": ["stop", "break", "exit", "return"], "correcta": "break"},
    {"q": "Quina estructura NO és mutable?", "opcions": ["list", "dict", "set", "tuple"], "correcta": "tuple"},
    {"q": "Quin operador comprova igualtat?", "opcions": ["=", "==", "!=", "<>"], "correcta": "=="},
    {"q": "Quina llibreria fem servir per nombres aleatoris?", "opcions": ["math", "random", "stats", "numpy"], "correcta": "random"},
    {"q": "Què imprimeix print('a', 'b', sep='-')?", "opcions": ["ab", "a b", "a-b", "a--b"], "correcta": "a-b"},
]


def reset_quiz(n_preguntes: int = 10):
    pool = PREGUNTES[:]
    random.shuffle(pool)
    st.session_state.quiz_qs = pool[: min(n_preguntes, len(pool))]
    st.session_state.quiz_i = 0
    st.session_state.quiz_punts = 0
    st.session_state.quiz_done = False
    st.session_state.quiz_respostes = []  # (pregunta_dict, resposta_tri)
    st.session_state.quiz_feedback = ""


init_state_once()

st.title("🎮 DeGalaLab Arcade")
st.caption("Arcade educativa: jocs curts per aprendre Python jugant. ✨")


joc = st.sidebar.selectbox(
    "Tria un joc",
    ["Endevina el nombre", "Pedra/Paper/Tisores", "Penjat", "Quiz"],
)
st.sidebar.markdown("### ℹ️ DeGalaLab Arcade")
st.sidebar.caption("Mini jocs fets amb Python + Streamlit per practicar programació.")
st.sidebar.caption("Privacitat: no es recullen dades personals, ni logins, ni emails. Tot funciona a la sessió del navegador.")
st.sidebar.markdown("**DeGalaLab:** https://degalalab.com")

st.sidebar.divider()

# ---------------------------
# 1) Endevina el nombre
# ---------------------------
if joc == "Endevina el nombre":
    st.header("🎯 Endevina el nombre")

    guess = st.number_input("Escriu un número (1–100)", min_value=1, max_value=100, step=1)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Provar", use_container_width=True):
            st.session_state.endevina_intents += 1
            secret = st.session_state.endevina_secret

            if guess < secret:
                st.info("És més gran")
            elif guess > secret:
                st.info("És més petit")
            else:
                st.success(f"Correcte! {st.session_state.endevina_intents} intents.")
                reset_endevina()

    with c2:
        if st.button("Reiniciar partida", use_container_width=True):
            reset_endevina()
            st.warning("Partida reiniciada.")

# ---------------------------
# 2) RPS
# ---------------------------
elif joc == "Pedra/Paper/Tisores":
    st.header("✂️ Pedra, paper o tisores")

    opcions = ["pedra", "paper", "tisores"]
    guanya_a = {"pedra": "tisores", "paper": "pedra", "tisores": "paper"}

    tria = st.radio("Tria:", opcions, horizontal=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Jugar", use_container_width=True):
            pc = random.choice(opcions)
            st.write("💻 Ordinador:", pc)

            if tria == pc:
                st.session_state.rps_stats["empat"] += 1
                st.info("🤝 Empat")
            elif guanya_a[tria] == pc:
                st.session_state.rps_stats["tu"] += 1
                st.success("✅ Guanyes!")
            else:
                st.session_state.rps_stats["pc"] += 1
                st.error("❌ Perds!")

    with c2:
        if st.button("Reiniciar marcador", use_container_width=True):
            st.session_state.rps_stats = {"tu": 0, "pc": 0, "empat": 0}
            st.warning("Marcador reiniciat.")

    st.subheader("📊 Marcador")
    st.write(st.session_state.rps_stats)

# ---------------------------
# 3) Penjat
# ---------------------------
elif joc == "Penjat":
    st.header("🔤 Penjat")

    paraula = st.session_state.penjat_paraula
    enc = st.session_state.penjat_encertades
    usadas = st.session_state.penjat_usades
    intents = st.session_state.penjat_intents
    intents_max = st.session_state.penjat_intents_max

    errors = intents_max - intents
    idx = min(errors, len(PENJAT) - 1)
    st.code(PENJAT[idx])

    estat = penjat_mostrar_paraula(paraula, enc)
    st.subheader(estat)

    st.write("**Intents restants:**", intents)
    st.write("**Lletres usades:**", " ".join(sorted(usadas)) if usadas else "(cap)")

    if st.session_state.penjat_msg:
        st.info(st.session_state.penjat_msg)

    # Final?
    if "_" not in estat:
        st.success(f"🏆 Has guanyat! La paraula era: **{paraula}**")
    elif intents == 0:
        st.error(f"💀 Has perdut! La paraula era: **{paraula}**")
    else:
        st.write("Tria una lletra:")

        # Teclat A-Z (simple)
        cols = st.columns(7)


        letters = list(string.ascii_lowercase)

        for i, ch in enumerate(letters):
            disabled = (ch in usadas) or (intents == 0) or ("_" not in estat)
            with cols[i % 7]:
                if st.button(ch, disabled=disabled):
                    usadas.add(ch)
                    if ch in paraula:
                        enc.add(ch)
                        st.session_state.penjat_msg = "✅ Bona!"
                    else:
                        st.session_state.penjat_intents -= 1
                        st.session_state.penjat_msg = "❌ No hi és."
                    st.rerun()

    if st.button("Reiniciar penjat"):
        reset_penjat()
        st.rerun()

# ---------------------------
# 4) Quiz: Normal vs Examen
# ---------------------------
else:
    st.header("❓Quiz")

    # Selector de mode
    mode = st.radio("Mode:", ["Normal", "Examen"], horizontal=True)
    if mode != st.session_state.quiz_mode:
        st.session_state.quiz_mode = mode
        reset_quiz(n_preguntes=10)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nou quiz", use_container_width=True):
            reset_quiz(n_preguntes=10)
            st.rerun()
    with c2:
        if st.button("Finalitzar i corregir", use_container_width=True, disabled=(st.session_state.quiz_mode != "Examen")):
            st.session_state.quiz_done = True

    qs = st.session_state.quiz_qs
    i = st.session_state.quiz_i

    # Si mode examen: deixem navegar pregunta a pregunta i guardem respostes
    if not st.session_state.quiz_done:
        if i >= len(qs):
            st.session_state.quiz_done = True
        else:
            p = qs[i]
            st.write(f"**Pregunta {i+1}/{len(qs)}**")
            st.write(p["q"])

            key = f"quiz_ans_{i}"
            resposta = st.radio("Resposta:", p["opcions"], key=key)

            if st.button("Enviar resposta"):
                # Guardem la resposta
                st.session_state.quiz_respostes.append((p, resposta))

                # Feedback segons mode
                if st.session_state.quiz_mode == "Normal":
                    if resposta == p["correcta"]:
                        st.session_state.quiz_punts += 1
                        st.success("✅ Correcte!")
                    else:
                        st.error(f"❌ Incorrecte. Era: {p['correcta']}")

                # Avança
                st.session_state.quiz_i += 1
                st.rerun()

    # Correcció / Resultats
    if st.session_state.quiz_done:
        respostes = st.session_state.quiz_respostes
        total = len(respostes)

        # En mode normal, punts ja s'ha anat sumant
        if st.session_state.quiz_mode == "Normal":
            punts = st.session_state.quiz_punts
            percent = (punts / total * 100) if total else 0
            st.subheader("📊 Resultats")
            st.write(f"**Punts:** {punts}/{total} ({percent:.1f}%)")

        else:
            # Mode examen: corregim ara
            encerts = 0
            errors_list = []
            for p, r in respostes:
                if r == p["correcta"]:
                    encerts += 1
                else:
                    errors_list.append((p["q"], r, p["correcta"]))

            percent = (encerts / total * 100) if total else 0
            st.subheader("📊 Resultats (Examen)")
            st.write(f"**Encerts:** {encerts}/{total} ({percent:.1f}%)")

            if errors_list:
                st.write("### ❌ Errors")
                for q, r_user, r_ok in errors_list:
                    st.write(f"- **{q}**")
                    st.write(f"  - La teva resposta: `{r_user}`")
                    st.write(f"  - Correcta: `{r_ok}`")
            else:
                st.success("🎉 Perfecte! Cap error.")
