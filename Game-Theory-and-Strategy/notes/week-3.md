## Week-3

### Relation between Nash Equilibrium and Dominance: 

<b>Dominant Strategy Equilibrium and Nash Equilibrium: </b>
<li>Any game has at most one Dominant Strategy Equilibrium.</li>
<li>If a<sup>*</sup> is a Dominant strategy equilibrium, then it is a Nash Equilibrium.</li>
<li>If a<sup>*</sup> is a Nash Equilibrium, then it is not necessarily a Dominant Strategy Equilibrium.</li>

<br>

### IESDS, IEWDS and NE relationship:
<li>If a<sup>*</sup> is a Nash Equilibrium, it doesn't get eliminated by IESDS.</li>
<li>If a<sup>*</sup> is the only action profile that survives IESDS/IEWDS, it is an NE, in fact, in case of IESDS, a unique NE.</li>
<li>A NE can get eliminated by IEWDS.</li>

<br>
<b>Finding a Nash Equilibrium: </b>
<ol>
  <li>Nash Equilibrium, where each player has a Dominant Strategy.</li>
  <li>Nash Equilibrium, by eliminating Dominated Strategy.</li>
  <li>Nash Equilibrium through Best Responses.</li>
</ol>
<br>

### Mixed Strategy Nash Equilibrium:

A game that doesn't have pure action Nash Equilibrium <br><br>
<table>
  <tr>
    <td> </td>
    <td>A</td>
    <td>B</td>
  </tr>
  <tr>
    <td>A</td>
    <td>(5,12)</td>
    <td>(8,9)</td>
  </tr>
  <tr>
    <td>B</td>
    <td>(6,7)</td>
    <td>(7,8)</td>
  </tr>
</table>
<br>
<b>Two Zero-Sum Games: </b>
1. Rock, Paper, Scissors: Two players with hand gestures representing - rock, paper and scissors. <br>
<br>
<table>
  <tr>
    <td> </td>
    <td>R</td>
    <td>P</td>
    <td>S</td>
  </tr>
  <tr>
    <td>R</td>
    <td>(0,0)</td>
    <td>(-1,1)</td>
    <td>(1,-1)</td>
  </tr>
  <tr>
    <td>P</td>
    <td>(1,-1)</td>
    <td>(0,0)</td>
    <td>(-1,1)</td>
  </tr>
  <tr>
    <td>S</td>
    <td>(-1,1)</td>
    <td>(1,-1)</td>
    <td>(0,0)</td>
  </tr>
</table>

<br>
2. Matching Pennies : A Zero Sum game: <br>
If pennies match (both heads or both tails), player 1 gets to keep both pennies, otherwise player 2 gets to keep both pennies. <br>
<br>
<table>
  <tr>
    <td> </td>
    <td>Head</td>
    <td>Tail</td>
  </tr>
  <tr>
    <td>Head</td>
    <td>(1,-1)</td>
    <td>(-1,1)</td>
  </tr>
  <tr>
    <td>Tail</td>
    <td>(-1,1)</td>
    <td>(1,-1)</td>
  </tr>
</table>
<br>
<b>What is the way forward?</b>
<li>Extend the concept of Actions/Strategies - New terminology</li>
<li>Pure Action Strategy - deterministic</li>
<li>Mixed Action Strategy - Probabilistic approach, derived from set of pure actions.</li>
Pure actions are special cases of mixed strategies.<br>

<b>Mixed Strategies: </b>
<li>For each player take a set of pure actions A.</li>
<li>Assign to each member of A, a probability p that it will be played</li>
<li>Example - Player has 2 choices U,D. Now we have probabilities of playing actions - p1,p2. Now the action instead of U,D pure becomes p1*U + p2*D</li>
<li>Enables a "convexification" of the problem</li>
<li>Good Thing - New candidates for equilibrium, perhaps some nice results.</li>
<li>Bad - How to interpret the equilibrium?</li>

<br>

