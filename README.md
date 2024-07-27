# Lunar-Lander-PPO
This project uses Proximal Policy Optimization (PPO) to train an agent to land a lunar module on a simulated moon surface using OpenAI's Gym environment `LunarLander-v2`.

# Overview
This project is designed to explore and apply reinforcement learning (RL) techniques to solve the LunarLander-v2 environment provided by OpenAI's Gym. In this project, we use Proximal Policy Optimization (PPO), a popular RL algorithm from Stable Baselines3, to train an agent to successfully land a lunar module on a simulated moon surface.

#What is Reinforcement Learning?
Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties and uses this information to improve its decision-making process. RL is particularly suited for problems where the solution involves sequential decision-making and where the environment is complex and dynamic.

# Project Description
The Lunar Lander environment simulates the landing of a lunar module on a lunar surface. The agent's goal is to control the lunar module's thrusters to land safely while avoiding obstacles and managing fuel consumption. This project involves training an RL agent using PPO, a state-of-the-art algorithm that balances exploration and exploitation to find optimal policies.

# Files
# lunar.py
This file contains the core implementation of the PPO agent and its interaction with the LunarLander environment. It includes:

Environment Setup: Initializes the LunarLander-v2 environment and wraps it with DummyVecEnv to handle vectorized operations.
PPO Model Initialization: Configures and initializes the PPO model with specific hyperparameters.
Training: Trains the PPO model on the LunarLander-v2 environment using a specified number of timesteps.
Model Saving: Saves the trained model for future use and evaluation.

# trainlunar.py
This file demonstrates how to load a pre-trained PPO model and evaluate its performance on the LunarLander-v2 environment. It includes:

Environment Setup: Initializes the LunarLander-v2 environment and wraps it with DummyVecEnv.
Model Loading: Loads the previously trained PPO model.
Evaluation: Runs the environment using the trained model and renders the agent's actions in the environment.
Results Display: Prints the rewards obtained during each episode.



https://github.com/user-attachments/assets/f8ac4ad4-582d-4efe-a096-c8a6ea1c6418

