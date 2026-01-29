# Reinforcement Learning (RL) — Rock 🟡 Paper 📄 Scissors ✂️

## 1️⃣ What Reinforcement Learning even is?

Reinforcement Learning is a way to teach a computer **by experience**, not by rules

Think about a kid learning a game:

* The kid tries something
* The kid sees if it was good or bad
* The kid remembers what worked
* Next time, the kid tries to do better

That kid is called the **agent**

## 2️⃣ Our game: Rock Paper Scissors

The rules (simple life rules):

* 🟡 Rock beats ✂️ Scissors
* ✂️ Scissors beats 📄 Paper
* 📄 Paper beats 🟡 Rock

The agent plays against an opponent

## 3️⃣ Who is the agent?

The **agent** is the learner

In our case:

* The agent chooses one move: 🟡 / 📄 / ✂️
* The environment answers with a result

Possible results:

* Win → good 😄
* Lose → bad 😢
* Draw → meh 😐

## 4️⃣ Rewards (how the agent feels)

We convert feelings into numbers (computers love numbers)

* Win  → +1
* Draw →  0
* Lose → -1

This number is called the **reward**

## 5️⃣ What is a Q-table? (the heart of RL)

Q-table = the agent's **cheat sheet / memory**

It answers this question:

👉 "If I am in this situation and I do this action, how good is it?"

For Rock Paper Scissors, the table is tiny

States = what happened last round
Actions = what I choose now

Example (conceptual, not code):

* Last round was a WIN

  * If I play 🟡 → value 0.2
  * If I play 📄 → value 0.5
  * If I play ✂️ → value 0.1

Higher number = better idea

## 6️⃣ How the Q-table is updated (baby steps)

After each round:

1. Agent picks an action
2. Game gives a reward
3. Agent updates ONE number in the Q-table

Simple idea:

"Was this better or worse than I expected?"

Slow brain formula (no math panic):

new value = old value + small correction

That correction depends on reward and future hope

## 7️⃣ Gamma (γ) — thinking about the future

Gamma answers:

👉 "Do I care about future rewards or only NOW?"

* Gamma close to 0

  * I only care about this round
  * YOLO mindset

* Gamma close to 1

  * I care about winning in the long run
  * Chess brain 🧠

Typical value: **0.9**

## 8️⃣ Epsilon (ε) — curiosity vs confidence

Epsilon answers:

👉 "Should I try something random?"

* High epsilon (like 1.0)

  * Try random moves
  * Exploration phase 🧪

* Low epsilon (like 0.1)

  * Use what I already know
  * Exploitation phase 🎯

Training usually looks like:

* Start with high epsilon
* Slowly reduce it

## 9️⃣ Showing the score

We keep a score counter:

* Wins: +1
* Losses: -1
* Draws: 0

Total score shows:

👉 "Is the agent actually learning?"

If score goes up over many games → 🎉 success

## 🔟 Full learning loop (slow recap)

1. Agent looks at Q-table
2. Agent maybe explores (epsilon)
3. Agent chooses 🟡 / 📄 / ✂️
4. Game returns reward
5. Q-table is updated
6. Score is updated
7. Repeat MANY times

## Final brain-friendly summary 🧠

* Agent = learner
* Reward = feedback
* Q-table = memory
* Gamma = future thinking
* Epsilon = curiosity

Reinforcement Learning is literally:

> Try → Fail → Remember → Improve

