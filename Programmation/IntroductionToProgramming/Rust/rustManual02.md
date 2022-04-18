Command-Line Rust : A Project-Based Primer for Writing Rust CLIs
by Ken Youens-Clark. 
O'REILY, Sebastoppol, CA, USA.(2022)

# Introduction 

Rust was developped by Graydon Hoare while working at Mozilla Research in 2006 (p. x)

Rust is "syntactically similar to C [...] :
 - loops,
 - semicolon-terminated statements,
 - and curly braces denoting blocks structures". (ibid)

Designed for safety and performance :
- The memory safety method of rust is through borrow checker which "tracks which part of a program has safe access to different parts of memory "(ibid).
- "Rust programs compile to native binaries and often match or beat the speed of programs written in C or C++." (ibid)

"Rust is a statically types languages like C/C++ or Java. This means that a variable can never change its type".

Statically types in opposition to Dynamically types (Perl JavaScript Python).

"Rust is not an object-oriented (OO) language like C++ or Java, as there are no classes or inheritance in Rust. Instead, Rust uses a struc(structure) to represent complexe data types and traits to describe how types behave. (p. xi) "

# Chapter 1 : Basic function

## General Command (p.2-3 )  :
- with rust compiler:
    `rustc hello.rs`
- on Windows
    - To compile : 
        `rustc.exe .\hello.rs`
    - To execute :
        `.\hello.exe`
- MacOs
    - To see what kind of file 
        `file hello`
    - Execute
        `./hello`
- Linux
    - To remove (directory or item)
        `rm hello` //usefull to remove the hello binaryt because it''s the name of the directory we will create. 
    - To create the directory structure        
        `mkdir -p hello/src` //the -p is for creating the parent folder before. 
    
## Organizing a Rust Project Directory (p.3-4):

```








