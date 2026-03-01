"""
Tic-Tac-Toe Q-Learning Agent — Streamlit App
Agent is X and goes first. You are O.
"""

# streamlit run .\ttt_ql_stream.py

import random
import time
from collections import defaultdict
import streamlit as st

# ─── Game constants ────────────────────────────────────────────────────────────
EMPTY = "."
X, O = "X", "O"
WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# ─── Game helpers ──────────────────────────────────────────────────────────────
def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def terminal(board):
    return winner(board) is not None or EMPTY not in board

def legal_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]

def apply_move(board, idx, mark):
    b = list(board); b[idx] = mark; return "".join(b)

def final_reward(board):
    w = winner(board)
    return 1 if w == X else (-1 if w == O else 0)

def epsilon_greedy(Q, state, eps=0.0):
    moves = legal_moves(state)
    if random.random() < eps:
        return random.choice(moves)
    best = max(Q[(state, a)] for a in moves)
    best_moves = [a for a in moves if Q[(state, a)] == best]
    return random.choice(best_moves)

def reset_game():
    """Reset board so agent (X) goes first. Critically resets agent_moved=False."""
    st.session_state.board       = EMPTY * 9
    st.session_state.turn        = X
    st.session_state.game_over   = False
    st.session_state.result_msg  = ""
    st.session_state.result_class= ""
    st.session_state.agent_moved = False

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🎮", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

html, body, [class*="css"] {
    background-color: #0a0a12 !important;
    color: #e0e0f0 !important;
    font-family: 'Share Tech Mono', monospace !important;
}
h1, h2, h3 { font-family: 'Orbitron', sans-serif !important; letter-spacing: 0.1em; }

