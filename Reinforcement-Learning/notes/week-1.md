## Week-1

<b>Learning to Control:</b> Learning through evaluation not instruction. Trial and Error method by
the agent to learn a correct way to do things. This is Reinforcement learning.
E.g. Walk, Talk etc. <br>

<b>Reinforcement Learning :</b> A trial-and-error learning paradigm through Rewards and Punishments (Negative Rewards).
Learn about a system through interaction, inspider by Behavioural Psychology. <br>

<b>Pavlov's dog:</b>
This is an example to demonstrate Reinforcement Learning. Ivan Pavlov, an experimental neurologist and physiologist is also known
through this experiment of the power of conditioning. 
<li>Initially, whenever food was shown to the dog, it starts panting as it is getting its body ready for digestion.</li>
<li>Now, to see how it reacts it was shown a bell ringing, as expected it did not react in anyway.</li>
<li>For a few times, the dog was shown food after ringing a bell.</li>
<li>Now, the next time when the bell rang, the dog immediately got itself ready for food by PANTING. Which did not happen earlier.</li>
<br>
The demonstration of the Pavlov's dog experiment is intended to show that the dog acted according to its conditioning earlier 
as it thought it shall be fed after the bell rang as it happened earlier.<br>
<br>
<em>A joke from the dog's perspective is, as soon as the dog starts panting, Pavlov used to take notes of its behaviour given the environment and situation. Hence, the dog thought that
he can make Pavlov write in his book simply by PANTING</em>
<br>

Why Reinforcement Learning?
<li>Works in learning Complex Dynamics - Helicopter control, Humanoid control.</li>
<li>Learns the ability to work in Complex Workspace.</li>
<li>Stochastic Sensing and actuation - Visual Attention(Manipulation Task)</li>
<li>Human-in-the-loop learning</li>
<li>Cognitively motivated learning</li>
<li>Customization/Personalization - Ads for each user displayed in websites, Recommendations.</li>
<li>Going beyond human knowledge - learn through self-play.</li>
<br>
<b>History of successes in RL:</b>
<li>TD-Gammon beats the best human backgammon player in 1995. Learnt completeley through self-play. New moves are not recorded by humans in centuries of play.</li>
<li>Also, playing Arcade games [DeepMind's Atari Player] - learnt to play from video input, learnt from scratch. A complex neural network has been utilized to solve this, was considered one of the hardest
learning problems solved by a computer. AlphaGo Master - defeated the 18-time World Champion 4-1.</li> 
<li>AI bot won across DoTA championships against top players in the world.</li>
<li>AlphaZero : A general AI algorithm that can win any game, trained from scratch RL by playing against itself.</li>
<li>Reduced Google Data Centre Cooling bill by 40%. AlphaFold - solved Protein Folding, one of the hardest problems in Biology. An AI agent achieved 25% improvement
over best human effort and several other applications. </li>
<br>
<b>Tic-Tac-Toe:</b>
- Learned through evaluation by Reinforcement learning. <br>
- Win gives 1 point<br>
- Loss gives -1 point<br>
- Draw gives 0 points<br>
- Learn from repeated play<br>
<br>
* Use of MENACE - Michie and Chambers'60 for training.<br>
<br>
A Game Tree can be drawn for every move that expands till the final result, assuming an imperfect opponent - he sometimes makes mistakes.<br>
<b>Temporal Difference:</b>
<li>Simple Rule to explain complex behaviors.</li>
<li>Prediction of outcome at time T+1 is better than the prediction at time t. Hence, use the later prediction to adjust the earlier prediction.</li>
<li>Has also had profound impact in behavioural psychology and neuroscience.</li>
<br>
<em>Examples of TD in the brain: </em>
<br><br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/97ebf32c-acb0-47e0-a9de-d0cecd3a71a5)

<br>Example of Dopamine.
<br><br>
<b>Deep Reinforcement Learning- Goal: Omnivorous learning - consume any information to learn, as closer to humans as possible.</b>
<br><br>
<b>Immediate Reinforcement: </b>The payoff accrues immediately after an action is chosen. But there is a <b>dilemma</b> between exploration and exploitation. Bandit problems encapsulate "Explore vs Exploit".
<br><br>
<b>Explore-Exploit Dilemma: </b>
Explore to find profitable actions and exploit to act according to the best observations already made. Choosing to do only one is not optimal hence the dilemma.<br>
<br>
<b>Multi-Arm Bandits:</b>
N-arm bandit problem is to learn to preferentially select a particular action/arm from a set of n actions (1,2,...n)
Each selection results in Rewards derived from a respective probab distribution.<br><br>
Arm i has a reward distribution with mean &mu;<sub>i</sub> and <br>
&mu;<sup>*</sup> = max {&mu;<sub>i</sub>}<br>
The maximum possible mean is the best possible action.<br><br>

### Traditional Approaches:

