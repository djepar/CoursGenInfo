Based on 
Efficient Linux at the Command Line, Daniel J. Barrett
O'REILLY (2022)
and
Learning Modern Linux : A Handbook for the Cloud Native Practitioner, Michal Hausenblas
O'REILLY (2022

Intro 
"An operating system takes on all this undifferentiated heavy lifting abstracting away the different hardware components and providing you with a (usually) clean and nicely designed Application Programming Interface (API), such as is the case with the Linux kernel [...]. We usually call these APIs that an OS exposes system calls or syscalls for short." (Hausenblas, 3%)

getuid give access to the uid of a function of man

The main function of an OS is to "provide us with an API, Application Program Interface" (p.__)

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
"ARM is a family of Reduced Instruction Set Computer (RISC)" (Hausenblas, p. 15)

### Main function of the Kernel
Management :
    - of the process
    - of the memory, allocating memory and mapping a file into memory. 
    - of the network
    - of the files
    - of character devices and device drivers


#### Process Management, from granular to smallest

    - Session : "contain one or more process group and represent a high level user-facing unit with optional tty attached.The kernel identifies a session via a number called session ID(SID)." (ibid, p. 33)
    - Process groups : "Contain one or more process" (idem). Can be found with process group ID (PGID).
    - Process : the user-facing unit. "Abstractions that group multiple resources (address space, one or more threads, sockets, etc), which the kernel expose to you via /proc/self for the current process. The kernel identifies a process via a number called process ID(PID)" (idem) 
    - Threads : "Implemented by the kernel as processes. That is, there is no dedicated data structures representing threads." (idem). It's share certain ressources with other process. 
      - Group thread ID (TGID), meaning multithreading
      - Thread id (TID)
    - Task 
      - In sched.h, there is task_struct, a data structure "that form the basis of implementing processes and threads alike. This data structure captures scheduling-related information, identifiers (such as PID and TGID), and signal handlers, as well as other information, such as the related to performance and security. 

##### Commands for process management
    - $ps
    - $top
#### Memory Management
"Both physical and virtual memory are divided into fixed-length chunks we call pages"

"The core of memory management : how to effectively provide each process with the illusation that its page actually exists in RAM while using the existing space optimally." (Hausenblas, p. 19)

To look for information about memory /proc/meminfo

### Networking
The layered architecture of Linux networking :
    - "Sockets : for abstracting communication
    - Transmission Control Protocol (TCP) and User Datagram Protocol (UDP): for connection-oriented communication and connectionless communication respectively.
    - Internet Protocol (IP): For addressing machines" (ibid, p.21)

### FileSystems
"Linux uses filesystems to organize files and directories on storage devices such as hard disk drives (HDDs), and solid-state drives(SSDs) or flash-memory." (ibidem)

### Device Drivers
"A driver is a bit of code that runs in the kernel. Its job is to manage a device, which can be actual hardware" or a pseudo-device. (ibidem)

Commands 
    - ls -al /sys/devices
    - mount

## Syscalls or between land user and the Kernel
"The service interface the kernel exposes and that user land entities call is the set of system calls, or syscalls for short." (ibid, p. 23)
The system usually invoke the syscall through the C standard library