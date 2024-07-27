import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

# Create the environment and wrap it with DummyVecEnv
def make_env():
    return gym.make('LunarLander-v2')

env = DummyVecEnv([make_env])

# Initialize the model
model = PPO("MlpPolicy", env, verbose=1, n_steps=2048, batch_size=64, learning_rate=0.0003, gamma=0.99, gae_lambda=0.95)

# Train the model
model.learn(total_timesteps=500000)  # Adjust the number of timesteps as needed

# Save the model
model.save("lunar_lander_model")
