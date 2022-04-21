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

## Writing and Running Integration Tests (p. 6 - 9)
Inside-out or unit testing are one type of test(will be seeing in chapter 4). The other type is outside-in or integration testing, test like a user would.

"The convention in Rust projects is to create a tests directory parallel to the src directory for testing code" (p.6)



```
#[test] //tells Rust to run this function when testing. 

fn works() {
    assert!(true); // The assert! macro asserts that a Boolean expression is true. 
   assert!(false);


}

```
To run the test : `cargo test`


assert! verify that some expectation i true, or assert_eq! to verify that something is an expected value. (p.7)
#### To create a more complext test (p. 8-12)

```
//in tests/cli.rs
use std::process::Command;

#[test]

fn run() {
    let mut cmd = Command::new("ls");
    let res = cmd.output();
    assert!(res.is_ok());

}

```
Should run : 
```
running 1 test
tests run ... ok
```




#### Path (p.9)
We can see the path with echo $PATH or $env:Path with Powershell. 

To translate the ':' to '\n' we just need to 
echo $PATH | tr : '\n'

To run the program we can write `.\name_of_file` in the debug file of the target file. 


#### Dependencies for dev

To find the program in the crate directory : assert_cmd

So we need to change Cargo.toml like this : 
```
[package]
name = "chapter1"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]

[dev-dependencies]
assert_cmd = "1"
```

#### Test 01 : runs
This first test just look to see if the program appears to succeed


#### Understanding Program Exit Values (p.11)
"What does it mean for a program to run successfully? Command-line program should report a final exit status to the operating system to indicate success or failure. The POSIX standards dictate that the standard exit code is 0 to indicate success and any number from 1 to 255 otherwise. " (p.11)

With `$?` we can access the exit status of the most recent command 
like 

```
$ true
$ echo $?
0
```

### Testing the Program Output
```
\\in tests/cli.rs change the fn runs to : 
#[test]
fn runs() {
    let mut cmd = Command::cargo_bin("chapter1").unwrap();
    cmd.assert().success().stdout("Hello, world!\n");
}










```

```

```




```



