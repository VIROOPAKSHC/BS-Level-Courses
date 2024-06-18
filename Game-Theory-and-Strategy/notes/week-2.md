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
<b>Iterated Elimination of Strictly dominated strategies: </b>
Eliminate the strategies that are not strictly dominating by comparing the payoffs 2 actions of a player under every action of the other player.
This elimination might result in a pair of actions for both the players that is beneficial for both of them and no regret state.
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
