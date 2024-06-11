## Week-1
### This course is a follow-up to an Algorithms course. This week is a Refresher on Greedy Algorithms
<br>


  <b>The Problem of Storing Files on Tape:</b>
<li>We have n files that we want to store on a magnetic tape. Each file F<sub>i</sub> has a length of L<sub>i</sub>.</li>
<li>Cost of accessing a stored file<sub>i</sub> is &Sigma;<sup>i=j</sup><sub>i=0</sub>L<sub>i</sub> </li>
<br>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/1962aa37-9c3e-4eb3-a72b-78a51859214e)

<li>Expected cost of reading a random file:
  
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/98303168-eadb-4dc4-9115-8ec965aa892d)

</li>

Random ordering does not give an optimal cost as the accessing cost is sum of lengths each.
So, which order minimizes the expected cost?
<br>

#### Type-1
<div>
<b>Q.</b> Consider the ordering as &pi; and &pi;(i) is the index of the file stored at location i, while i starts from 0.

<b>A.</b> A strategy that <b>feels</b> natural: store the files in increasing order of length.
But this does not solve the question. A proof is required to prove the correctness of the algorithm and the course follows the same order.

### Derivation:

<b>Lemma:</b> E(cost) is minimized when L<sub>&pi;(i+1)</sub> >= L<sub>&pi;(i)</sub> &forall;i

<b>Proof:</b>
Suppose &pi; is optimal & &exist;i s.t L<sub>&pi;(i+1)</sub> < L<sub>&pi;(i) (contradiction)

Let's compare the costs of accessing in both ordering:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ab1620cf-8c7e-467f-85ec-e42ca16f58d7)

and the cost of accessing all the other files than these is the same obviously. <br>
Let's say the cost of access before F<sub>i</sub> is X in both cases and the cost of accessing file after both these is Y in both cases. (Of course it is the summation so it is the same.)

Cost of accessing the shorter file in first case is X+Length of &pi;(i)+Length of &pi;(i+1) and in second case is X+Length of &pi;(i+1). <br>
So, the difference between the:

Cost<sub>2</sub> - Cost<sub>1</sub> = -L<sub>i</sub>

For the case of long file:

Cost<sub>2</sub> - Cost<sub>1</sub> = L<sub>(i+1)</sub>

As L<sub>(i+1)</sub> < L<sub>i</sub> from the assumption, and the Cost<sub>2</sub> > Cost<sub>1</sub>, by contradiction it is evident that second ordering is optimal compared to the first one.

Summary:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/022e94fb-5d7f-4f95-836e-80b5f3637b11)

</div>

#### Type-2

Suppose, now we are also given the information about the frequencies with which these files are accessed. Every F<sub>i</sub> will be access f<sub>i</sub>.

Now, <br>
 the Total cost using the ordering &pi; = &Sigma;<sub>(k=1 to n)</sub>f<sub>&pi;(k)</sub> . { &Sigma;<sub>(k=1 to n)</sub>L<sub>&pi;(i)</sub> } = &Sigma;<sub>(k=1 to n)</sub> &Sigma; <sub>(i=1 to k)</sub> f <sub>&pi;(k)</sub> .L<sub>&pi;(i)</sub>

 <b>Q.</b> Which order minimizes the total cost? <br>
 <b>A.</b> If all the file lengths are equal: sort by decreasing frequencies. If all the frequencies are equal: sort by increasing file lengths. But what if there are shorter files with less frequencies or longer files with higher frequencies in this order ? 
Goal: Sort according to some function: g(f,l) that <b>prioritizes high frequency and small length files.</b>

 Suppose the function has the following form, <br>
     <b>g(f,l) = l-f</b>, <br> and we have 2 files  with file 1: f<sub>1</sub> = 1, l<sub>i</sub>=3 => g(f,l) = 2
 <br> and file 2: f<sub>2</sub> = 2, l<sub>2</sub> = 5, g(l,f) = 3<br>
and if the files are ordered according to the lowest value of the function g. Then the ordering will be: A,B. <br>
So, now the cost to access B = 1X3 + 2X(3+5) = 19 [ because whenever you access B you need to access both A and B ].

While the optimal order is: <b>B,A</b>,
giving a cost of accessing B = 2X5+1X(3+5) = 18 < 19.

This function does not work. So lets look at a function that works:

<b>Sort by the ratio: L/f </b>

Why this works? Lower length values have more priority while also higher frequency values have more priority.

### Derivation:

<b>Lemma</b>: Total cost &pi; is minimized when L<sub>&pi;(i)</sub> / f<sub>&pi;(i)</sub> <= L<sub>&pi;(i+1)</sub> / f<sub>&pi;(i+1)</sub> &forall; i

<b> Proof: </b>

Assume: <br>
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/4d931e0a-4868-464b-ba03-45608f89d672) <br>
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/c22c6e1f-0367-4d32-950e-6feef9fc5c53)

Suppose, this is optimal and has L<sub>a</sub> / f<sub>a</sub> > L<sub>b</sub> / f<sub>b</sub>.

Now, swap the files:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/f777f54c-0609-42f4-ad41-e3fc4e18b6ef)