.title-glow {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.4rem; font-weight: 900; text-align: center;
    background: linear-gradient(90deg, #00f5d4, #9b5de5, #f72585);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: pulse-glow 3s ease-in-out infinite; margin-bottom: 0.2em;
}
@keyframes pulse-glow {
    0%, 100% { filter: brightness(1); } 50% { filter: brightness(1.4); }
}
.subtitle {
    text-align: center; color: #6c6c9c; font-size: 0.85rem;
    letter-spacing: 0.2em; margin-bottom: 2em;
}

.stButton > button {
    width: 100% !important; height: 100px !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 2.2rem !important; font-weight: 900 !important;
    border-radius: 12px !important; border: 2px solid #2a2a4a !important;
    background: #10101e !important; color: #e0e0f0 !important;
    transition: all 0.15s ease !important; cursor: pointer !important;
}
.stButton > button:hover {
    border-color: #9b5de5 !important; background: #1a1a2e !important;
    box-shadow: 0 0 20px rgba(155,93,229,0.4) !important;
    transform: translateY(-2px) !important;
}
.stButton > button:disabled {
    opacity: 0.85 !important; cursor: default !important; transform: none !important;
}

.status-box {
    text-align: center; padding: 1em 1.5em; border-radius: 12px;
    font-family: 'Orbitron', sans-serif; font-size: 1.1rem; font-weight: 700;
    letter-spacing: 0.08em; margin: 1em auto; max-width: 400px;
    animation: fade-in 0.4s ease;
}
@keyframes fade-in {
    from { opacity: 0; transform: translateY(-8px); } to { opacity: 1; transform: translateY(0); }
}
.status-your-turn { background: #0d2b1a; border: 2px solid #00f5d4; color: #00f5d4; }
.status-agent-turn{ background: #1a0d2b; border: 2px solid #9b5de5; color: #9b5de5; }
.status-win  { background: #1a2b0d; border: 2px solid #7fff00; color: #7fff00; }
.status-lose { background: #2b0d0d; border: 2px solid #f72585; color: #f72585; }
.status-draw { background: #1a1a1a; border: 2px solid #888;    color: #ccc; }

.train-box {
    background: #0d0d1e; border: 1px solid #2a2a4a; border-radius: 12px;
    padding: 1.5em; text-align: center; margin: 1em 0;
}
.train-title { font-family: 'Orbitron', sans-serif; font-size: 1.2rem; color: #9b5de5; margin-bottom: 0.5em; }
.train-ep    { font-size: 0.9rem; color: #6c6c9c; }

.stats-row {
    display: flex; justify-content: center; gap: 2em;
    margin: 0.5em 0 1.5em; flex-wrap: wrap;
}
.stat-pill {
    background: #10101e; border: 1px solid #2a2a4a; border-radius: 999px;
    padding: 0.4em 1.2em; font-size: 0.8rem; letter-spacing: 0.1em;
}
.stat-pill span { font-weight: bold; }
.stat-win  span { color: #00f5d4; }
.stat-lose span { color: #f72585; }
.stat-draw span { color: #888; }

hr { border-color: #1e1e3a !important; }
.stProgress > div > div { background: linear-gradient(90deg, #9b5de5, #f72585) !important; }
#MainMenu, footer { visibility: hidden; }
label { color: #a0a0c0 !important; font-size: 0.82rem !important; letter-spacing: 0.08em !important; }
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="title-glow">TIC-TAC-TOE AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">◈ Q-LEARNING AGENT ◈ AGENT IS X (GOES FIRST) ◈ YOU ARE O ◈</div>', unsafe_allow_html=True)

# ─── Session state init ────────────────────────────────────────────────────────
defaults = dict(
    Q=None, board=EMPTY * 9, turn=X,
    game_over=False, result_msg="", result_class="",
    wins=0, losses=0, draws=0, agent_moved=False,
)
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─── Training screen ───────────────────────────────────────────────────────────
if st.session_state.Q is None:
    st.markdown(
        '<div class="train-box"><div class="train-title">🤖 CONFIGURE & TRAIN THE AGENT</div></div>',
        unsafe_allow_html=True,
    )

    ep_choice = st.select_slider(
        "Training episodes",
        options=[50_000, 100_000, 200_000, 300_000],
        value=200_000,
        format_func=lambda x: f"{x:,}",
    )

    sl1, sl2 = st.columns(2)
    with sl1:
        gamma_choice = st.slider(
            "Gamma — future discount",
            min_value=0.5, max_value=1.0, value=0.9, step=0.05,
            help="1.0 = values future rewards highly; 0.5 = short-sighted",
        )
    with sl2:
        epsilon_choice = st.slider(
            "Epsilon — exploration rate",
            min_value=0.1, max_value=1.0, value=0.5, step=0.05,
            help="Higher = more random moves explored during training",
        )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⚡  START TRAINING", use_container_width=True):
            train_placeholder = st.empty()
            prog_bar = st.progress(0)
            CHUNKS     = 10
            chunk_size = ep_choice // CHUNKS
            Q          = defaultdict(float)
            alpha      = 0.3

            for chunk in range(CHUNKS):
                start_ep = chunk * chunk_size + 1
                end_ep   = (chunk + 1) * chunk_size

                for ep in range(start_ep, end_ep + 1):
                    board = EMPTY * 9
                    state = board
                    while True:
                        action     = epsilon_greedy(Q, state, epsilon_choice)
                        next_state = apply_move(state, action, X)
                        if terminal(next_state):
                            r = final_reward(next_state)
                            Q[(state, action)] += alpha * (r - Q[(state, action)])
                            break
                        opp_action = random.choice(legal_moves(next_state))
                        after_opp  = apply_move(next_state, opp_action, O)
                        if terminal(after_opp):
                            r = final_reward(after_opp)
                            Q[(state, action)] += alpha * (r - Q[(state, action)])
                            break
                        best_next = max(Q[(after_opp, a)] for a in legal_moves(after_opp))
                        Q[(state, action)] += alpha * (gamma_choice * best_next - Q[(state, action)])
                        state = after_opp

                prog_bar.progress((chunk + 1) / CHUNKS)
                train_placeholder.markdown(
                    f'<div class="train-box">'
                    f'<div class="train-title">⚙ TRAINING IN PROGRESS</div>'
                    f'<div class="train-ep">{end_ep:,} / {ep_choice:,} episodes &nbsp;|&nbsp; '
                    f'γ={gamma_choice} &nbsp; ε={epsilon_choice}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            st.session_state.Q = Q
            train_placeholder.empty()
            prog_bar.empty()
            st.success("✅ Training complete! Let's play.")
            time.sleep(0.7)
            reset_game()
            st.rerun()

    st.stop()

# ─── Game screen ───────────────────────────────────────────────────────────────
st.markdown(
    f'<div class="stats-row">'
    f'<div class="stat-pill stat-win">YOU WIN  <span>{st.session_state.wins}</span></div>'
    f'<div class="stat-pill stat-lose">AI WINS  <span>{st.session_state.losses}</span></div>'
    f'<div class="stat-pill stat-draw">DRAWS  <span>{st.session_state.draws}</span></div>'
    f'</div>',
    unsafe_allow_html=True,
)

board = st.session_state.board

# Status banner
if st.session_state.game_over:
    st.markdown(
        f'<div class="status-box {st.session_state.result_class}">{st.session_state.result_msg}</div>',
        unsafe_allow_html=True,
    )
elif st.session_state.turn == O:
    st.markdown('<div class="status-box status-your-turn">▶ YOUR TURN — CLICK A CELL</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-box status-agent-turn">🤖 AGENT IS THINKING…</div>', unsafe_allow_html=True)

# Board grid
def cell_label(val):
    return "✗" if val == X else ("◯" if val == O else " ")

for row in range(3):
    cols = st.columns(3, gap="small")
    for col in range(3):
        idx      = row * 3 + col
        val      = board[idx]
        disabled = (val != EMPTY) or st.session_state.game_over or (st.session_state.turn != O)
        with cols[col]:
            if st.button(cell_label(val), key=f"cell_{idx}", disabled=disabled, use_container_width=True):
                new_board = apply_move(board, idx, O)
                st.session_state.board = new_board
                if terminal(new_board):
                    st.session_state.game_over = True
                    r = final_reward(new_board)
                    if r == -1:
                        st.session_state.result_msg   = "🎉 YOU WIN!"
                        st.session_state.result_class = "status-win"
                        st.session_state.wins += 1
                    else:
                        st.session_state.result_msg   = "⚖ DRAW"
                        st.session_state.result_class = "status-draw"
                        st.session_state.draws += 1
                else:
                    st.session_state.turn        = X
                    st.session_state.agent_moved = False  # allow agent to move next render
                st.rerun()

# Agent auto-move
if (not st.session_state.game_over
        and st.session_state.turn == X
        and not st.session_state.agent_moved):
    time.sleep(0.4)
    a         = epsilon_greedy(st.session_state.Q, st.session_state.board, eps=0.0)
    new_board = apply_move(st.session_state.board, a, X)
    st.session_state.board       = new_board
    st.session_state.agent_moved = True  # mark done BEFORE rerun to prevent double-fire

    if terminal(new_board):
        st.session_state.game_over = True
        r = final_reward(new_board)
        if r == 1:
            st.session_state.result_msg   = "🤖 AI WINS!"
            st.session_state.result_class = "status-lose"
            st.session_state.losses += 1
        else:
            st.session_state.result_msg   = "⚖ DRAW"
            st.session_state.result_class = "status-draw"
            st.session_state.draws += 1
    else:
        st.session_state.turn = O

    st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Control buttons
b1, b2, b3 = st.columns(3)
with b2:
    if st.button("🔄  NEW GAME", use_container_width=True):
        reset_game()  # agent_moved=False → agent fires on next render
        st.rerun()
with b3:
    if st.button("⚙  RETRAIN", use_container_width=True):
        st.session_state.Q      = None
        st.session_state.wins   = 0
        st.session_state.losses = 0
        st.session_state.draws  = 0
        reset_game()
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center;color:#3a3a5a;font-size:0.75rem;letter-spacing:0.15em;">'
    'Q-LEARNING · ε-GREEDY POLICY · TRAINED VS RANDOM OPPONENT</div>',
    unsafe_allow_html=True,
)