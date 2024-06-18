### Week-2

<b>Dominance: </b>
An action(a) for a player(i) strictly dominates action (b) if 'a' leads to better outcomes than 'b' for the player(i) no matter what other players are doing. Here, (b) is strictly dominated by (a). An action (a) for the player (i) is called strict dominant action if 'a' strictly dominates all other actions of the player (i). <br>
Actions are the same as Strategy in normal games. <br>
<b>Strictly Dominant Strategy Equilibrium:</b>
A strictly dominant strategy equilibrium is an action profile where each player's action is strictly dominant. In Prisoner's dilemma both the players' strictly dominant strategy is to choose Confess.
<br>
Good News: Our actions are to follow the strictly dominant strategy and no need to worry about the other's strategy.<br>
Similarly, Weakly dominant strategy equilibrium can be defined as the pay-offs not strictly greater than but greater than or equal to.
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/895860aa-e1a1-4c96-b5c2-9c4419dee54a)

### IESDS and IEWDS: 
<b>Iterated Elimination of Strictly dominated strategies: </b> <br>

In the first step, at most one dominated strategy is removed from the strategy space of each of the players since no rational player would ever play these strategies. This results in a new, smaller game. Some strategies—that were not dominated before—may be dominated in the smaller game. The first step is repeated, creating a new even smaller game, and so on. The process stops when no dominated strategy is found for any player. This process is valid since it is assumed that rationality among players is common knowledge, that is, each player knows that the rest of the players are rational, and each player knows that the rest of the players know that he knows that the rest of the players are rational, and so on ad infinitum

<br>
<em> Example: 1 - Consider the following tabular matrix and eliminate the strictly dominated strategies.</em>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/f96d11a2-e291-4373-8983-cd6f17c1389a)

From the above image the elimination goes as follows:
<ol>
  <li>Comparing M,R of player 2 - M > R - R column eliminated</li>
  <li>Comparing U,D of player 1 - U > D - D row eliminated</li>
  <li>Comparing remaining action pairs - (U, L) and (U,M) - U,M is the dominant strategy - (U,L) is eliminated</li>
</ol>

The best outcome is - (U,M)
<br><br>
Similarly, <b>IEWDS - Iterated Elimination of Weakly dominated strategies:</b>
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/7ce7309a-51f4-4904-8856-c9b011e4041c)

From the table above the order of elimination is:
<ol>
  <li>Store-A Action-High row eliminated</li>
  <li>Store-B Action-High column eliminated</li>
  <li>Store-A Action-Low row eliminated</li>
  <li>Store-B Action-Low column eliminated</li>
</ol>

Final strategy is - (Match,Match)
<br>

<b>Dominance Solvable: </b>
Iterated dominance: remove (strictly/weakly) dominated strategy, repeat. If iterated elimination of dominated strategies leads to all but one action for each player, the game is called a dominance-solvable game. <br>

<br>
<em>Iterated weak dominance strategy is path-dependent while Iterated strict dominance is path-independet meaning the elimination process will always terminate at the same point.</em>
<br>

<b> Nash Equilibrium: </b>
<br>
By utlizing the concept of optimization, it can be understood as the optimal state in which the actions of both the players are optimal according to each and even if given a chance, they would not want to modify their actions. <br>
<br>
${a_i^* \in argmax U_i(a_i,a_i*)}$ where a<sup>*</sup><sub>i</sub> is the optimal action of the player-i.<br>
<br>
This is called the Best Response of a<sub>i</sub> given the actions of the remaining players. <br>

<b> Nash Equilibrium in a 2 Player game: </b>
<br>
In a two-player game, an action profile 
${ a_1^* , a_2^* }$ 
is a Nash Equilibrium if 
${ a_1^* }$
is best response of player 1 to player 2's
${ a_2^* }$
and 
${ a_2^* }$
is best response to player 1's
${ a_1^* }$
<br>
These are obtained by applying the argmax function to the pay-off matrix. 
<br>

