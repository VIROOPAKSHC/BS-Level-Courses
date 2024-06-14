## Week-1: Game Theory and Strategy

<b> Decision Making: </b>
<li>Different alternatvives are encountered.</li>
<li>Each alternative might lead to unique outcomes.</li>
<li>Preferences might be defined over the set of outcomes.</li>
<li>These preferences follow Completeness and Transitivity.</li>
<br>
Notation: a > b - a is preferred over b, similarly for a < b. a ~ b means that both choices are equally preferred.
<br>

### Game Theory as Multi-Person Decision Theory:

<em> Example : A scenario of multiple persons going to a restaurant and selecting items to choose over menu. And cost is split between the two of you. The alternatives and associated values and prices remain the same. </em>

There are 2 options: Cheap food: Value-1000 and Price-500 and Expensive food: Value-2500 and Price-3000. Let's Denote as C , E.

<ol>4 Possible scenarios:
<li>C,C - Total will be 500+500 and the division among each will be (500,500). Now the payoff will be (1000(actual value eated)-500(paid amount),1000-500) = (500,500)</li>
<li>C,E - Total will be 500+3000 = (1750,1750), payoff = (1000-1750,2500-1750) = (-750,750)</li>
<li>E,C - Reverse of the above scenario - (750,-750)</li>
<li>E,E - 3000+3000 = (3000,3000), payoff = (2500-3000,2500-3000) = (-500,-500)</li>
</ol>
<br>
Tabular Form/Strategic Form Representation - This can be represented using a matrix with rows and columns as C,E both but rows represents first person selection, and columns represent second person selection.<br>
<br>
<b>What is a Game? -  Strategic interactions </b> in which the outcome for each agent depends on not only her action but also the choices made by others.
<br><br>
<em>Example 1: Traffic Problem : Consider there are 2 options in traffic - F , D [ following the rule or do not follow the rule respectively ]. Now the following are the 4 possible scenarios represented in tabular form:</em>
<table>
  <tr>
    <th> </th>
    <th>Others - F</th>
    <th>Others - D</th>
  </tr>
  <tr>
    <td>You - F</td>
    <td>(3,3)</td>
    <td>(0,4)</td>
  </tr>
  <tr>
    <td>You - D</td>
    <td>(4,0)</td>
    <td>(-1,-1)</td>
  </tr>
</table>
Now, considering the scenarios the most profitable scenario for you is to <b>D</b> when others are <b>F</b> because it gives you a payoff of 4 which is the highest.
<br><br>
<em>Example 2: Braess's Paradox : Conider there are 4000 automated cars that want to reach a destination B and are starting from A. There are 2 available paths to reach B from A which are - <b>A-C-B</b> or <b>A-D-B</b>. Now the cost of AC = 45 and CB = X/100 (X - number of cars on CB. And the cost of AD = X / 100 (X - number of cars on AD) and DB = 45.</em>
Now, N = {1,2,....4000} and each A<sub>i</sub> = {ACB,ADB} i &isin; N. <br>
The payoff = -time-taken. So for ACB = -[45 + X<sub>ACB</sub>/100] similarly for ADB.
<br><br>
<em>Example 3: Adverse Selection : Firm A ("the acquirer") is considering taking over firm T ("the target"). It does not know firm T's value; it believes that this value, when firm T is controlled by its own management, is at least $0 and at most $100, and assigns equal probability to each of the 101 dollar values in this range. Firm T will be worth 50% more under firm A's management than it is under its own management. Suppose that firm A bids y to take over firm T, and firm T is worth x(under its own management). Then if T accepts A's offer, A's payoff is 1.5x - y, and T's payoff is y; if T rejects A's offer, A's payoff is 0, and T's payoff is x. Should A acquire T?</em>

Drawing a table like above can help make a good decision.
<br><br>

<b> Game Classifications: </b> Sequential and Simultaneous.<br>
In Simultaneous games, nobody is already aware of the decisions of others. In Sequential games, players are aware of the earlier decisions taken by other players, in this setting we can see the game progress and can draw a Game Tree. <br>
Simultaneous - Static Setting<br>
Sequential - Dynamic Setting<br>
<br>
```
Types of Games:
│   
│       
│
└───Co-operative games 
│   │   
│   │    Transferable Utility   
│   │   Non-transferable utility
│   
└───Non-cooperative games
    │   Complete Information
    │   Incomplete Information
```
<br>
<table>
  <tr>
    <th> </th>
    <th>Complete Information</th>
    <th>Incomplete Information</th>
  </tr>
  <tr>
    <td>Static</td>
    <td>Normal Form game with complete information.</td>
    <td>Normal Form game with Incomplete information.</td>
  </tr>
  <tr>
    <td>
      Dynamic
    </td>
    <td>Extensive form game with complete information</td>
    <td>Extensive form game with incomplete information (This is not discussed in this course.)</td>
  </tr>
