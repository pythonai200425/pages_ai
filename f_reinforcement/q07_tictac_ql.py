# Q-learning for Tic-Tac-Toe
# Agent = X, Opponent = random O

import random
from collections import defaultdict

EMPTY = "."
X = "X"
O = "O"

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# ---------- Game helpers ----------
def winner(board):
    for a,b,c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def terminal(board):
    return winner(board) is not None or EMPTY not in board

def legal_moves(board):
    return [i for i,v in enumerate(board) if v == EMPTY]

def apply_move(board, idx, mark):
    b = list(board)
    b[idx] = mark
    return "".join(b)

def final_reward(board):
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0

# ---------- Q-learning ----------
def epsilon_greedy(Q, state, eps):
    moves = legal_moves(state)
    if random.random() < eps:
        return random.choice(moves)
    best = max(Q[(state, a)] for a in moves)
    best_moves = [a for a in moves if Q[(state, a)] == best]
    return random.choice(best_moves)

def train_qlearning(
    episodes=200_000,
    alpha=0.3,
    gamma=0.9,
    epsilon=0.2
):
    Q = defaultdict(float)

    for ep in range(1, episodes + 1):
        board = EMPTY * 9
        state = board

        while True:
            # ----- Agent move -----
            action = epsilon_greedy(Q, state, epsilon)
            next_state = apply_move(state, action, X)

            if terminal(next_state):
                r = final_reward(next_state)
                Q[(state, action)] += alpha * (r - Q[(state, action)])
                break

            # ----- Opponent move (environment) -----
            opp_action = random.choice(legal_moves(next_state))
            after_opp = apply_move(next_state, opp_action, O)

            if terminal(after_opp):
                r = final_reward(after_opp)
                Q[(state, action)] += alpha * (r - Q[(state, action)])
                break

            # ----- Q-learning update (bootstrapping) -----
            best_next = max(Q[(after_opp, a)] for a in legal_moves(after_opp))
            Q[(state, action)] += alpha * (gamma * best_next - Q[(state, action)])

            state = after_opp

        if ep % 50_000 == 0:
            print(f"episode {ep}")

    return Q

# ---------- Play vs trained agent ----------
def pretty(board):
    def c(i): return board[i] if board[i] != EMPTY else " "
    return (
        f"{c(0)}|{c(1)}|{c(2)}\n"
        f"-+-+-\n"
        f"{c(3)}|{c(4)}|{c(5)}\n"
        f"-+-+-\n"
        f"{c(6)}|{c(7)}|{c(8)}\n"
    )

def play_vs_agent(Q):
    board = EMPTY * 9
    turn = X
    print("You are O. Moves 1-9\n")

    while True:
        print(pretty(board))

        if terminal(board):
            r = final_reward(board)
            if r == 1:
                print("Agent wins")
            elif r == -1:
                print("You win")
            else:
                print("Draw")
            return

        if turn == X:
            a = epsilon_greedy(Q, board, eps=0.0)
            board = apply_move(board, a, X)
            turn = O
        else:
            moves = legal_moves(board)
            m = int(input("Your move (1-9): ")) - 1
            if m in moves:
                board = apply_move(board, m, O)
                turn = X

# ---------- Run ----------
if __name__ == "__main__":
    Q = train_qlearning()
    print("Training finished\n")
    play_vs_agent(Q)
