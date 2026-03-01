"""
Atari Ms. Pac-Man demo using Gymnasium.

Install dependencies:
    pip install gymnasium[atari] autorom[accept-rom-license] pygame

Two modes:
    python pacman_demo.py          # random agent  (live window)
    python pacman_demo.py --record # saves an mp4 to ./recordings/
"""

'''
pip install gymnasium[atari] autorom[accept-rom-license] pygame
python pacman_demo.py --agent heuristic
'''

import argparse
import time
import ale_py
import gymnasium as gym

'''
# Train for 10,000 episodes (saves pacman_qtable.pkl automatically)
python pacman_qlearn.py --mode train

# Train longer for better results
python pacman_qlearn.py --mode train --episodes 50000

# Watch the trained agent play
python pacman_qlearn.py --mode watch
'''

# Register ALE environments with Gymnasium
gym.register_envs(ale_py)


# ─────────────────────────────────────────────────────────────
# Agents
# ─────────────────────────────────────────────────────────────

class RandomAgent:
    """Picks a random legal action every step."""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, obs, info=None):
        return self.action_space.sample()


class SimpleHeuristicAgent:
    """
    Very naive agent that avoids repeating the same action forever.
    Cycles through a fixed pattern: UP → RIGHT → DOWN → LEFT.
    Better than pure random against walls; still loses quickly.
    """
    ACTIONS = [1, 2, 3, 4]   # FIRE=1, UP=2, RIGHT=3, DOWN=4, LEFT=5 in ALE

    def __init__(self, action_space, switch_every=8):
        self.action_space = action_space
        self.switch_every = switch_every
        self._step = 0
        self._idx  = 0

    def act(self, obs, info=None):
        if self._step % self.switch_every == 0:
            self._idx = (self._idx + 1) % len(self.ACTIONS)
        self._step += 1
        return self.ACTIONS[self._idx]


# ─────────────────────────────────────────────────────────────
# Runner
# ─────────────────────────────────────────────────────────────

def run(agent_type="random", record=False, n_episodes=3, fps=30):
    env_id = "ALE/MsPacman-v5"

    # Wrap with RecordVideo if requested
    if record:
        import os
        base_env = gym.make(env_id, render_mode="rgb_array")
        env = gym.wrappers.RecordVideo(
            base_env,
            video_folder="./recordings",
            episode_trigger=lambda ep: True,   # record every episode
            name_prefix="pacman",
        )
        print("Recording to ./recordings/")
    else:
        env = gym.make(env_id, render_mode="human")

    # Pick agent
    if agent_type == "heuristic":
        agent = SimpleHeuristicAgent(env.action_space)
        print("Agent: SimpleHeuristic")
    else:
        agent = RandomAgent(env.action_space)
        print("Agent: Random")

    print(f"Action space : {env.action_space}")
    print(f"Obs shape    : {env.observation_space.shape}\n")

    total_rewards = []

    for ep in range(1, n_episodes + 1):
        obs, info = env.reset()
        ep_reward  = 0
        steps      = 0
        lives      = info.get("lives", "?")

        print(f"─── Episode {ep} ───")

        while True:
            action = agent.act(obs, info)
            obs, reward, terminated, truncated, info = env.step(action)

            ep_reward += reward
            steps     += 1

            # Slow down rendering so it's watchable
            if not record:
                time.sleep(1 / fps)

            if terminated or truncated:
                print(f"  Steps: {steps:>5}  |  Score: {ep_reward:>6.0f}  |  Lives left: {info.get('lives', '?')}")
                break

        total_rewards.append(ep_reward)

    print(f"\n{'─'*40}")
    print(f"Average score over {n_episodes} episodes: {sum(total_rewards)/len(total_rewards):.1f}")

    env.close()


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Atari Ms. Pac-Man demo")
    parser.add_argument("--agent",    choices=["random", "heuristic"], default="random")
    parser.add_argument("--record",   action="store_true", help="Save mp4 instead of live window")
    parser.add_argument("--episodes", type=int, default=3)
    parser.add_argument("--fps",      type=int, default=30)
    args = parser.parse_args()

    run(
        agent_type=args.agent,
        record=args.record,
        n_episodes=args.episodes,
        fps=args.fps,
    )
