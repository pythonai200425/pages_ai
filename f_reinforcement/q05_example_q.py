import random

states = ["EMPTY", "ROCK", "PAPER", "SCISSORS"]
actions = ["ROCK", "PAPER", "SCISSORS"]

# Q-table: Q[s][a] is a number now (not sum/count)
Q = {s: {a: 0.0 for a in actions} for s in states}

def reward(my_action, opp_action):
    if my_action == opp_action:
        return 0
    if (
        (my_action == "ROCK" and opp_action == "SCISSORS") or
        (my_action == "PAPER" and opp_action == "ROCK") or
        (my_action == "SCISSORS" and opp_action == "PAPER")
    ):
        return 1
    return -1

gamma = 1.0
alpha = 0.3
epsilon = 0.1

def eps_greedy(state):
    if random.random() < epsilon:
        return random.choice(actions)
    best = max(Q[state].values())
    best_actions = [a for a in actions if Q[state][a] == best]
    return random.choice(best_actions)

for episode in range(10000):
    # STEP 1: agent acts from EMPTY
    s0 = "EMPTY"
    a0 = eps_greedy(s0)          # my action
    r0 = 0

    # STEP 2: opponent acts (environment)
    s1 = a0                      # state after my action
    a1 = random.choice(actions)  # opponent action (random)
    r1 = reward(a0, a1)

    # --- Update state1 (terminal after opponent plays) ---
    # Q(s1,a1) <- Q(s1,a1) + alpha * (r1 - Q(s1,a1))
    Q[s1][a1] = Q[s1][a1] + alpha * (r1 - Q[s1][a1])

    # --- Update state0 using the value of what actually happened in step 2 ---
    # target for s0 is: r0 + gamma * Q(s1, a1)   (uses the sampled next action)
    target0 = r0 + gamma * Q[s1][a1]
    Q[s0][a0] = Q[s0][a0] + alpha * (target0 - Q[s0][a0])

print("\nQ-table values:\n")
for s in states:
    print(s)
    for a in actions:
        print(f"  {a}: {Q[s][a]:.2f}")
