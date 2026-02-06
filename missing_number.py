# missing_number.py
from __future__ import annotations

import random
import streamlit as st


# --- Banc de reptes (petit però ampliable) ---
CHALLENGES = [
    # seq, options, answer
    {"seq": [2, 4, 6, None], "options": [7, 8, 10], "answer": 8, "hint": "Parells (+2)"},
    {"seq": [3, 6, 9, None], "options": [10, 12, 15], "answer": 12, "hint": "Multiples de 3"},
    {"seq": [1, 1, 2, 3, 5, None], "options": [6, 8, 9], "answer": 8, "hint": "Fibonacci"},
    {"seq": [10, 8, 6, None], "options": [5, 4, 3], "answer": 4, "hint": "Resta 2"},
    {"seq": [1, 4, 9, None], "options": [12, 15, 16], "answer": 16, "hint": "Quadrats (1²,2²,3²,4²)"},
    {"seq": [5, 10, 20, None], "options": [25, 30, 40], "answer": 40, "hint": "Doblar"},
    {"seq": [2, 3, 5, 8, None], "options": [11, 12, 13], "answer": 13, "hint": "Cada terme és suma dels dos anteriors"},
    {"seq": [100, 50, 25, None], "options": [10, 12.5, 15], "answer": 12.5, "hint": "Dividir per 2"},
]


def _format_seq(seq: list[float | int | None]) -> str:
    return ", ".join("?" if x is None else str(x) for x in seq)


def init_state() -> None:
    if "mn_score" not in st.session_state:
        st.session_state.mn_score = 0
    if "mn_total" not in st.session_state:
        st.session_state.mn_total = 0
    if "mn_remaining" not in st.session_state:
        st.session_state.mn_remaining = list(range(len(CHALLENGES)))
        random.shuffle(st.session_state.mn_remaining)
    if "mn_current" not in st.session_state:
        st.session_state.mn_current = None
    if "mn_feedback" not in st.session_state:
        st.session_state.mn_feedback = None
    if "mn_revealed" not in st.session_state:
        st.session_state.mn_revealed = False


def new_round() -> None:
    # si s’han esgotat, rebarreja
    if not st.session_state.mn_remaining:
        st.session_state.mn_remaining = list(range(len(CHALLENGES)))
        random.shuffle(st.session_state.mn_remaining)

    idx = st.session_state.mn_remaining.pop()
    st.session_state.mn_current = idx
    st.session_state.mn_feedback = None
    st.session_state.mn_revealed = False


def reset_game() -> None:
    for k in ["mn_score", "mn_total", "mn_remaining", "mn_current", "mn_feedback", "mn_revealed"]:
        if k in st.session_state:
            del st.session_state[k]
    init_state()
    new_round()


def render_missing_number_game() -> None:
    st.title("🔎 Quina falta?")
    st.caption("Tria el número que falta a la seqüència. Joc curt, ràpid i perfecte per practicar patrons.")

    init_state()
    if st.session_state.mn_current is None:
        new_round()

    idx = st.session_state.mn_current
    ch = CHALLENGES[idx]

    col1, col2, col3 = st.columns(3)
    col1.metric("Punts", st.session_state.mn_score)
    col2.metric("Rondes", st.session_state.mn_total)
    col3.metric("Pendents", len(st.session_state.mn_remaining))

    st.subheader("Seqüència")
    st.code(_format_seq(ch["seq"]), language="text")

    # resposta
    choice = st.radio("Quin número hi falta?", ch["options"], horizontal=True, key=f"mn_choice_{idx}")

    cta1, cta2, cta3 = st.columns([1, 1, 1])
    with cta1:
        if st.button("✅ Comprova", use_container_width=True, disabled=st.session_state.mn_revealed):
            st.session_state.mn_total += 1
            if choice == ch["answer"]:
                st.session_state.mn_score += 1
                st.session_state.mn_feedback = ("success", "Correcte! 🎉")
            else:
                st.session_state.mn_feedback = ("error", f"No 😅 La resposta era **{ch['answer']}**.")
            st.session_state.mn_revealed = True

    with cta2:
        if st.button("💡 Pista", use_container_width=True):
            st.info(f"Pista: {ch['hint']}")

    with cta3:
        if st.button("🔁 Reinicia", use_container_width=True):
            reset_game()
            st.rerun()

    # feedback
    if st.session_state.mn_feedback:
        kind, msg = st.session_state.mn_feedback
        getattr(st, kind)(msg)

    # següent
    if st.session_state.mn_revealed:
        if st.button("➡️ Següent repte", use_container_width=True):
            new_round()
            st.rerun()


# --- Execució directa (si el vols com a fitxer standalone) ---
if __name__ == "__main__":
    render_missing_number_game()
