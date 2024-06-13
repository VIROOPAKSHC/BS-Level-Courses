## Week-2 : Matroids

### A combinatorial object called Matroids.

Instread of proving every theorem individually, proving a problem has the matroid structure removes the necessity to prove it based on a theorem, that will be discussed this week which outsources the proof.

<b>Setting up - A Generic Optimization Problem:</b>

Consider a Universe U = {e<sub>1</sub>,e<sub>2</sub>,e<sub>3</sub>,....,e<sub>N</sub>} and consider a weight attributed to every element in the universe which is rational, non-negative.
  <br> wt function : U -> a<sup>>=0</sup>

Now, consider a set F which consists of the sets = {S<sub>1</sub>,S<sub>2</sub>,...,S<sub>m</sub>}
and the weight function naturally extends. 
<br>So, the weight of S wt(S) = &Sigma;<sub>e&isin;S</sub>wt(e)

Now, the question is to find a set in F that has the maximum weight. Note that this is a maximization problem.
<br>
However, in general the natural approach is to use a sorting algorithm to sort the sets based on their weights and take the first/last element accordingly. This would work, <b>if we have the set F completely defined</b>. But in most cases we are provided with a vague definition of what goes into F from the set U. 

In general, we are given with an <b>Oracle</b> function that checks if a given set is present in F which is a sort-of black-box.

Now, the problem has become difficult and challenging. 

Consider the following algorithm:
```
Sort the elements of U in descending order of weights;
Initialize the set X = {}
While there are elements left:
  if ((X U curr) belongs to F): // Generally given by the Oracle function
    X <- X U curr
  move on to the next element in the list
```

From the outside, it looks like the algorithm might always provide an optimal solution, but consider the following scenario:

Universe U = {W,X,Y,Z} with wt(W) = 50, wt(X) = 30, wt(Y) = 42, wt(Z) = 10
and F = {{W},{X,Y},{Y,Z},{Z}} with weights = 50, 72, 52, 10 respectively.

Now according to our code when we move through the elements in U and iterate over it after sorting it, it chooses W first and tries to map it with any of the rest because weight of W is te highest. However this was not the optimal solution we wanted instead, the output should have been {X,Y}, but because X has not been selected first, the pair has not been selected.

<b>Defining Matroids:</b>
Given a Universe U and a Family F of the universe defined as above, F is called a Matroid if it follows all the following propoerties:
<ol>
  <li>Non-emptiness: F must contain the element &Phi;</li>
  <li>heredity: If X &isin; F and Y &Subset; X then Y &isin; F</li>
  <li>Exchange Property: If X,Y &isin; F and |X| > |Y| then &exists; x &isin; X-Y. Which means Y &cup; {x} &isin; F.</li>
</ol>

Now, consider our example earlier, the set F is clearly not a matroid for several reasons:
<li>It does not fulfill the non-emptiness propoerty.</li>
<li>It does not fulfill the heredity property because for e.g. {X,Y} is present, then {X}, {Y} should be individually present in F.</li>
<li>And it also does not fulfill the Exchange property.</li>
And this can be considered as a non-example for Matroids.

<b>Example for Matroids:</b>

Uniform Matroid: <br>
 U = {1,2,....,n} [Consider n=10] <br>
 F = {X | X &Cup; U, |X| &le; k } <br>
<br>
F satisfies all the above properties now. <br>
<br>
Linear Matroid:<br>
 A = n x m matrix <br>
 U = {1,....,m} <br>
 F = {X &Subset; U | the columns corresponding to X are linearly independent in A } <br>
<br>
F satisfies all the properties.<br>
<br>
Graphic Matroid:<br>
 G = (V,E) set of edges and vertices<br>
 U = E<br>
 F = {X &Subset; E | G[x] is acyclic}<br>
<br>
F satisfies all the properties;
<br>
Another <b>non-example</b> of Matroids:
<br>
 G = (V,E) <br>
 U = E<br>
 F = {X | X &Subset; E s.t X is a matching (by matching it has disjoint collection of endpoints)}<br>
This might seem like a matroid strucutre, but is not. <br>
<br>
This is because: both non-emptiness and heredity are going to be fulfilled but not the Exchange property because consider the following case:
We have a set, {{ab},{xy}} with 2 disjoint match pairs which is valid, also we have another element in F, {xb}. Now, as we have 2 different elements in F, one with a bigger size than the other, we should be able to pull out one element from the bigger set and add it to the smaller which should still belong to F. However, it fails to follow in this case.
<br>
<br>
Summarized matroid definition:<br>
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/d7e7f745-84ee-4e55-8abf-76c031781b6d)
<br>

<b> Some Terminology: </b>
<li>All the elements in a Family are called Independent sets. [Note: this terminology is different from that of graphs]</li>
<li>Maximal sets in F. A set is called maximal set when there is no other set that contains this or it cannot be extended further. [Basis elements]</li>

