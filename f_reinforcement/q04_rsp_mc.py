import random

states = ["EMPTY", "ROCK", "PAPER", "SCISSORS"]
actions = ["ROCK", "PAPER", "SCISSORS"]

# Q-table: store [sum_of_returns, count]
Q = {
    s: {a: {"sum": 0, "count": 0} for a in actions}
    for s in states
}

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

gamma = 1  # change to 0 to see the difference

for episode in range(10000):
    # STEP 1: empty board → agent chooses
    state0 = "EMPTY"
    my_action = random.choice(actions)
    r0 = 0

    # STEP 2: opponent chooses
    state1 = my_action
    opp_action = random.choice(actions)
    r1 = reward(my_action, opp_action)

    # Monte Carlo returns
    G0 = r0 + gamma * r1
    G1 = r1

    # Update EMPTY → my action
    Q[state0][my_action]["sum"] += G0
    Q[state0][my_action]["count"] += 1

    # Update after-my-move → opponent action
    Q[state1][opp_action]["sum"] += G1
    Q[state1][opp_action]["count"] += 1

# Print averages
print("\nQ-table averages:\n")
for s in states:
    print(s)
    for a in actions:
        entry = Q[s][a]
        if entry["count"] > 0:
            avg = entry["sum"] / entry["count"]
            print(f"  {a}: {avg:.2f}")
        else:
            print(f"  {a}: None")
