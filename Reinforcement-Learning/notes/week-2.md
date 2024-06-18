## Week-2

<b>Action at a Temporal Distance: </b>
<li>Here, there is no immediate feedback.</li>
<li>Learning an appropriate action at S<sub>1</sub> depends on actions at S<sub>2</sub> and S<sub>3</sub></li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/7fa4999d-a652-4eff-bedf-0b79c97af6a3)

<b>Full RL Framework</b>:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ac2e90ae-ba05-4648-aa2c-a7f1f50f9fd2)

<li>Learning through interacting within a stochastic environment via actions that modify the state.</li>
<li>This close interaction helps in learning with a goal to maximize a measure of long term performance.</li>
<li>There's also rewards(+ve and -ve) associated with the results of the action on the environment.</li>
<br>
<b>Full RL Problem: </b>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/a09e1734-a5c9-4833-948f-89f2d4044ec1)

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/dfd86817-4f14-4fb4-aff8-4b3b16852918)

<li>The idea is to use prediction as surrogate feedback.</li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/85dfdc2d-09bc-41af-b0dd-0c8556d12eef)

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/6610bf8e-3ef8-4acc-bfa8-444704fd1049)

### Markov Decision Processes:
<b>The Agent-Environment Interface: </b>

Agent and environment interact at discrete time steps: t = 0,1,2,.... <br>
Agent observes state at step t: s<sub>t</sub> &isin; S <br>
Produces action at step t: a<sub>t</sub> &isin; A(s<sub>t</sub>) <br>
Gets resulting reward: r<sub>t+1</sub> &isin; R <br>
and resulting next state: s<sub>t+1</sub> <br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/c1e0d3cb-be60-4da2-9f9d-b72f9b6e1f0d)

<b>The Markov Property: </b>
<li>The state at step t, means whatever information is available to the agent at step t about its environment.</li>
<li>The state can include immediate "sensations", highly processed sensations, and structures built up over time from sequences of sensations.</li>
<li>Ideally, a state should summarize past sensations so as to retain all "essential" information, i.e, it should have the markov property:</li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/25e974f0-670e-4a5b-9c80-36386d24f160)

<b> Markov Decision Processes: </b>
<li>MDP, M, is the tuple: M = <S,A,p,r> </li>
<li>S: set of states<br>
A: set of actions<br>
p: S x A x S -> [0,1]: probability of transition<br>
r: S x A x S -> R: expected reward</li>
<li>Policy: &pi;:S x A -> [0,1] (May/May not deterministic)</li>
<li>Maximize total expected reward</li>
<li>Learn an optimal policy.</li>

<b>Designing an RL Solution: </b>
<li>States - Enough info to take decisions.</li>
<li>Actions - Control variables, discrete - items to recommend, continuous - torque to a motor</li>
<li>Rewards - Based on the goal</li>

<br>
<em>Example - 2-D Workspace: </em>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/c9013e80-84c8-44fd-bdbe-522fab0db8bc)

At every position you can choose to move in any of the directions (N,NE,E,SE,S,SW,W,NW) Reward for reaching the goal square G is +10. <br>

If there isn't any other condition, the agent might take a path of however length to reach G and can still end up getting the Reward +10. Now, if there is a constraint saying it can still movie in all the directions and reward to moving every non-goal square is -1. Now, as the agent's goal to maximize the reward comes into play, it takes the path as diagonal as possible learving the blocked squares. <br>

<em>Example - 2 </em>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/f189ab83-0ad8-40f8-be3d-6413c50dcbd4)

Here, there are 2 actions/choices that can be made = {advertise, ~advertise, research, ~research }<br>
Different states are = {hot,cold}<br>
And, actions applicable in each state are:<br>
A(hot) = {advertise, ~advertise}<br>
A(cold) = {research, ~research}<br>
<br>
Finally, consider the transition probabilities and rewards.<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/b62a12ee-5a4e-4a8f-ba75-917f55f8e7e3)

<em>Example - 3: Robot Control</em>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/09e3f4d2-d23b-4d03-8ec8-5ab90158d5f9)

<br>