Claim: If X, Y &isin; F and if X & Y are basis elements (i.e., X&Y are maximal in F) then |X| = |Y|
<li>All the basis elements have same size and the size is called the rank.</li>
<li>If a set does not belong to the family it is called a dependent set.</li>
<br>
So, consider for a connected graph, the basis elements form a spanning tree following all the matroid properties and all of them would have the same size.

Now, coming back to our problem, let's look at Greedy algorithm for Matroids.
<br><br>
Input: (U,F), wt : U -> Q<sup>&ge;0</sup>, oracle access to F. <br>
Output: max-wt. set in F.<br>
Now, F follows the matroid structure over the universe U.<br>
<br>
Greedy Basis  Algorithm:
```
Sort the elements of U in decreasing order of wt.
X -> {}
for i in 1-> n:
  if ( X U ei belongs to F ):
    X <- X U {ei}
return X
```
<br><br>
Using a contradiction on the exchange property it can be proved that if F has a matroid structure, then the Optimal solution and Outputted solution from the Greedy Basis Algorithm are one and the same.<br>
<br>
<b>Greedy on Non-Matroid Structures: Fails!!</b>

<em>New Terminology:</em>
<li>SubSystem: Finite collection of sets that follow the "heredity" property, i.e., X &isin; F, Y &Subset; X then Y &isin; F. But this may or may not follow the exchange property. </li>
<br>
<br>
Now, For any subset system (U,F) that is not a matroid, there is a weight function W such that the greedy algorithm does NOT return an optimal solution.<br>
<br>
<br>
Theorem: If F -> Fails to satisfy the exchange property then it means that &exists; X,Y &isin; F such that |X| > |Y| but &forall; x &isin; X\Y, Y &cup; {x} &notin; F.
<br>
<br>
<em> Now, we want to prove that failing to obey the exchange property makes it fail to give an optimal solution using the Greedy basis algorithm: </em>

Consider X, Y and |X| > |Y| (indicates size), and because it does not follow exchange property, if we take an x &isin; X \ Y, then Y &cup; {x} &notin; F. And X is the optimal output of the problem and Y is the greedy basis output (as this is a non-matroid structured problem both are different in sizes too). <br>
<br>
Let's say size of |Y| is m and all the elements in Y have the weight of m+2. And consider all the elements in the X \ Y, region to be m+1.<br> 
Now, because m+2 > m+1, greedy chooses all the m elements of Y, this weight = m*(m+2) = m<sup>2</sup> + 2m <br>
Now, as size of |X| > |Y| => |X| &ge; m+1 <br>
Then the weight of X would be &ge; (m+1)*(m+1) = m<sup>2</sup> + 2m + 1 <br>
Now, it is set that <b> X is heavier than Y, but the elements of Y are heavier than those in X and because of that greedy basis selects Y (this is also becauuse it has a non-matroid structure else we could use the exchange property and prove that both are the same) </b>
<br>
Hence, as greedy is misguided because the problem does not have matroid structure, it fails to produce an optimal solution. <br>
<br>
<br>
Similarly, let's look at a modified example from Scheduling Classes but with weights to each class. Earlier, even though Scheduling classes were not in matroid structure (because it does not follow the exchange property due to non-overlap etc) it should not work with the Greedy basis algorithm, but it did produce an optimal answer. Why is it? <br><br>

Because there was not a waiting time/weight associate with each element and all elements were equally important the greedy algorithm worked. But now because if we associate weights with the classes like the one shown below: <br><br>
![image](https://github.com/VIROOPAKSHC/BS-Level-Courses/assets/69083163/47728979-0da2-4be8-aa20-2f4bc3c37e9e)
Among this, the greedy would pick the green one because of heigher weight and fails to produce an optimal solution.<br>
#### New Problem: Scheduling with Deadlines:
This is a concrete problem that can be solved using the greedy algorithm, but we will not be showing the proof because it follows the Matroid strucutre.<br><br>
Problem Definition: There are n tasks with deadline D and penalty P to each task and n days. 
D[i] is day by which the i-th task should be completed to avoid a penalty which is in the range of [1,n]. P &isin; Q<sup>&ge;0</sup>. A schedule is a permutation &pi; of {1..n}
<br>
Cost(&Pi;) = &Sigma;<sub>(i=1 to n)</sub> P[i] * [&Pi;(i) > D[i]] <br>
The value inside the square backets is 1 if the statement is true else 0
<br>
<br>

Realistic Schedule: A subset of schedule is called realistic where all tasks in X are on time. <br>
For a schedule on tasks to be realistic &forall; 1 &le; i &le; n, the # of tasks in X that have a deadline of i (or &le; i) is &le; i. <br>
If the tasks follow the above, then it is possible to simply sort based on the deadline and we would be done with an optimal schedule.<br>
<br>
<em> More Formally: </em>
X &Subset; [n] is realistic if and only if | X(t) | &le; t &forall; 1 &le; t &le; n, where the | X(t) | = number of tasks in X with a deadline on or before t. <br>
<b>Claim:</b> The set X of realistic tasks that maximizes total penalty corresponds to an optimal schedule.
<br>
<b>Claim:</b> The collection of realistic tasks forms a matroid.
