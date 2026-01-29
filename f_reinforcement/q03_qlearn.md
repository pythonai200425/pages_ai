# Q-Learning — Rock 🟡 Paper 📄 Scissors ✂️

## 1️⃣ What is Q-Learning?

Q-learning is a way of learning **while the game is still running**

Instead of waiting for the end, the agent:

* Makes a move
* Gets feedback
* Learns immediately
* Moves on

Think of it like this:

> “I’ll adjust my thinking step by step as I go”

## 2️⃣ Big idea: learning from guesses

Q-learning does **not** wait for the final result

It uses:

* What just happened (reward now)
* What it *thinks* will happen next (current knowledge)

So Q-learning learns from **estimates**, not certainty

That’s the key difference from Monte Carlo

## 3️⃣ Q-table (same memory, different usage)

Q-learning uses the **same Q-table** as Monte Carlo

The table still answers:

> “If I am in this situation and take this action, how good is it?”

The difference is:

* Monte Carlo writes after the game ends
* Q-learning writes **during the game**

## 4️⃣ One-step update (very important)

In Q-learning:

* Only **ONE cell** is updated at a time
* The current (state, action)
* No going back over the whole path

Learning spreads backward **slowly**, over many games

## 5️⃣ How a single update works (human version)

When the agent:

1. Is in a state
2. Chooses an action
3. Gets a reward
4. Moves to a new state

It thinks:

> “Was this better or worse than I expected, considering what usually happens next?”

Then it nudges the current Q-table value slightly

## 6️⃣ Example: learning during a game

Path:

A → B → C → D → WIN (+1)

Q-learning updates like this:

* At A → update A
* At B → update B
* At C → update C
* At D → update D

Each update uses:

* Reward now
* Best guess about the future

No waiting for the end

## 7️⃣ Gamma (γ) in Q-learning

Gamma controls **how much the future matters**

* Low gamma:

  * Focus on immediate reward
  * Short memory

* High gamma:

  * Future reward matters
  * Long memory

Gamma does **not** choose actions
It only affects how values are updated

## 8️⃣ Epsilon (ε) in Q-learning

Epsilon controls **how actions are chosen**

* High epsilon:

  * Random actions
  * Exploration

* Low epsilon:

  * Choose best-known action
  * Exploitation

Epsilon does **not** affect learning math
It only affects behavior

## 9️⃣ Why Q-learning works

Even though early guesses are bad:

* The agent keeps correcting itself
* Good paths get reinforced
* Bad paths fade away

Learning happens gradually, not instantly

## 🔟 When Q-learning is a good choice

Q-learning is great when:

* Games are long
* Rewards are delayed
* You want faster learning
* Waiting for the end is expensive

Q-learning is harder to understand
But very powerful

## 🔒 Final brain-friendly summary 🧠

* Q-learning learns **during the game**
* It updates **one step at a time**
* It learns from **guesses + correction**
* Gamma = how much the future matters
* Epsilon = curiosity vs confidence

Q-learning is basically:

> Try → Adjust → Try again → Adjust again → Improve