<b>Obtaining Mixed Strategy Nash Equilibrium: </b>
Consider the above Matching Pennies game but with added probabilities to each player. Player 1 plays Head with probability p and Tail with probability 1-p. 
Similarly, Player 2 plays Head with probability q and Tail with probability 1-q. <br>
Now the matrix becomes:<br><br>
<table>
  <tr>
    <td> </td>
    <td>Head</td>
    <td>Tail</td>
    <td>Expected Payoff</td>
  </tr>
  <tr>
    <td>Head</td>
    <td>(1,-1)</td>
    <td>(-1,1)</td>
    <td>2q-1</td>
  </tr>
  <tr>
    <td>Tail</td>
    <td>(-1,1)</td>
    <td>(1,-1)</td>
    <td>1-2q</td>
  </tr>
  <tr>
    <td>Expected Payoff</td>
    <td>1-2p</td>
    <td>2p-1</td>
    <td>1</td>
  </tr>
</table>
<br>
Now, lets apply <b> Best Response Correspondence: </b><br>
BR<sub>1</sub>(q) => solve 2q-1 > 1-2q => then he should play Heads. Soluton => q > 1/2 Player 1 should play Heads.
Now if the inequality is reversed then, q < 1/2, then Player 1 has to play Tails.<br>
Hence, BR<sub>1</sub>(q) = {<br>
                              H if q > 1/2 <br>
                              T if q < 1/2 <br>
                              {H,T} if q=1/2 <br>
                            }<br>
       BR<sub>1</sub>(p) = {<br>
                            p=1 if q>1/2,<br>
                            p=0 if q<1/2,<br>
                            p &isin; [0,1] q = 1/2<br>
                            }<br>
Here, any combination of H,T would also be a best response if q=1/2 because, the total payoff would become 0 for Player 1. <br>
Similarly, BR<sub>2</sub>(p) = {<br>
                              H if p < 1/2<br>
                              T if p > 1/2<br>
                              {H,T} if p=1/2<br>
                            }<br>
              OR<br>
          BR<sub>2</sub>(p) = {<br>
                            q=1 if p<1/2,<br>
                            q=0 if p>1/2,<br>
                            q &isin; [0,1] p = 1/2<br>
                            }<br>
<br>

Now, <br>

${ P^* , Q^*  = P^* \in BR_1 ( Q^* ), Q^* \in BR_2 ( P^* ) }$
<br>

In the above case p=1/2 and q=1/2 are the only choices to obtain a Nash Equilibrium by confirming that each other are the Best Responses of each other given their current actions. <br>
<br>
Graphically it can be done like this:
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/9d5a5f24-1e71-4d18-8e77-d4a5c3dbab35)

The orange part represents the BR_2 function and blue part represents the BR_1 function. <br>

<b>Characteristics of Mixed Strategy Nash Equilibrium: </b>
Definition: For each player i,

${ U_i ( \alpha^* ) \ge U_i (a_i, \alpha^*_{-i} ) }$ 

