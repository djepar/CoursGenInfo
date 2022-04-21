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

PAGE 7 : faire ClosestPair







```

