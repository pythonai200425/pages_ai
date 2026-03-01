# Gymnasium Explained: Environment Functions and How to Train an Agent

This page explains:

1. What Gymnasium is
2. What functions exist inside an environment
3. What each function receives and returns
4. How to train an agent using Gym

---

# 1) What is Gymnasium?

Gymnasium is a standard API for Reinforcement Learning environments.

It defines a simple communication protocol between:

* The **Agent** (your Q-learning / policy / neural network)
* The **Environment** (the world / game / simulator)

The interaction loop is always:

Agent chooses action → Environment responds with next state + reward

---

# 2) The Core Environment Structure

Every Gym environment is a class that inherits from `gym.Env`.

Minimal structure:

```python
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class MyEnv(gym.Env):

    def __init__(self):
        super().__init__()

        # Define action space
        self.action_space = spaces.Discrete(3)

        # Define observation space
        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self, *, seed=None, options=None):
        ...

    def step(self, action):
        ...
```

Now let's understand each part.

---

# 3) action_space

Defines what actions the agent is allowed to take.

### spaces.Discrete(n)

```python
self.action_space = spaces.Discrete(3)
```

**Discrete(3)** means:

The agent can choose exactly ONE integer from:

```
0, 1, 2
```

That’s it.

So:

* Discrete(2) → actions: 0 or 1
* Discrete(3) → actions: 0,1,2
* Discrete(9) → actions: 0..8

It represents a **finite set of separate choices**.

Typical examples:

* Left / Right → Discrete(2)
* Rock / Paper / Scissors → Discrete(3)
* TicTacToe cells → Discrete(9)

Important:

```python
action = env.action_space.sample()
```

This randomly samples one valid integer action.

---

# 4) observation_space

Defines what the state looks like.

### spaces.Box(...)

```python
self.observation_space = spaces.Box(
    low=0,
    high=1,
    shape=(4,),
    dtype=np.float32
)
```

**Box** means:

The state is a continuous numeric vector inside a range.

Let’s break it down:

* `low=0` → minimum value allowed
* `high=1` → maximum value allowed
* `shape=(4,)` → state has 4 numbers
* `dtype=np.float32` → numbers are floats

So this defines a state like:

```
[0.2, 0.7, 0.0, 1.0]
```

Each element must be between 0 and 1.

Box represents a **continuous space**, not discrete choices.

Typical examples:

* Cart position, velocity, angle → Box
* Image pixels → Box
* Sensor readings → Box

---

### Discrete vs Box (Core Difference)

Discrete → one choice from fixed integers

Box → vector of real numbers inside a range

Discrete is used for:

* finite actions
* categorical states

Box is used for:

* continuous values
* numeric vectors
* images

---

# 5) reset()

()

Called at the start of every episode.

Signature:

```python
def reset(self, *, seed=None, options=None):
```

What it should do:

* Reset internal variables
* Initialize state
* Return the first observation

Return value:

```python
observation, info
```

Example:

```python
def reset(self, *, seed=None, options=None):
    super().reset(seed=seed)
    self.state = np.zeros(4)
    return self.state, {}
```

---

# 6) step(action)

This is the most important function.

Signature:

```python
def step(self, action):
```

Input:

* `action` chosen by the agent

What it must do:

1. Apply the action
2. Update internal state
3. Compute reward
4. Check if episode ended

Return value (5 items):

```python
observation, reward, terminated, truncated, info
```

Explanation:

* `observation` → next state
* `reward` → immediate reward (float)
* `terminated` → True if episode ended naturally
* `truncated` → True if stopped due to time limit
* `info` → extra debug information (dict)

Example:

```python
def step(self, action):
    self.state = self.state + action

    reward = 1.0
    terminated = False
    truncated = False

    return self.state, reward, terminated, truncated, {}
```

---

# 7) The Agent–Environment Interaction Loop

This is the standard training loop skeleton:

```python
env = MyEnv()

for episode in range(1000):

    obs, _ = env.reset()
    done = False

    while not done:

        action = env.action_space.sample()  # replace with policy

        next_obs, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        obs = next_obs
```

This structure is always the same.

---

# 8) Training a Q-Learning Agent with Gym

Now we plug Q-learning into the loop.

Example (tabular Q-learning):

```python
from collections import defaultdict
import numpy as np

Q = defaultdict(float)
alpha = 0.1
gamma = 0.99
epsilon = 0.1

for episode in range(1000):

    obs, _ = env.reset()
    state = tuple(obs)

    done = False

    while not done:

        # epsilon-greedy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            q_values = [Q[(state, a)] for a in range(env.action_space.n)]
            action = int(np.argmax(q_values))

        next_obs, reward, terminated, truncated, _ = env.step(action)
        next_state = tuple(next_obs)

        done = terminated or truncated

        # Q update
        if done:
            target = reward
        else:
            next_q = max(Q[(next_state, a)] for a in range(env.action_space.n))
            target = reward + gamma * next_q

        Q[(state, action)] += alpha * (target - Q[(state, action)])

        state = next_state
```

Notice:

Gym does NOT change Q-learning.

It only standardizes how:

* we get states (`reset`, `step`)
* we apply actions
* we detect episode termination

---

# 9) Summary

Gymnasium environments must define:

* `action_space`
* `observation_space`
* `reset()`
* `step(action)`

The agent training loop always follows:

reset → loop(step) → until terminated or truncated

Once you understand that, any algorithm (Q-learning, DQN, PPO, etc.) fits inside this structure.