, for every mixed strategy profile &alpha;<sub>i</sub> of player i, where U<sub>i</sub>(&alpha;<sup>*</sup>) is the player i's expected payoff to the mixed strategy profile &alpha;
<br>
<b>Characteristics:</b>
<li>If player - i is mixing, multiple actions x,y,z and only x,y are involved in a Nash Equilibrium, then U<sub>i</sub>(x,&alpha;<sup>*</sup><sub>-i</sub> = U<sub>i</sub>(y, &alpha;<sup>*</sup><sub>-i</sub></li>
<li>The action z that is not involved in Nash Equilibrium cannot have greater payoff compared to those involved in NE.</li>
<br>

<b>Nash Theorem: </b>
<li>Every strategic game in which players are having finite number of strategies has a mixed strategy Nash Equilibrium</li>
<li>Reassuring but not helpful in finding equilibria.</li>
<li>Finiteness sufficient but not a necessary criterion.</li>
<br>

<b>Mixed Strategy Nash Equilibrium - Battle of Sexes: </b>
<table>
  <tr>
    <td> </td>
    <td>Action Movie</td>
    <td>Romantic Movie</td>
  </tr>
  <tr>
    <td>Action Movie</td>
    <td>(3,1)</td>
    <td>(0,0)</td>
  </tr>
  <tr>
    <td>Romantic Movie</td>
    <td>(0,0)</td>
    <td>(1,3)</td>
  </tr>
</table>
Player - 2 probabs are q,1-q and Player - 1 probabs are p,1-p respectively. <br>
Player 1's payoff = P.Q.3 + P.(1-Q).0 + Q.(1-P).0 + (1-P).(1-Q).1 = 1-Q + P ( 4Q - 1 ) <br>
Similarly, Player 2's payoff = 3 - 3.P + Q.(4.P-3) <br>
<br>

By differentiating both the equations of Payoff and obtaining the values for best response functions, the following is the graph:<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/f0c4128d-3b6c-4bf3-9b76-e48b2e90f97b)

<b>Reporting a Crime Problem: </b>
Consider a crime has occured in a locality and has been witnessed by N people. According to Social Psychology none of the witnesses
are going to call the police - indifference to one's neighbour and his troubles to the conditioned reflex of life that nobody reports and I should
not report are the reasons. But consider this case in the form of Game Theory.<br>
In such a situation, everybody wants to have the crime reported and gets a pay-off(satisfaction) of V, but 
when an individual would like to report they would incur a cost of (C) causing the payoff if they have to report the crime to become = V-C,
however, the satisfaction is mental and V>>C. Hence if 2 people are considered the following is the pay-off matrix,
considering that N,R are their actions where N is not reporting and R is reporting.
<table>
  <tr>
    <td> </td>
    <td>N</td>
    <td>R</td>
  </tr>
  <tr>
    <td>N</td>
    <td>(0,0)</td>
    <td>(V,V-C)</td>
  </tr>
  <tr>
    <td>R</td>
    <td>(V-C,V)</td>
    <td>(V-C,V-C)</td>
  </tr>
</table>
<br>
Now, if we consider pure strategy actions then Nash Equilibrium = (N,R), (R,N), which means that
both the persons are relying on the other to for the crime to be reported which is a symmetric solution.
But, symmetric solutions are for games where each player is doing the exact same thing, and in this game everyone
is not doing the same thing. Hence, this is not a solution.<br><br>
Now, consider mixed strategy actions for Nash Equilibrium: <br>
Player-1 Performs actions N,R with probabilities P,1-P and Player-2 performs actions N,R with probabilities Q,1-Q respectively:
<br>
<br>
U_i is the function to get the payoff of player-i given his action and the actions of remaining players.<br>
U<sub>1</sub>(N,Q) = the payoff of player-1 for action N, when Player-2 acts stochastically with probability Q<br><br>
U<sub>1</sub>(N,Q) = payoff of (N,N) x probab of player-2 selecting N + payoff of (N,R) x probab of player-2 selecting R = 0x(Q) + Vx(1-Q) = V(1-Q) <br>
U<sub>1</sub>(R,Q) = payoff of (R,N) x probab of player-2 selecting N + payoff of (R,R) x probab of player-2 selecting R = (V-C)x(Q) + (V-C)x(1-Q) = V-C<br>
If V-C > V(1-Q) => perform R => 1-p = 1 => p = 0<br>
Solving that, Q > C/V, P = 0 <br>
and Q < C/V, P = 1<br>
and Q = C/V, P &isin; [0,1] <br>
<br>
<br>
Graphically: <br><br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/3cb7d466-4f19-43d0-9b53-7ef381cad3c7)

Solution is to take (C/V, 1 - C/V) => Symmetric Nash Equilibrium. <br>
<br>
Now, extending this solution to N people, consider that player-i just plays N, while others play N,R with probabilities p, 1-p and
there are 2 possible cases:<br>
atleast one among n-1 reports + none of them reports.<br>
Converting them into probabilities:<br>
Pr(atleast one among n-1 reports) * (V) + Pr(none of them reports) * (0); <br>
Now, this is equal to the probability of Player-i reporting and costing him V-C. <br>
Pr(atleast one among remaining n-1 report)* V = Pr(player-i reporting) * (V-C)<br>
Pr(atleast one among remaining n-1 reporting) = 1 - Pr(no one reporting) = 1 - (1-p)<sup>n-1</sup> <br>
<br>
(1-(1-p)<sup>n-1</sup>) * V = 1 * (V-C) <br>
p = 1 - (C/V)<sup>1/(n-1)</sup> <br>
therefore as n incrases, p increases <br>. So if there are more people in the area, the chance of reporting increases.<br>
<br>
