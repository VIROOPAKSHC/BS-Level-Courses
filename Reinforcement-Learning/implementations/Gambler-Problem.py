# Author - Chekuri Viroopaksh
# Gambler Problem simulation - use of Value iteration

class Gambler:
    def __init__(self,ph=0.25):
        self.S = list(range(101))
        self.A = {s:list(range(1,min(s,100-s)+1)) for s in self.S}
        self.terminal = [0,100]
        self.ph = ph
        self.V = np.zeros(101)
        self.V[100] = 1
        self.policy = np.zeros(101)
    
    def value_iteration(self,delta=1,theta=1e-5,gamma=1):
       
        while True:
            delta = 0
            for s in self.S:
                if s in self.terminal:
                    continue
                v_initial = self.V[s]
                v = []
                for a in self.A[s]:
                    v_a=self.ph*(1+gamma*self.V[s+a])+(1-self.ph)*(gamma*self.V[s-a])
                    v.append(v_a)
                self.V[s] = max(v)
                delta = max(delta,abs(v_initial - self.V[s]))
            if delta<theta:
                break
        
        for s in self.S:
            if s in self.terminal:
                continue
            action_values = []
            for a in self.A[s]:
                win_state = s + a
                lose_state = s - a
                action_value = self.ph * (1 + gamma * self.V[win_state]) + (1 - self.ph) * (gamma * self.V[lose_state])
                action_values.append(action_value)
            self.policy[s] = self.A[s][np.argmax(action_values)]

        return self.V, self.policy

gambler_025 = Gambler(ph=0.25)
V_025, policy_025 = gambler_025.value_iteration()
print("Value Function for ph=0.25:\n", V_025)
print("Optimal Policy for ph=0.25:\n", policy_025)

