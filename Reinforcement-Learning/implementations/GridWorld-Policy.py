# Author - Chekuri Viroopaksh
# Code for simulation of Policy Evaluation, Policy Improvement and Policy Iteration on Grid World problem

terminal = [(0,0),(3,3)]
m,n=4,4
S = [(i,j) for i in range(m) for j in range(n)]
A = ['up','down','left','right']
gamma = 1
def transition(s,a,s_next):
    x,y = s
    s_dash = -1
    if a=='up':
        s_dash = (x-1,y) if x>=1 else (x,y)
    elif a == 'down':
        s_dash = (x+1,y) if x<m-1 else (x,y)
    elif a=='right':
        s_dash = (x,y+1) if y<n-1 else (x,y)
    else:
        s_dash = (x,y-1) if y>=1 else (x,y)
    
    prob = s_dash == s_next

    return prob, -1

pi = {s:{a:1/4 for a in A} for s in S}

def policy_evaluation(theta=1e-5,delta=1,pi={s:{a:1/4 for a in A} for s in S},gamma=1):
    # theta = 1e-5
    # delta = float('inf')
    V = {s:0 for s in S}
    iter = 0
    while delta >= theta:
        
        iter+=1
        delta = 0
        for s in S:
            if s in terminal:
                continue
            v = V[s]
            val = 0
            for a in A:
                pi_s_a = pi[s][a]
                in_sum=0
                for s_next in S:
                    prob,reward = transition(s,a,s_next)
                    in_sum+=prob*(reward+gamma*V[s_next])
                val += pi_s_a*in_sum
            V[s] = val
            delta = max(delta,abs(v-V[s]))
    return V

def policy_improvement(V, pi):
    iter = 0
    while True:
        iter += 1
        policy_stable = True
        pi_next = {s: {a: 0 for a in A} for s in S}
        for s in S:
            if s in terminal:
                continue
            q = {a: 0 for a in A}
            for a in A:
                for s_next in S:
                    prob, reward = transition(s, a, s_next)
                    q[a] += prob * (reward + gamma * V[s_next])
            best_action = max(q, key=q.get)
            for a in A:
                pi_next[s][a] = 1 if a == best_action else 0
            if pi_next[s] != pi[s]:
                policy_stable = False
        if policy_stable:
            break
        pi = pi_next.copy()
        V = policy_evaluation(pi=pi)
    return pi, iter

# Initial policy evaluation
V = policy_evaluation(pi=pi)

# Policy improvement
pi_next, iter = policy_improvement(V, pi)
print(f"Policy improved in {iter} iterations")
print(pi_next)

# Policy Iteration still not working perfectly at this point.
