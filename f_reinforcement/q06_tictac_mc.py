# Monte Carlo (first-visit) control for Tic-Tac-Toe
# Agent = X, Opponent = random O
# Learns Q(s,a) by running full games and updating at the end

import random
from collections import defaultdict

EMPTY = "."
X = "X"   # agent
O = "O"   # opponent

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def winner(board):
    for a,b,c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def terminal(board):
    return winner(board) is not None or EMPTY not in board

def legal_moves(board):
    return [i for i,ch in enumerate(board) if ch == EMPTY]

def apply_move(board, idx, mark):
    b = list(board)
    b[idx] = mark
    return "".join(b)

def reward_final(board):
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0  # draw

def epsilon_greedy_action(Q, state, eps):
    moves = legal_moves(state)
    if not moves:
        return None
    if random.random() < eps:
        return random.choice(moves)
    # greedy with random tie-break
    best = None
    best_val = float("-inf")
    for a in moves:
        v = Q[(state, a)]
        if v > best_val:
            best_val = v
            best = [a]
        elif v == best_val:
            best.append(a)
    return random.choice(best)

def generate_episode(Q, eps):
    """
    Returns:
      history: list of (state_before_X, action_X) for agent decisions
      final_reward: +1/-1/0 at terminal
    """
    board = EMPTY * 9
    history = []

    turn = X  # X always starts
    while True:
        if turn == X:
            a = epsilon_greedy_action(Q, board, eps)
            if a is None:
                break
            history.append((board, a))
            board = apply_move(board, a, X)
        else:
            moves = legal_moves(board)
            if not moves:
                break
            a = random.choice(moves)
            board = apply_move(board, a, O)

        if terminal(board):
            break

        turn = O if turn == X else X

    return history, reward_final(board)

def train_monte_carlo(num_episodes=200_000, epsilon=0.2, gamma=1.0):
    # Q values and Monte Carlo bookkeeping
    Q = defaultdict(float)
    returns_sum = defaultdict(float)
    returns_count = defaultdict(int)

    for ep in range(1, num_episodes + 1):
        episode, G_terminal = generate_episode(Q, epsilon)

        # In Tic-Tac-Toe here, reward is only at the end, so every visited (s,a)
        # gets the same return, discounted by how far from the end it was:
        # G_t = (gamma^(T-1-t)) * G_terminal
        seen = set()
        T = len(episode)
        for t, (s, a) in enumerate(episode):
            if (s, a) in seen:
                continue  # first-visit MC
            seen.add((s, a))

            power = (T - 1 - t)
            G = (gamma ** power) * G_terminal

            returns_sum[(s, a)] += G
            returns_count[(s, a)] += 1
            Q[(s, a)] = returns_sum[(s, a)] / returns_count[(s, a)]

        # optional tiny progress print
        if ep % 50_000 == 0:
            print(f"episode {ep} done")

    return Q

def pretty(board):
    def cell(i):
        return board[i] if board[i] != EMPTY else " "
    return (
        f"{cell(0)}|{cell(1)}|{cell(2)}\n"
        f"-+-+-\n"
        f"{cell(3)}|{cell(4)}|{cell(5)}\n"
        f"-+-+-\n"
        f"{cell(6)}|{cell(7)}|{cell(8)}\n"
    )

def play_vs_agent(Q, eps_agent=0.0):
    board = EMPTY * 9
    turn = X
    print("You are O. Enter moves 1-9.\n")

    while True:
        print(pretty(board))

        if terminal(board):
            r = reward_final(board)
            if r == 1:
                print("Agent (X) wins")
            elif r == -1:
                print("You (O) win")
            else:
                print("Draw")
            return

        if turn == X:
            a = epsilon_greedy_action(Q, board, eps_agent)
            board = apply_move(board, a, X)
            turn = O
        else:
            moves = legal_moves(board)
            while True:
                try:
                    m = int(input("Your move (1-9): ")) - 1
                    if m in moves:
                        break
                    print("Illegal, try again")
                except:
                    print("Bad input, try again")
            board = apply_move(board, m, O)
            turn = X

if __name__ == "__main__":
    Q = train_monte_carlo(num_episodes=200_000, epsilon=0.2, gamma=1.0)
    print("Training done\n")
    play_vs_agent(Q, eps_agent=0.0)