</table>
<br>
<b>Terminology in a strategic environment:</b>
<li>Players: Everyone who affects decision makers' earnings.</li>
<li>Actions: Actions available to each player.</li>
<li>Payoffs or Preferences: Number associated with each outcome. Reflect the interests of the players.</li>
<li></li>
<br>
<b>Prisoner's Dilemma: </b> There have been a crime and the police have arrested 2 possible suspects for the crime and are investigating them independently in different cell rooms without each knowing what the other said. The police have given them an offer if they confess what they know and the prisoner's already know what happens if they nobody confesses (minimal punishment of 1 year for each). The police offered to let them walk away if they confess the crime is committed by the other, while the other gets 20 years jail. Now the prisoners are the players in this game with possible choices - C,D (confess and do not respectively).If both of them confess then 5 years of jail punishment for each.
<br>
Strategic Form representation:
<table>
  <tr>
    <th> </th>
    <th>Suspect 2 - C</th>
    <th>Suspect 2 - D</th>
  </tr>
  <tr>
    <td>Supect 1 - C</td>
    <td>(-5,-5)</td>
    <td>(0,-20)</td>
  </tr>
  <tr>
    <td>Suspect 2 - D</td>
    <td>(-20,0)</td>
    <td>(-1,-1)</td>
  </tr>
</table>

<br>
<b>Formal Characterization of the game:</b>
<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>Set of Players</td>
    <td>P1,P2</td>
  </tr>
  <tr>
    <td>Set of Actions for Each player</td>
    <td>A<sub>1</sub>={C,D}, A<sub>2</sub>={C,D}</td>
  </tr>
  <tr>
    <td>Set of Rules</td>
    <td>Choose either C or D simultaneously</td>
  </tr>
  <tr>
    <td>Set of Outcomes</td>
    <td>O = {(C,C), (C,D), (D,C), (D,D)}</td>
  </tr>
  <tr>
    <td>Payoff</td>
    <td>U<sub>1</sub>(o), U<sub>2</sub>(o)</td>
  </tr>
</table>
<br>
<b>How are the rules for a game defined?</b>
<br>
<li>Timing of the moves: Are they simultaneous or sequential?</li>
<li>Nature of conflict of resolution: Will players interact once or repeatedly?</li>
<li>Informational Conditions : Are some players better informed?</li>
<li>Enforceability of Agreement: Can contracts be enforced?</li>
<br>
<br>
Consider there's an Acquirer(A) and a target (T). The Target puts a price of $ 50 on the item A is trying to acquire and A can only give bids of $ 25 multiples. As A acquires T its value increases by 50% - 1.5 * X = 75. Now is a <b>complete information game</b> because we know how the game progress:
<table>
  <tr>
    <td>Reply to the Offer -> </td>
    <td>Yes</td>
    <td>No</td>
  </tr>
  <tr>
    <td>Bidding Amount</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0</td>
    <td>(75,0)</td>
    <td>(0,50)</td>
  </tr>
  <tr>
    <td>25</td>
    <td>(50,25)</td>
    <td>(0,50)</td>
  </tr>
  <tr>
    <td>50</td>
    <td>(25,50)</td>
    <td>(0,50)</td>
  </tr>
  <tr>
    <td>75</td>
    <td>(0,75)</td>
    <td>(0,50)</td>
  </tr>
</table>

<br>
<br>
Now if the T does not know if he is sure of giving it at $ 50 or $ 100 with probability of 1/2 each, then it becomes an <b>incomplete information game</b> because now there is not a single certain game being played. The above tables comes with a probability of 1/2 and there's going to be another table with a probability of 1/2
<br>

