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

# Introduction to Slowness
## Why is my computer slow?
Monitoring are system to see where is the bottleneck component. 
On Linux : top
MacOs : Activity Monitor
Windows : Resource Monitor and Performance Monitor. 

## How Computers Use Resources
The data uses by a processes can be on the CPU/GPU, RAM,  Hard-driver or Network (from the quicker to slower)
Cache is a good way to fasten the speed of an app : if the data is on the network, we can cache it on the RAM (etc).

## Possible Causes of Slowness
Use the process of elimination (like with every other problem) : 
1. Looking for the simplest explanation. 
2. Bissecting the problem

Possibles causes
- When a file uses by a program become to big. 
    - Can be solve with logrotate
- Can look if the problem is for all users or just some (help fin the cause)
- If a program use a share-file system base on a network
- Malicious software

## Slow Web Server
If the loading page is slow, we can use the tool `ab` (Apache Benchmark) "to figure out how slow it is."
Priority in linux : lower the number, the higher the priority. 
To change the priority  : `nice` and `renice`
Example "for pid in $(pidof ffmpeg); do renice 19 #pid; done
To resolve the ffmpeg problem
`for pid in $(pidof ffmpeg); do while kill -CONT $pid: do sleep 1; done

## Monitoring tools
https://docs.microsoft.com/en-us/sysinternals/downloads/procmon 

http://www.brendangregg.com/linuxperf.html

http://brendangregg.com/usemethod.html

Activity Monitor in Mac:

Performance Monitor on Windows

https://www.digitalcitizen.life/how-use-resource-monitor-windows-7

https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

https://en.wikipedia.org/wiki/Cache_(computing)

https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/