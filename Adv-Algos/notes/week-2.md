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
  <li>Hereditary: If X &isin; F and Y &Subset; X then Y &isin; F</li>
  <li>Exchange Property: If X,Y &isin; F and |X| > |Y| then &exists; x &isin; X-Y. Which means Y &cup; {x} &isin; F.</li>
</ol>

Now, consider our example earlier, the set F is clearly not a matroid for several reasons:
<li>It does not fulfill the non-emptiness propoerty.</li>
<li>It does not fulfill the hereditary property because for e.g. {X,Y} is present, then {X}, {Y} should be individually present in F.</li>
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
This is because: both non-emptiness and Hereditary are going to be fulfilled but not the Exchange property because consider the following case:
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

Now, coming back to our problem, let's look at Greedy algorithm for Matroids.
<br><br>
Input: (U,F), wt : U -> Q<sup>&ge;0</sup>, oracle access to F. <br>
Output: max-wt. set in F.<br>
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
