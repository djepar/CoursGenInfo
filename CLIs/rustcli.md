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
        `rm hello` 
    - To create the directory structure        
        `mkdir -p hello/src` //the -p is for creating the parent folder before. 
    -to move
        `mv hello.rs hello/src`

    
## Organizing a Rust Project Directory (p.3-4):
Removing the hello binary (for Unix System)
    ```
    rm hello
    ```
Then creating the new directory with the parent 
```
    mkdir -p hello/src
```
Change the location of hello.rs
```
mv hello.rs hello/src
```   
## Creating and Running a Project with Cargo (p. 5 - 6)

Create : `cargo new hello`

To compile and run : `cargo run`

To compile quietly : `cargo run --quiet`

## Writing and Running Integration Tests (p. 6 - __)
Inside-out or unit testing are the two types of integration tests (will be seeing in chapter 4)

"The convention in Rust projects is to create a tests directory parallel to the src directory for testing code" (p.6)

```
#[test] //tells Rust to run this function when testing. 

fn works() {
    assert!(true); // The assert! macro asserts that a Boolean expression is true. 
   assert!(false);


}

```
bv 
#### To create a more complext test (p. 8-9)

```
use std::process::Command;

#[test]

fn run() {
    let mut cmd = Command::new("ls");
    let res = cmd.output();
    assert!(res.is_ok());

}

```








```

```

```




```



