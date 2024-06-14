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