<b>Definition of Nash Equilibrium: </b>
A set of actions, one action for each player, constitute the Nash Equilibrium if no player can benefit by changing her action unilaterally (while other players keep their actions unchanged)

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/a3d26009-4c6f-4407-b3a2-1a8ca8d3c058)

<em>Battle of Sexex problem - example</em>
<table>
  <tr>
    <td> </td>
    <td>M</td>
    <td>C</td>
  </tr>
  <tr>
    <td>M</td>
    <td>(1,2)</td>
    <td>(0,0)</td>
  </tr>
  <tr>
    <td>C</td>
    <td>(0,0)</td>
    <td>(2,1)</td>
  </tr>
</table>
<br>
Here, both the statest (M,M) and (C,C) are equilibria.
<br>
<em>Stag Hunt game - Example</em>
<table>
  <tr>
    <td> </td>
    <td>Stag</td>
    <td>Rabbit</td>
  </tr>
  <tr>
    <td>Stag</td>
    <td>(8,8)</td>
    <td>(0,4)</td>
  </tr>
  <tr>
    <td>Rabbit</td>
    <td>(4,0)</td>
    <td>(2,2)</td>
  </tr>
</table>
<br>
Here, both the (S,S) and (R,R) are equilibria.
<br>
<em>Hawk and Dove Game/The game of chicken: </em>
<table>
  <tr>
    <td> </td>
    <td>Hawk</td>
    <td>Dove</td>
  </tr>
  <tr>
    <td>Hawk</td>
    <td>((V-C)/2,(V-C)/2)</td>
    <td>(V,0)</td>
  </tr>
  <tr>
    <td>Dove</td>
    <td>(0,V)</td>
    <td>(V/2,V/2)</td>
  </tr>
</table>
Here, as C>0, V>0 and if C>V then (V-C)/2 < 0, hence V>C.
Nash Equilibria would be => (Dove, Hawk) and (Hawk, Dove) <br>
<br>
<b>Nash Parables (Prajit Dutta): </b>
<li>Play Prescription.</li>
<li>Pre-play communication.</li>
<li>Rational Introspection.</li>
<li>Focal Point.</li>
<li>Trial and Error</li>
<br>
<em>Analogy - seats at Paradox IITM and payoff is the value of the feeling felt based on the other's sitting/standing position.</em>
<br>
<br>
<b>Bress's Paradox - Modelling the Network as a game: </b>
<br>
Consider the destination reaching problem where there are 4000 carss and 2 possible paths that can be taken by the drivers. The payoff for a driver is the negative of time taken. <br>
Time taken: <br>
A-C = (X/100) <br>
C-B = 45<br>
A-D = 45<br>
D-B = (X/100)<br>
Now the distances to B from A, through ACB and ADB is the same = 45 + (X/100) <br>
Hence, now to optimize and findout the Nash Equilibirum. The NE is when there are 2000 drivers on ACB and 2000 drivers on ADB. The cost for taking there routes is :<br>
ACB = (2000/100) + 145 = 65 <br>
ADB = 45 + (2000/100) = 65 <br><br>
And, if any of the drivers take the other road the cost would become = 2001/100 + 45 = 65.01 which is not a desirable for the drivers and hence the equilibrium is not disturbed.<br>
<br>
<b> Now a minor modification the game - </b> If a new path of cost 0 is added between C and D then?<br>
Now the idea of drivers to reduce the time speed acts at either of the sides and points: <br>
If 4000 drivers ride the road of cost X/1000 then it would cost each of them 40, while the other option is 45. Hence, every driver chooses this and now because of 0 cost between CD, 4000 cars take the AC path as it is lesser costly than AD, and now after reaching C, CB is 45 and taking CDB is only 40. Now, the total cost between AB increasing the total cost to 80 while the calculated cost earlier was 65. <br>

<br>
<em> The above case is almost a replica of several real-life scenarios where adding a new bridge only increased/worsened traffic.</em>
<br><br>

<b>Another problems called the Location problem and Cournot competition have also been discussed. </b>
