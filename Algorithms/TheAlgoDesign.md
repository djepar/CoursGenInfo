# The Algorithm Design Manual 
Third Edition
By Steven S. Skiena

# Chapter 1 : Introduction to Algorithm Design

"What is an algorithm? An algorithm is a procedure to accomplish a specific task." (p.3)

An alorithm solve a general "well-specified _problem_", for exemple:
The problem : soorting
The Input : A sequence of n keys a1...an
The output : The permutation (reordering)

The instance would ve the sequence to sort. 

An algorithm take any of the possible input and transforms it to the desired output. (p. 3)

"Three desirable properties for a good algorithm" : correct, efficient and easy to implement. (p. 4)

## Robot welding shortest path

### Resolve with the Nearest Neighbor

```
NearestNeighbor(P)
    Pick and visit an initial point p0 from P
    p = p[0]
    i = 0
    While i < len(p)
        i += 1
        Select p[i] + 1
        Visit p[i]
    Return to p[0] from p[n-1]

```

Problem with the NearestNeighbor algorithm : doesn't find the shortest path. 

### Resolve with the the ClosestPair(P) 

" A different idea might repeatedly connect the closest pair of endpoints whose connection will not create a problem, such as premature termination of the cycle. Each vertex begins as its own single vertex chain. After merging everything together, we will end up with a single chain containing all the points in it. Connecting the final two endpoints gives us a cycle. " (p. 7)


```
ClosestPair(P)
    Let n be the number of points in set P.
    For i = 1 to n -1 do
        d = infinity
        For e3ach pair of endpoints (s,t) forem distinct vertex chains
            if dist(s,t) <= d then sm = s, tm = t, and d = dist(s,t)
        Connect (Sm, tm) by an edge
    Connect the two endpoints by an edge
```

The closest-pair is a bit more complicated and less efficient but it's gave us the right answer : the shortest path for this example. 


### Resolving with the OptimalTSP
TSP is the traveling salesman problem that we will try to solve through out the book. ?(p. 8)
```
OptimalTSP(P)
    d = infinity
    For each of the n! permutations Pi of point set P
        If (cost(Pi)<= d) then d = cost(Pi) and Pmin = Pi
    return Pmin

```

### The difference between algorithms and heuristics
Algorithms always produce the correct result
Heuristic may usually do a good job but provide no guarantee of correctness. 

## 1.2 Selecting the Right Jobs
Problem : Movie Scheduling Problem
Input : A set I of n intervals on the line. 
Output: What is the largest subset of mutually non-overlapping intervals that can be selected from I?

### Resolving the Right Jobs with EarliestJobFirst(I)

```
EarliestJobFirst(I)
    Accept the earliest starting job from I that does not overlap any previously accepted job, and repeat until no more such jobs remain. 
```
This one those not work because the Earliest job can be a long movie and we need to have the largest subset of mutually non-overlapping intervals. 


### Resolving the Right Jobs with ShortestJobFirst


```
ShortestJobsFirst(I)
    While( I != ∅) do
        Accept the shortest possible job j from I. 
        delete j, and any interval that intersects j from I

```

### Resolving the Right Jobs with Exhaustive Scheduling(I)
```

j = 0
Smax = ∅
For each of the 2^n subsets Si of intervals I
    If (Si is mutually non-overlapping) and (size(Si) > j)
        then j = size(Si) and Smax = Si
Return Smax

```
Because of 2^n, it's can become almost impossible to solve for large N. 

### Resolving the Right Jobs with Optimal Scheduling(I)

```
OptimalScheduling(I)
    While ( I !=  ∅) do
        Accept the job j from I with the earliest completion date. 
        Delete j, and any interval which intersects j, from I. 
```

#### Beware 
"Reasonable-looking algorithms can easiliy be incorrect. Algorithm correctness is a property that must be carefully demonstrated."

## 1.3 Reasoning about Correctness

First tool to distinguish correct algorithms from incorrect ones : proof. 
Made from :
1. A clear and precise statemet of what to prove. 
2. A set of assumptions of things that are taken to be true, and hence can be used as part of the proof. 
3. Chain of reasoning that takes you from these assumptions to the statement you are trying to prove. 
4. The square or Qed at the bottom to denote that you have finisehd (Quod erat demonstrandum)
(p.11)

### Problems and Properties 
The part of a problem
1. the set of allowed input instances
2. the required properties of the algorithm's output. 



"Take-Home Lesson : An important and honorable technique in algorithm design is to narrow the set of allowable instancess until there is a correct and efficient algorithm. For example, we can restrict a graph problem from general graphs down to trees, or a geometric problem from two dimensions down to one. " (p. 12)

### Demonstrating Incorrectness 
Counterexample is the best way to prove an algorithm doesn't work. 

Good counterexamples are :
- Verifiability : "To demonstrate that a particular instance is a counterexample to a particular algorithm, you must be ablo to calculate what answer your algorithm will give in this instance, and display a better answer so as to prove that the algorithm didn't find it. " (p.13)
- Simplicity : "Good counter-example have all unneecessary details stripped away." (ibid) 

Hunting for counterexample :
- Think small
- Think exhaustively
- Hunt for the weakness 
- Go for a tie
- Seek extremes



```
```
```
```
