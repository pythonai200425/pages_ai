"""
Q-learning for Tic-Tac-Toe
Agent = X, Opponent = random O
Implemented using a custom OpenAI Gym environment.
"""

import random
import numpy as np
from collections import defaultdict

import gymnasium as gym
from gymnasium import spaces


# ─────────────────────────────────────────────
# 1.  Custom Gym Environment
# ─────────────────────────────────────────────

EMPTY = 0
X     = 1
O     = 2

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),   # rows
    (0,3,6),(1,4,7),(2,5,8),   # cols
    (0,4,8),(2,4,6)            # diagonals
]


class TicTacToeEnv(gym.Env):
    """
    Single-agent Tic-Tac-Toe environment.

    Observation : length-9 numpy array, values in {0,1,2}
                  0 = empty, 1 = X (agent), 2 = O (opponent)
    Action      : integer in [0, 8]  (board cell index)
    Reward      : +1  agent wins
                   0  draw or game continues
                  -1  opponent wins (or illegal move)

    After each agent step the environment automatically plays
    a random opponent move before returning control.
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode

        # 9 cells, each can be 0/1/2
        self.observation_space = spaces.MultiDiscrete([3] * 9)
        # 9 possible cells to place X
        self.action_space = spaces.Discrete(9)

        self.board = None

    # ── helpers ──────────────────────────────

    def _winner(self):
        for a, b, c in WIN_LINES:
            if self.board[a] != EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def _is_terminal(self):
        return self._winner() is not None or EMPTY not in self.board

    def _legal_moves(self):
        return [i for i, v in enumerate(self.board) if v == EMPTY]

    def _obs(self):
        return self.board.copy()

    # ── Gym API ──────────────────────────────

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.board = np.zeros(9, dtype=np.int8)
        return self._obs(), {}

    def step(self, action):
        # ── illegal move ──
        if self.board[action] != EMPTY:
            return self._obs(), -1.0, True, False, {"reason": "illegal"}

        # ── agent plays X ──
        self.board[action] = X

        if self._is_terminal():
            reward = 1.0 if self._winner() == X else 0.0
            return self._obs(), reward, True, False, {}

        # ── opponent plays O (random) ──
        opp_action = random.choice(self._legal_moves())
        self.board[opp_action] = O

        if self._is_terminal():
            w = self._winner()
            reward = -1.0 if w == O else 0.0
            return self._obs(), reward, True, False, {}

        # ── game continues ──
        return self._obs(), 0.0, False, False, {}

    def render(self):
        symbols = {EMPTY: ".", X: "X", O: "O"}
        b = [symbols[v] for v in self.board]
        print(f"\n{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}\n")


# ─────────────────────────────────────────────
# 2.  Q-learning Agent
# ─────────────────────────────────────────────

def obs_to_key(obs: np.ndarray) -> tuple:
    """Convert numpy observation to a hashable state key."""
    return tuple(obs.tolist())


def epsilon_greedy(Q: dict, state_key: tuple, legal: list, eps: float) -> int:
    if random.random() < eps or not any((state_key, a) in Q for a in legal):
        return random.choice(legal)
    best_val = max(Q.get((state_key, a), 0.0) for a in legal)
    best_actions = [a for a in legal if Q.get((state_key, a), 0.0) == best_val]
    return random.choice(best_actions)


def train_qlearning(
    episodes: int = 200_000,
    alpha:    float = 0.3,
    gamma:    float = 0.9,
    epsilon:  float = 0.5,
) -> dict:
    env = TicTacToeEnv()
    Q: dict = defaultdict(float)

    for ep in range(1, episodes + 1):
        obs, _ = env.reset()
        state_key = obs_to_key(obs)

        while True:
            legal = [i for i, v in enumerate(obs) if v == EMPTY]
            action = epsilon_greedy(Q, state_key, legal, epsilon)

            next_obs, reward, terminated, truncated, _ = env.step(action)
            next_key = obs_to_key(next_obs)
            done = terminated or truncated

            if done:
                # Terminal update — no bootstrap
                Q[(state_key, action)] += alpha * (reward - Q[(state_key, action)])
                break

            # Bootstrap from best next action
            next_legal = [i for i, v in enumerate(next_obs) if v == EMPTY]
            best_next = max(Q.get((next_key, a), 0.0) for a in next_legal)
            target = reward + gamma * best_next
            Q[(state_key, action)] += alpha * (target - Q[(state_key, action)])

            obs = next_obs
            state_key = next_key

        if ep % 50_000 == 0:
            print(f"  episode {ep:>7,}")

    env.close()
    return Q


# ─────────────────────────────────────────────
# 3.  Evaluation helper
# ─────────────────────────────────────────────

def evaluate(Q: dict, n_games: int = 10_000) -> None:
    env = TicTacToeEnv()
    wins = draws = losses = 0

    for _ in range(n_games):
        obs, _ = env.reset()
        state_key = obs_to_key(obs)
        while True:
            legal = [i for i, v in enumerate(obs) if v == EMPTY]
            action = epsilon_greedy(Q, state_key, legal, eps=0.0)   # greedy
            obs, reward, terminated, truncated, _ = env.step(action)
            state_key = obs_to_key(obs)
            if terminated or truncated:
                if reward > 0:
                    wins += 1
                elif reward < 0:
                    losses += 1
                else:
                    draws += 1
                break

    env.close()
    print(f"\nEvaluation over {n_games:,} games vs random opponent:")
    print(f"  Wins   : {wins:>6,}  ({wins/n_games*100:.1f}%)")
    print(f"  Draws  : {draws:>6,}  ({draws/n_games*100:.1f}%)")
    print(f"  Losses : {losses:>6,}  ({losses/n_games*100:.1f}%)")


# ─────────────────────────────────────────────
# 4.  Interactive play
# ─────────────────────────────────────────────

def play_vs_agent(Q: dict) -> None:
    env = TicTacToeEnv(render_mode="human")
    obs, _ = env.reset()
    print("You are O. Enter a number 1-9 to choose a cell.\n")
    env.render()

    while True:
        # Agent turn (X)
        legal = [i for i, v in enumerate(obs) if v == EMPTY]
        action = epsilon_greedy(Q, obs_to_key(obs), legal, eps=0.0)
        obs, reward, terminated, truncated, _ = env.step(action)
        env.render()

        if terminated or truncated:
            if reward > 0:
                print("Agent (X) wins!")
            elif reward < 0:
                print("You (O) win!")
            else:
                print("It's a draw!")
            break

        # Human turn (O)  — env already played O internally,
        # but here we want interactive input, so we bypass
        # the auto-opponent by directly writing to the board.
        # We undo the auto-opponent O move first.
        # Better: use a separate env mode for interactive play.
        print("Your move (1-9): ", end="")
        try:
            m = int(input()) - 1
        except ValueError:
            print("Invalid input, skipping.")
            continue

        # Write move directly (env already put a random O;
        # overwrite that cell if it's still empty, else find a free cell)
        human_legal = [i for i, v in enumerate(obs) if v == EMPTY]
        if m in human_legal:
            obs[m] = O
            env.board = obs.copy()
        else:
            print("Illegal move, picking random.")
            obs[random.choice(human_legal)] = O
            env.board = obs.copy()

        env.render()
        if env._is_terminal():
            w = env._winner()
            if w == O:
                print("You (O) win!")
            else:
                print("It's a draw!")
            break

    env.close()


# ─────────────────────────────────────────────
# 5.  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Training Q-learning agent …")
    Q = train_qlearning(episodes=200_000)
    print("Training complete.\n")

    evaluate(Q)

    again = input("\nPlay against the agent? (y/n): ").strip().lower()
    while again == "y":
        play_vs_agent(Q)
        again = input("Play again? (y/n): ").strip().lower()