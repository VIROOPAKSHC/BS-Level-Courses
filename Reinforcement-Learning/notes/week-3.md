## Week-3

<b>Bellman Equation for a policy &pi; </b>
<br>

${ v_\pi (s) = \Sigma_a \pi (a|s) \Sigma_{s',r} p (s',r | s, a) [ r+ \gamma v_\pi (s') ], \forall s \in S}$
<br>
<li>Linear Equation in |S| variables.</li>
<li>Unique solution exists.</li>
Derived by expanding the function initially. <br>
<br>
<em>Example:
<br>
  <li>Actions: norht, south, east, west: deterministic.</li>
  <li>If the action takes the agent off the grid: no move but reward=-1</li>
  <li>Other actions produce reward = 0, except actions that move agent out of special states A and B as shown.</li>
  <li>The special states give rewards of +10, +5 in A,B. Any action you take in A,B moves you to A', B' respectively and gives you reward.</li>


![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/184b04f6-40cc-41e1-bd1e-b25c938b3013)

<li>State-value function for equiprobable random policy; &gamma; = 0.9</li>
<li>The values in the boxes of the matrix have been assigned after the solving linear equations of value functions or solving in iterative fashion.</li>
  
</em>

<b>Optimal Value Functions:</b>
<br>
For finite MDPs, policies can be partially ordered: &pi; &ge; &pi;' iff v<sub>&pi;</sub>(s) &ge; v<sub>&pi;'</sub> (s) &forall; s &isin; S <br>
<br>
There is always at least one (and possibly many) policies that is better than or equal to all the others. This is an optimal policy. We denote them all &pi;<sub>*</sub>. <br>
Optimal policies share the same optimal state-value function:
<br>

${ v_* ( s ) = max_\pi v_\pi ( s ) \forall s \in S }$

${ q_* (s,a) = max_\pi q_\pi (s,a) \forall s \in S, a \in A }$

<br>
