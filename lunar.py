import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

# Create the environment and wrap it with DummyVecEnv
def make_env():
    return gym.make('LunarLander-v2', render_mode='human')

# Wrap the environment
env = DummyVecEnv([make_env])

# Load the model
model_path = "D:\\S7\\reinforment\\lunar_lander_model.zip"
model = PPO.load(model_path, env=env)

# Number of episodes to run
episodes = 5

# Run the environment
for ep in range(episodes):
    obs = env.reset()  # Reset the environment
    done = False
    while not done:
        action, _states = model.predict(obs)  # Predict the action
        obs, reward, done, info = env.step(action)  # Step in the environment
        env.render()  # Render the environment
        print(f"Reward: {reward}")

env.close()  # Close the environment