Let r<sub>i,k</sub> be the reward acquired when i<sup>th</sup> arm is selected for the k<sup>th</sup> time.<br>
Define<br>
Q<sub>k+1</sub>(a<sub>i</sub>) = Q<sub>k</sub>(a<sub>i</sub>) + &alpha;(r<sub>i,k</sub> - Q<sub>k</sub>(a<sub>i</sub>))
<br><br>
Q(a<sup>*</sup>) = max<sub>i</sub> { Q(a<sub>i</sub>) }
<br><br>
Setting: &alpha; = 1/(k<sub>i</sub>+1) yields the sampling average.<br><br>
<b>Notation:</b>
<li>Q(a<sub>i</sub>) is called the expected reward for the action i.</li>
<li>Q(a<sup>*</sup>) is the maximum possible expected average for an action among the available actions/arm.</li>
<li>a<sup>*</sup> is the optimal action to be taken.</li>
<li>Q<sub>k</sub>(a<sub>i</sub>) is expected reward for taking the action a<sub>i</sub> at time k.</li>
<li>k<sub>i</sub> is the number of times the action a<sub>i</sub> has been selected till time k.</li>
<li>r<sub>i,k</sub> is the reward for taking the action a<sub>i</sub> at time k.</li> 
<br>
<br>

<b>Epsilon Greedy: </b> Select arm a<sup>*</sup> = argmax<sub>i</sub> { Q<sub>k</sub> ( a<sub>i</sub> ) } with probability 1-&epsilon; and select any arbitary arm with probability &epsilon;<br>
<br>
<b>Softmax: </b> Select arms with probability proportional to the current value estimates<br>
&pi;<sub>k</sub>(a<sub>i</sub>) = exp(Q<sub>k</sub>(a<sub>i</sub>)/&tau;) / &Sigma;<sub>j</sub> exp(Q<sub>k</sub>(a<sub>j</sub>)/&tau;)
<br> Here, the &tau; is the temperature.
<br>
Asymptotic Convergence is guaranteed.<br>

<b>&epsilon;-Greedy Example:</b> a 10-arm bandit problem.

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/6017a712-0f9c-47f5-a3ef-05bf809551d8)

<br><br>
<b>Objectives</b>
<li>Identify the correct arm eventually.</li>
<li>Maximize the total rewards obtained or Minimize regret(=loss) while learning.</li>
Regret = Optimal Payoff - Current Payoff(selected by the algorithm currently) across time.<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/b82d23dd-6468-482f-84c9-43b8f08afc78)

<b>Probably Approximately Correct frameworks (PAC) </b>:
<li>Identification of an &epsilon;-optimal arm with probability of 1-&delta;</li>
<li>&epsilon;-Optimal: Mean of the selected arm satisfies. &mu; > &mu;<sup>i</sup> - &epsilon;</li>
<li>Minimize sample complexity: Order of samples required for such an arm identification.</li>
<br>
<b>Other approaches:</b>
<li>Median Elimination - Round Based Algos</li>
<li>Upper Confidence Bounds(UCB) - Optimize Regret</li>
<li>Thompson Sampling - Optimize Regret</li>
<br>
<b>UCB (Upper Confidence Bounds): </b>
<li>The arm with the best estimate r<sup>*</sup> so far serves as a benchmark and other arms are played only if the upper bound of a suitable confidence interval is at least r<sup>i</sup></li>
<li>Simplest approach - Be greedy with respect to upper confidence bounds.</li>
<li>Suboptimal arm j played fewer than (8/&Delta;<sub>j</sub>) ln n times, where &Delta;<sub>j</sub> = &mu;<sup>*</sup> - &mu;<sub>j</sub> : Further improvements focus on reducing the constants.</li>
<br>
<b>Algorithm:</b><br>
Intialization: Play each machine once <br>
max{ Q<sub>k</sub> (a<sub>j</sub>) + square_root ( 2 ln n<sub>k</sub> / n<sub>k,j</sub>), where n<sub>k</sub> total number of time steps and n<sub>k,j</sub> is the number of times a<sub>j</sub> has been taken till time step k.<br>
<br>
<br>
<b>Contextual Bandits:</b>
<li>Different ads for different users - One bandit for each user!</li>
<li>Hard to train - need several rounds of experience with the same user</li>
<li>Assume that the parameters of the reward distributions themselves are determined by a set of hyperparameters - Typical assumption is a linear parameterization of the expectation.</li>
<li>Assume that each user is represented by a set of features - can be joint features of user and arm.</li>
<li>The "statistic" used for choosing arms is now dependent on these features.</li>
<li>Could correspond to the presence/absence of different signals.</li>
<br>
<b>LinUCB :</b>
<li>One of the more popular contextual bandit algorithms.</li>
<li>Predicted expected reward assumed to be a linear function of the features - Ridge regression to fit params, can derive upper confidence bounds for the regression fit, use UCB like action selection. </li>
<br>
