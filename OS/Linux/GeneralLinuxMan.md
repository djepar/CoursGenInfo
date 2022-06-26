Based on 
Efficient Linux at the Command Line, Daniel J. Barrett
O'REILLY (2022)
and
Learning Modern Linux : A Handbook for the Cloud Native Practitioner, Michal Hausenblas
O'REILLY (2022

Intro 
"An operating system takes on all this undifferentiated heavy lifting abstracting away the different hardware components and providing you with a (usually) clean and nicely designed Application Programming Interface (API), such as is the case with the Linux kernel [...]. We usually call these APIs that an OS exposes system calls or syscalls for short." (Hausenblas, 3%)

getuid give access to the uid of a function of man

The main function of an OS is to "provide us with an API, Application Program Interface" (p. 32)

## Linux Kernel

### Linux Architecture
Three layers :
    - At the bottom, we have the hardware layer. It contains the CPU, the RAM, the Motherboard, etc. 
    - The middle layer is the Kernel. 
    - The upper layer is the user space, where the shell, the majority of the application that are running and the utilities like ps (Hausenblas)

Between the Kernel and the User Land, we find the syscall (system calls).

Between the Kernel and the Hardware, there is a collection of individual interfaces grouped by hardware:

User vs kernel mode
    -Kernel mode : app closer to the hardware, faster with limited abstraction. 
    -User land : slower, safer and more convenient abstraction wise. 
Normally, we need to know how to interact with the kernel but not how to use the kernel mode (except for kernel dev)

cpu info commands
    - $lscpu
    - $cat /proc/cpuinfo


#### Arm Architecture 
"ARM is a family of Reduced Instruction Set Computer (RISC)" (Hausenblas, p. 31)


