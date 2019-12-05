import gym
import gym_catch
import imageio
import time
import numpy as np


def rollout():
    env = gym.make("catch-v0", render=True, kFrames=1)
    frames = []
    state = env.reset().reshape(80, 80)
    frames.append(state)
    #print(frames[0].shape)
    
    while True:
        state, reward, done, info = env.step(env.action_space.sample())
        state = state.reshape(80, 80)
        frames.append(state)
        if done:
            break
    #imageio.mimsave("video.gif", frames)

if __name__ == "__main__":
    rollout()