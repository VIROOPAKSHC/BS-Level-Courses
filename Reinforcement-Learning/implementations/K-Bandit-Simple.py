# Author - Chekuri Viroopaksh
# Reinforcement Learning
# K - Arm bandit problems
import numpy as np
import matplotlib.pyplt as plt

time_step = 1000
epsilon = 0.1
k = 10
# Empty placeholders for storing total rewards and optimal actions over different timesteps in different problems
total_rewards = np.zeros(time_step) 
optimal_actions = np.zeros(time_step) 
num_prob = 2000

for _ in range(num_prob):
    # Generating num_prob different k-armed bandit problems.
    q_star = np.random.normal(0,1,10)
    Q = np.zeros(k)
    N = np.zeros(k)
    rewards = np.zeros(time_step)
    actions = np.zeros(time_step)
    for t in range(time_step):
        # exploration and exploitation
        if np.random.random() < epsilon:
            A = np.random.randint(k)
        else:
            A = np.argmax(Q)

        actions[t] = (A==np.argmax(q_star)) # Keeping track of the optimality of the action taken

        R = np.random.normal(q_star[A],1)
        N[A] = N[A] + 1
        Q[A] = Q[A] + (1/N[A]) * (R - Q[A])
        rewards[t] = R
        
    total_rewards += rewards
    optimal_actions += actions

average_rewards = total_rewards/2000
average_actions = (optimal_actions/20)

plt.title("Optimal Action percentage vs time steps")
plt.xlabel("time step")
plt.ylabel("Optimal action percentage")
plt.plot(range(time_step),average_actions)
plt.show()

plt.title("Average rewards vs time steps")
plt.xlabel("time step")
plt.ylabel("Average reward")
plt.plot(range(time_step),average_rewards)
plt.show()
