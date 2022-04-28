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


# Chapter 2 : Test for Echo
In this chapter, we create a Rust version of the echo program

echo print its arguments to STDOUT :
```

admin@admins-MacBook-Pro CoursGenInfo % echo BOnjouR
BOnjouR
```

To put the STDOUT to a file : 
```
admin@admins-MacBook-Pro CoursGenInfo % echo Bonjour > allo.txt
admin@admins-MacBook-Pro CoursGenInfo % ls 
Algorithms      IntroProg       Mathematics     allo.txt
CLIs            LICENSE         README.md
admin@admins-MacBook-Pro CoursGenInfo % cat allo.txt
Bonjour
```
(p.19)

## main()

"All functions return a value, and the return type may be indicated with an arrow and the type such as `-> u32` to say that the functions returns an unsigned 32-bit integer. 
The lack of any return type for main implies that the function returns what Rust calls the unit type. " (p.20)

println! macro : "will automatically append a newline to the output.

### Passing args : 
```

fn main() {
    println!("{:?}",std::env::args());
}
```
For passing the -n argument/flag : 
```
cargo run Bonjour -n
or
cargo run -- -n Bonjour
but not !!!!! cargo run -n Bonjour
```

### Adding clap as a Dependency
```
[dependencies]
clap = "2.33"
```
Then : `cargo build`
 
To know the size of a project : `du -shc`

`cargo clean` : to clear the target directory, we will need to recompile after (p.24)


Pretty-print the arguments 

```
println!("{:?}", wtv); // to format the debug view of the argument
println!("{:#?}", wtv); // to include newlines and indentations to read the output, also called pretty-printing. (p.26)

```
#### Runnning echoR without args : 
Will give an error, but to see the output error message we need to write in the bash shell : 
```
cargo run 1>out 2>err
cat err
```
It will redirect channel 1 (STOUT) to a file called out and channel 2 (STDERR) to a file called err.  (p.29)

### Creating the Program Output

Arg can use two functions that return mutiple values :

    ArgMatches::values_of, will returns Option<Values>

    ArgMatches::values_of_lossy, will returns Option<Vec<String>>

Since, we want to return a string, we will use ArgMatches::values_of_lossy

Definitions

    "Option a value that is either None or Some< T>, where T is any type like a string or an integer. In the vase of AargMatches::values_of_lossy, the type T will be a vector of strings."

    "Values : an iterator for getting multiple values out of an argument."

    "Vec : A vector, whhich is a contiguous growable array type."

    "String:  A string of characters " (p. 30)

#### About unwrap : 
Using Option::unwrap is risky because, if we unwrap a None, the program panic and crash. But in that case, we know that it's will only return a type, so we can safetly use unwrap : 


```
let text = matches.values_of_lossy("text").unwrap();
```

#### Omitting endline 

```
// Long way : 
    let mut ending = "\n";
    if omit_newline {
        ending = ""; //will not work
    }

// Short way
    let ending = if omit_newline { "" } else { "\n" };

```

### Integration Tests

Adding dev dependencies  in toml
[dev-dependencies]
assert_cmd = "2"
predicates = "2"


"I often put the word dies somewhere in the test name to make it
clear that the program is expected to fail under the given condi‐
tions. If I run cargo test dies, then Cargo will run all the tests
with names containing the string dies." (p.34)

### Creating files to compare

With a bash command (the files will be in tests/expected) : 


```
#!/usr/bin/env bash

OUTDIR="tests/expected"
[[ ! -d "$OUTDIR" ]] && mkdir -p "$OUTDIR"

echo "Hello there" > $OUTDIR/hello1.txt
echo "Hello"  "there" > $OUTDIR/hello2.txt
echo -n "Hello  there" > $OUTDIR/hello1.n.txt
echo -n "Hello"  "there" > $OUTDIR/hello2.n.txt

```
And then we can compare with a test in tests/cli.rs

```
#[test]
fn hello1(){
    let outfile = "tests/expected/hello1.txt";
    let expected = fs::read_to_string(outfile).unwrap();
    let mut cmd = Command::cargo_bin("echor").unwrap();
    cmd.arg("Hello there").assert().success().stdout(expected);
}

```


For the moment, we used unwrap to unpack an Ok value or propagate an Err. Now we will change the whole test to use '?' instand. 
For that, we will need to create a type alias,"a specific type of
Result that is either an Ok that always contains the unit type or some value that
implements the std::error::Error trait" (p.36): To be sure, it's on the heap and not the stack. 


```

type TestResult = Result<(), Box<dyn std::error::Error>>;

```


```

```

```




```



