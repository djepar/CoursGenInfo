1-1. Show that a + b can be less than min(a, b).
    -5 + -6 


1-2. Show that a × b can be less than min(a, b).
    -5 + 3


1-3. Design/draw a road network with two points a and b such that the fastest route between a and b is not the shortest route.
    Easiest : 
        A --- C --- B
    More complex :
                -
            -       -
        A-              - B
        ---------------- C
    
1-4. Design/draw a road network with two points a and b such that the shortest route between a and b is not the route with the fewest turns.

                -
            -       -
        A-              - C
        ----        ----- B
            |------|


1-5. [4] The knapsack problem is as follows: given a set of integers S = {s1, s2,...,sn}, and a target number T, find a subset of S that adds up exactly to T. For example, there exists a subset within S = {1, 2, 5, 9, 10} that adds up to T = 22
but not T = 23.

Find counterexamples to each of the following algorithms for the knapsack problem. That is, give an S and T where the algorithm does not find a solution that
leaves the knapsack completely full, even though a full-knapsack solution exists.
(a) Put the elements of S in the knapsack in left to right order if they fit, that is, the first-fit algorithm.
    S = 5, 4, 3 ,5 ,5
    T = 11
(b) Put the elements of S in the knapsack from smallest to largest, that is, the
best-fit algorithm.
    S = {10, 15, 22, 25, 30}
    T = 30



(c) Put the elements of S in the knapsack from largest to smallest.
    S = {20, 10, 7, 5, 3}
    T = 8






1-6. [5] The set cover problem is as follows: given a set S of subsets S1,...,Sm of
the universal set U = {1, ..., n}, find the smallest subset of subsets T ⊆ S such
that ∪ti∈T ti = U. For example, consider the subsets S1 = {1, 3, 5}, S2 = {2, 4},
S3 = {1, 4}, and S4 = {2, 5}. The set cover of {1,..., 5} would then be S1 and
S2.
Find a counterexample for the following algorithm: Select the largest subset for
the cover, and then delete all its elements from the universal set. Repeat by
adding the subset containing the largest number of uncovered elements until all
are covered.
1-7. [5] The maximum clique problem in a graph G = (V,E) asks for the largest
subset C of vertices V such that there is an edge in E between every pair of
vertices in C. Find a counterexample for the following algorithm: Sort the
vertices of G from highest to lowest degree. Considering the vertices in order
28 CHAPTER 1. INTRODUCTION TO ALGORITHM DESIGN
of degree, for each vertex add it to the clique if it is a neighbor of all vertices
currently in the clique. Repeat until all vertices have been considered.
Proofs of Correctness
1-8. [3] Prove the correctness of the following recursive algorithm to multiply two
natural numbers, for all integer constants c ≥ 2.
Multiply(y, z)
if z = 0 then return(0) else
return(Multiply(cy, z/c) + y · (z mod c))
1-9. [3] Prove the correctness of the following algorithm for evaluating a polynomial
anxn + an−1xn−1 + ··· + a1x + a0.
Horner(a, x)
p = an
for i from n − 1 to 0
p = p · x + ai
return p
1-10. [3] Prove the correctness of the following sorting algorithm.
Bubblesort (A)
for i from n to 1
for j from 1 to i − 1
if (A[j] > A[j + 1])
swap the values of A[j] and A[j + 1]
1-11. [5] The greatest common divisor of positive integers x and y is the largest integer
d such that d divides x and d divides y. Euclid’s algorithm to compute gcd(x, y)
where x>y reduces the task to a smaller problem:
gcd(x, y) = gcd(y, x mod y)
Prove that Euclid’s algorithm is correct.
Induction
1-12. [3] Prove that n
i=1 i = n(n + 1)/2 for n ≥ 0, by induction.
1-13. [3] Prove that n
i=1 i
2 = n(n + 1)(2n + 1)/6 for n ≥ 0, by induction.
1-14. [3] Prove that n
i=1 i
3 = n2(n + 1)2/4 for n ≥ 0, by induction.
1-15. [3] Prove that
n
i=1
i(i + 1)(i + 2) = n(n + 1)(n + 2)(n + 3)/4
1-16. [5] Prove by induction on n ≥ 1 that for every a = 1,
n
i=0
ai = an+1 − 1
a − 1