# Author - Chekuri Viroopaksh
# Implementation of Non-stationary scenario of K-Bandit problem with 2 different selection strategies.
import numpy as np
import matplotlib.pyplot as plt

def k_bandit_simulation(time_step=1000,epsilon=0.1,k=10,method='sample_average',alpha=None):
    """
    Function to run a simulation of k-bandit problem
    Allows multiple selection strategies for non-stationary k-bandit scenario
    method parameter can be 'sample_average' or 'constatnt-step-size'
    """
    # Empty Placeholders for rewards and optimal actions over different timesteps
    total_rewards = np.zeros(time_step)
    optimal_actions = np.zeros(time_step)
    
    for _ in range(2000):
        q_star = np.random.normal(0,1,10)
        Q = np.zeros(k)
        N = np.zeros(k)
        rewards = np.zeros(time_step)
        actions = np.zeros(time_step)
        
        for t in range(time_step):
            
            q_star += np.random.normal(0,0.01,10) # Non-stationary problems - random walk
            
            if np.random.random() < epsilon:
                A = np.random.randint(k)
            else:
                A = np.argmax(Q)
            
            actions[t] = (A==np.argmax(q_star))

            R = np.random.normal(q_star[A],1)
            N[A] = N[A] + 1
            if method=='constant-step-size':
                Q[A] = Q[A] + alpha*(R-Q[A]) # Uses constant alpha parameter instead of 1/N[A] as for sample_average method
            else:
                Q[A] = Q[A] + (1/N[A]) * (R - Q[A])
            rewards[t] = R
            
        total_rewards += rewards
        optimal_actions += actions

    average_rewards = total_rewards/2000
    average_actions = (optimal_actions/20)
    return average_rewards,average_actions

avg_rewards_sample,avg_actions_sample = k_bandit_simulation(time_step=10000)
avg_rewards_non_stat,avg_actions_non_stat = k_bandit_simulation(time_step=10000,method='constant-step-size',alpha=0.1)

plt.title("Optimal Actions Percentage vs Time steps")
plt.plot(range(time_step),avg_actions_sample)
plt.plot(range(time_step),avg_actions_non_stat)
plt.xlabel("time step")
plt.ylabel("Optimal action percentage")
plt.legend(['epsilon=0.1','constant step size alpha=0.1'])
plt.show()

plt.title("Average Reward vs time step")
plt.xlabel("time step")
plt.ylabel("Average reward")
plt.plot(range(time_step),avg_rewards_sample)
plt.plot(range(time_step),avg_rewards_non_stat)
plt.legend(['epsilon=0.1','constant step size alpha=0.1'])
plt.show()
