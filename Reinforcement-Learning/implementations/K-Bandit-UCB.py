# Author - Chekuri Viroopaksh
# UCB strategy selection in K-Bandit problems.
import numpy as np
import matplotlib.pyplot as plt

def k_bandit_simulation_ucb(time_step=1000,epsilon=0.1,k=10,c=2):
    """
    UCB Algorithm for arm selection strategy
    """
    total_rewards = np.zeros(time_step)
    optimal_actions = np.zeros(time_step)
  
    for _ in range(2000):
        q_star = np.random.normal(0,1,10)
        Q = np.zeros(k)
        N = np.zeros(k)
        rewards = np.zeros(time_step)
        actions = np.zeros(time_step)
        
        for t in range(time_step):
            # Initially all arms are selected
            # Upper bound criterion after initial time steps.
            if t<k:
                A = t
            else:
                A = np.argmax(Q+c*np.sqrt(np.log(t)/N))

            actions[t] = (A==np.argmax(q_star))
            R = np.random.normal(q_star[A],1)
            N[A] = N[A] + 1
            Q[A] = Q[A] + (1/N[A]) * (R - Q[A])
            rewards[t] = R
            
        total_rewards += rewards
        optimal_actions += actions

    average_rewards = total_rewards/2000
    average_actions = (optimal_actions/20)
    return average_rewards,average_actions

avg_rewards_ucb,avg_actions_ucb = k_bandit_simulation_ucb(time_step=10000)
plt.title("Average rewards vs time step")
plt.xlabel("time step")
plt.ylabel("Average rewards")
plt.plot(range(10000),avg_rewards_ucb)
plt.show()

plt.title("Optimal actions percentage vs time step")
plt.xlabel("time step")
plt.ylabel("Optimal action percentage")
plt.plot(range(10000),avg_actions_ucb)
plt.show()
