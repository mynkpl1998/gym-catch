# Catch

A custom gym environment designed quickly evaluate Reinforcement learning algorithms. 

# Installation
```
git clone 
cd 
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
