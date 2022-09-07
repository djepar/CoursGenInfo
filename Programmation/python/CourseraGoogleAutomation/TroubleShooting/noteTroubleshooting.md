# Troubleshooting Concepts
Troubleshooting : "The process of identifying, analyzing, and solving problems"
Debugging : "The process of identifying, analyzing and removing bugs in a system. "

Examples of tools : 
- tcpdump 
- wireshark
- strace
-ltrace : A library call tracer (https://www.man7.org/linux/man-pages/man1/ltrace.1.html)

Debuggers : 
"Let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more"

## Problem Solving Steps 
1. Getting information
    - Reproduction case : "A clear description of how and when the problem appears".
2. Finding the root cause
3. Performing the ncessary remediation. 
Important to document what we do while debugging. 

### Silently Crashing Application
strace "lets us look more deeply at what the program is doing. It will trace a system calls made by the program and tell us what the result of each of these calls was."
System calls : "calls that the programs running on our computer make to the running kernel". 
To see failure `strace -o failure.strace ./<program-name>`
Pipping with less : `strace ./script.py | less`

# Understanding the problems
Questions to ask to understand what didn't work :
"
- What were you trying to do?
- What steps did you follow?
- What was the expected results?
- What was the actual results?
"

## Reproduction case 
"A reproduction case is a way to verify if the problem is present or not"
"First step is to read the logs available to you"
On Linux : /var/log/syslog and read the file .xsession-errors
On MacOs /library/Logs
On Windows : Event viewer tool.
## Finding the Root Cause
Use creativity and research to find the cause. 
For memory error, we can use iotop, iostat and vmstat
And to solve it : ionice
For a service using to much network bandwith : iftop,
To solve it rsync or Trickle
## Dealing with Intermittent Issues
If possible, adding code to have more information. 
Heisenbug or the observer effect : "observing a phenomen alters the phenomenon."

# Binary Search a Problem
Faster, but need a sorted list. 

## Applying Binary Search in Troubleshooting
Bisecting the problem : each part of the problem we know is working can be put aside.

git let us use `bisect` that do that automaticaly. 

## Finding Invalid Data 
`cat contacts.csv | ./import.py --server test`
Important to put server. 
Using `wc` to count the number of files
`wc -l contacts.csv`
Searching invalid Data with head and tail
`head -50 contacts.csv | ./import.py --server test`
`less -50 contacts.csv | ./import.py --server test`
`head -50 contacts.csv | tail -25 | head -13 ./import.py --server test`