<b>Incomplete Information game:</b> when there exists a player who is not certain about which game is being played.
<br> Acquirer's idea about the value comes from a probability distribution over possible value.
<br>
<b>Dominant, Dominate and Dominated Actions:</b>
An action(a) from player (i) dominates action (b) if 'a' leads to better outcomes than 'b' for player(i) no matter what other players are doing. Here, (b) is dominated by (a). An action(a) for player (i) is called a dominant action if 'a' dominates all other actions of player (i).
<br>
From our above Prisoner's Dilemama game: it appears to be better for the second person to confess whatever might be the action of the first person because it is the best action. Hence, Confess is a dominant strategy for the second person. 
<br>
<br>
<b>Pure Action vs Mixed action :</b>
A mixed action is a probability distribution over that player's pure actions. <br>
<em>Consider the following example to understand Pure action and mixed action:</em>
<table>
  <tr>
    <th> </th>
    <th>2nd player - L</th>
    <th>2nd player - R</th>
  </tr>
  <tr>
    <td>1st player - U</td>
    <td>(3,2)</td>
    <td>(0,5)</td>
  </tr>
  <tr>
    <td>1st player - M</td>
    <td>(0,5)</td>
    <td>(3,2)</td>
  </tr>
  <tr>
    <td>1st player - D</td>
    <td>(1,1)</td>
    <td>(1,1)</td>
  </tr>
</table>
<br>
If you consider every single action of 1st player U,M,D then individually they aren't dominant over others. But if you consider a mixed action:
{(1/2)U + (1/2)M} = U with a probab of 1/2 and M with a probab of 1/2 has a total payoff of 1.5 inboth L and R actions of the 2nd player. This is higher than 1 in both cases and now {(1/2)U + (1/2)M} is a dominant action. <br>
<br>
<b>Delection Action Profile:</b>
<li>Action Profile: Writing actions of all the player - (a1,a2,a3,...an)</li>
<li>Deleted Action: Instead of writing every action which is cumbersome, read the important action of the ith player, it is moved to the front. - (ai,a1,a2,....,an)</li>
<br>
<b>Weakly and Strictly Dominant Action: </b>
In the following case: U dominated action D of player 1 in only a single action of player 2 while the payoff in the second case is same, hence it is dominant too but weakly.<br>
<table> 
  <tr>
    <td></td>
    <td>L</td>
    <td>R</td>
  </tr>
  <tr>
    <td>U</td>
    <td>(1,0)</td>
    <td>(0,0)</td>
  </tr>
  <tr>
    <td>D</td>
    <td>(0,0)</td>
    <td>(0,0)</td>
  </tr>
</table>
<br>
<b> Formal Definition: </b> A strictly dominant strategy is U<sub>i</sub>(a<sub>i</sub>,a<sub>-i</sub>) > U<sub>i</sub>(a<sup>'</sup><sub>i</sub>, a<sub>-i</sub>) &forall; a<sub>-i</sub>.
In the case of weakly dominant strategy it is &ge; instead of strictly greater.
<br>
<br>
### Differences in Game theory:
<b>Cooperative Game Theory: </b> Coalition formation to coordinate their actions. Making Binding agreements and Pooling their winnings.<br>
<b>Natural Questions in Cooperative Game Theory :</b>Which coalition will form? How do we distribute the gain/cost?<br>
<b>Assumptions: </b> Rational Behaviour. Unlimited Communication. Unlimited ability to make a binding agreement.<br>
<b>Goal in these types:</b> To characterize the set of possible coalition that may emerge.
<br><br>
In the non-cooperative games:
A detailed model of the situation, focus on procedure and May/May not have conflicting goals.
<br>
<b>Natural Questions: </b> What would be the outcome of this interaction?<br>
<b>Assumptions:</b> Rational Behavior. <br>
<b>Goal in these types:</b> To obtain outcome.<br>

<br>
<b>Solving the Game: </b>
What does it mean? We impose some restriction that is acceptable by the players to move forward in the game. Which is also called an <b>Equilibrium</b>
<br>
<b>Equilibrium</b> State of balance when all the forces are balanced. A state that doesn't change on its own. Or a state where neither of the players do not want to change their actions after taken ( given a chance they would not like to change their actions also called no regret )
<br>
From the prisoner's dilemma: if the first player chooses to C and second player chooses to D then later if given a chance D would like to choose C instead of D because he would have a better payoff that way. This is not an equilibrium. However, if both choose C then no one would want to improve and that is an equilibrium because no one is interested in modifying to increase their payoffs.<br><br>
Even if D,D is chosen, if given a chance the second player or the first player would want to change to D,C or C,D because they would be able to increase their payoff from -1 to 0 each. Hence this is not an equilibrium too.<br>
Only equilibrium in that situation is to choose C,C and this is also called <b>Nash Equilibrium.</b>
<br>
<b>Assumptions:</b>
Rationality - players are perfect in decision-making : able to compare choices, consistent in decision-making, maximize their pay-offs, perfect recall and perfect calculators.
<br>
Common Knowledge - I know "X", Everyone knows "X", All players know "x", All know that all know "X", and so on...