Now if the cost in the ordering &pi;<sup>'</sup> is lesser than that of &pi;, through contradiction our algorithm/function is proved.

Now, the additional cost to pay because of swapping is = f<sub>a</sub> X L<sub>b</sub> and the reduced cost due to swapping is = f<sub>b</sub> X L<sub>a</sub>.

However, by reordering our assumption's inequality, it is clear that L<sub>a</sub> X f<sub>b</sub> >  L<sub>b</sub> X f<sub>a</sub>. 

Hence, the reduced cost is greater than the additional cost to be paid, proving a contradiction to our assumption, i.e. a more optimal inequality than the assumed inequality.

### Scheduling Classes Problem:

Consider, there is a dance academy which offers classes on Saturdays for hobbyists who want to pick up a little bit of dance. So, the classes are offered at a different periods of times in the day and do not want an overlap. The goal is to maximize the number of different classes that can be adjusted to register for. 

Each class has a ( S<sub>p</sub>, f<sub>p</sub> ). The following is the schedule and a new comer has to pick up only non-mutual conflicting but can pick classes where one's starting time is the same as the other's ending time:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/096fe016-b4d8-436c-b57f-b620889681aa)

Possible strategies: <br>
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/8a1bf56a-2086-4b29-873a-79643e2caa9d)

But all the strategies fail to give the optimal scheduling. 

The strategy that works is: <b> Choose the class the ends first.</b>. In action:
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/2a614db8-b800-4073-8ef4-f737226d9a89)

The green ones are selected and the red ones represent the clash/conflict.

The algorithm: <br>
&emsp;Sort clases by finish time. <br>
&emsp;count = 0, X = &Phi;<br>
&emsp;while a class is still available:<br>
&emsp;&emsp;add the first class to X & remove it.<br>
&emsp;&emsp;remove all classes that conflict with C.<br>

### Derivation:

<b>Lemma</b>: At least one optimal conflict free collection of classes includes the one that finishes first.

<b>Proof by induction:</b>
<b>Theorem: The greedy schedule is optimal</b>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ee89cc6a-bf43-428c-bf47-0d773c44af29)

Another proof:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/ad622603-8203-4141-93d1-26edea55a4ad)


### Stable Matching problem:

Given 2 groups of "agents" which require a mapping between them while having preferences, the problem is to find an optimal matching so that both the groups are satisfied.  

Possible agents can be: (doctors, hospitals),  <b> (men, women) in a dating website </b>, (students, colleges), (jobs, applicants).

Preferences/Rankings are domain and context-dependent, not for us to worry, already made. Assume that the Rankings are complete and strict. The matchings can be of any cardinality but to keep the discussion simple we consider - one-to-one matching/mapping.

Total no. of agents = 2N (N women + N men) 

It might not always be in a way to ensure that the matching caters the happiness/satsifaction of every agent in the domain, because of the constrained one-to-one cardinality. 

Consider a matching like the following:

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/b9d81778-4927-4961-9cf3-446be9821630)

Now, an unstable or blocking pair in a matching is one where the agents prefer another agents than the ones they are currently mapped to.

Consider in the above case, Raj prefers working with Giggle than with Amazing. This does not make any pair a blocking pair because we do no know what Giggle feels about Raj. However, if Giggle displays admiration for Raj over Lata, then we have a blocking pair (Giggle-Raj) because they are not happy with their current partners and are interested in another partners. 

In general, we would like matching with no Blocking pairs. (Remember the feeling has to be mutual). But this is not always possible.

<b>Goal:</b> Find a matching that minimizes the number of blocking pairs.

[ <b> Utopia </b>: A matching with no blocking pairs. Where everyone is happy. ]

<b>Ideas: </b>

<li> Start with any matching. If there is a blocking pair, rematch with their favorable partner and <b>Hopefully</b> there won't be newer ones. [Most probably we are going to be in a while loop. This greed is never-ending.]</li> <br> ["All the preferences should be consistent."]

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/76be4f84-752e-4a60-b637-fd3d1f75d66f)

<li> Another greedy approach <b>that works</b>: Men propose in rank order and Women engage with the best offer. [Men and Women here are just agents prefering their partners accordingly and this is generally applicable.] </li>

![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/06852d53-7caf-4e5f-9aae-6fe61286f8d4)

According to the algorithm, men who are single propose to the first woman of their preference list and the women accept the first person(who is still single before he engages with another woman) and gets engaged.

Scenarios:

<li>Woman who receives no proposal => Nothing to do.</li>

<li>Woman W that is engaged to a man M => Receives propsal from M<sup>'</sup>. </li>

Now, M<sup>'</sup> proposes to W and according to the preference list W prefers M<sup>'</sup> over M ( but the proposal was not received earlier because M prefers some other woman W<sup>'</sup> over W and as that woman is engaged he now comes to W.). As this could create a <b>Blocking pair</b> in the final matching if W remains with M (as she prefers M<sup>'</sup> over M), it is better off according to the greedy approach to break off the engagement with M and get engaged with M<sup>'</sup>

This repeats as long as any of the men are single. And eventually ends. [The implementation and other details are going to be in the implementation folder.]
