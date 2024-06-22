import numpy as np
import matplotlib.pyplot as plt

def k_bandit_simulation_Gradients(time_step=1000,alpha=0.1,k=10,baseline=4):
    """
    Bandit gradients
    """

    total_rewards = np.zeros(time_step)
    optimal_actions = np.zeros(time_step)

    for _ in range(2000):

        q_star = np.random.normal(baseline,1,k)
        H = np.zeros(k)
        rewards = np.zeros(time_step)
        actions = np.zeros(time_step)
        Rewards = []

        for t in range(time_step):
            Pi = np.exp(H)/np.sum(np.exp(H))
            A = np.random.choice(np.arange(k), p=Pi)
            
            actions[t] = (A==np.argmax(q_star))

            R = np.random.normal(q_star[A],1)
            Rewards.append(R)
            if t > 0:
                avg_reward = np.mean(Rewards)
            else:
                avg_reward = 0
            
            for a in range(k):
                if a==A:
                    H[A] = H[A] + alpha * (R - avg_reward) * (1-Pi[A])
                    continue

                H[a] = H[a] - alpha*(R-avg_reward) * (Pi[a])
            
            rewards[t] = R
            
        total_rewards += rewards
        optimal_actions += actions

    average_rewards = total_rewards/2000
    average_actions = (optimal_actions/20)
    return average_rewards,average_actions


avg_rewards_grads,avg_actions_grads = k_bandit_simulation_Gradients(time_step=1000)
plt.title("Optimal action percentage vs time step")
plt.xlabel("time step")
plt.ylabel('Optimal action percentage')
plt.plot(range(1000),avg_actions_grads)
plt.show()

