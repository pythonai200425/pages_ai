# pip install gymnasium stable-baselines3
from stable_baselines3 import DQN
# pip install gymnasium
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random
from collections import defaultdict

EMPTY, X, O = 0, 1, -1

# -------------------------
# Gym Env: single-agent (X) vs random opponent (O)
# -------------------------
class TicTacToeEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(9)  # pick a cell 0..8
        # board values: -1, 0, 1  (O, empty, X)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(9,), dtype=np.int8)
        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.zeros(9, dtype=np.int8)
        return self.state.copy(), {}

    def legal_moves(self, s=None):
        s = self.state if s is None else s
        return [i for i in range(9) if s[i] == EMPTY]

    def _winner(self, s):
        lines = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in lines:
            if s[a] != EMPTY and s[a] == s[b] == s[c]:
                return int(s[a])  # 1 (X) or -1 (O)
        return 0

    def _terminal(self, s):
        return self._winner(s) != 0 or EMPTY not in s

    def step(self, action):
        # invalid move -> strong penalty + end
        if action not in self.legal_moves():
            return self.state.copy(), -1.0, True, False, {"invalid": True}

        # agent move (X)
        self.state[action] = X

        # if ended after agent
        if self._terminal(self.state):
            w = self._winner(self.state)
            r = 1.0 if w == X else 0.0  # win=+1, draw=0
            return self.state.copy(), r, True, False, {}

        # opponent move (random O)
        opp_action = random.choice(self.legal_moves())
        self.state[opp_action] = O

        # if ended after opponent
        if self._terminal(self.state):
            w = self._winner(self.state)
            r = -1.0 if w == O else 0.0  # loss=-1, draw=0
            return self.state.copy(), r, True, False, {}

        # game continues
        return self.state.copy(), 0.0, False, False, {}

    def render(self):
        symbols = {X: "X", O: "O", EMPTY: "."}
        s = [symbols[int(v)] for v in self.state]
        print("\n".join([" ".join(s[i:i+3]) for i in range(0, 9, 3)]))
        print()




env = TicTacToeEnv()              # your gym env (step/reset already coded)

model = DQN("MlpPolicy", env, verbose=0,
            learning_rate=1e-3, buffer_size=50_000,
            exploration_fraction=0.3, exploration_final_eps=0.05)

model.learn(total_timesteps=1_000)   # <-- automation: SB3 runs the training loop
model.save("tictactoe_dqn")

obs, _ = env.reset()
while True:
    action, _ = model.predict(obs, deterministic=True)
    obs, r, done, trunc, info = env.step(int(action))
    if done or trunc: break
print("final reward:", r)
