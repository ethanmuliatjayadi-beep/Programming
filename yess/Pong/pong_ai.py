import gymnasium as gym
# Updated imports for newer Gymnasium versions
from gymnasium.wrappers.atari_preprocessing import AtariPreprocessing
from gymnasium.wrappers.frame_stack import FrameStack

# 1. CREATE the environment first
env = gym.make("ALE/Pong-v5")

# 2. APPLY the wrappers to the environment you just created
env = AtariPreprocessing(env, screen_size=84, grayscale_obs=True, frame_skip=4, scale_obs=True)
env = FrameStack(env, num_stack=4)

# Now this will work!
num_actions = env.action_space.n
print(f"Number of possible actions: {num_actions}")