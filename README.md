# Catch

A custom gym environment designed to quickly evaluate Reinforcement learning algorithms.

<div align="center">
    <img src="images/resized.gif">
</div>

# Installation
```
git clone https://github.com/mynkpl1998/gym-catch.git
cd gym-catch 
pip install -e .
```

# How to use ?
```
import gym
import gym_catch
env = gym.make("catch-v0", render=True, fps=30, kFrames=1)

# Reset the environment
state = env.reset()

# Step through the environment
while True:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    if done:
        break
```

# Environment Properties
1. Observation space - Box(80, 80, 1)
2. Action space - Discrete(3)

