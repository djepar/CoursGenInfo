# Chapter 1

## Installation : 

If linker problem --> install C compiler 

### Linux and MacOs
curl --proto 'https' --tlsv1.2 https://sh.rustup.rs -sSf | sh

Installing a C compiler in macOS : `xcode-select --install`

### Windows
Download and install rustup on the website

### Troubleshooting
`rustc --version`

### Updating and Uninstalling
`rustup update`

To uninstall : `rustup self uninstall`
## HelloWorld
### Create a Project Directory
```
mkdir /projects
cd projects
mkdir hello_word 
cd hello_world
```

### Create the source files
main.rs // the rust files always end up with .rs

### The program : 
```
fn main() {
    println!("Hello, world!"); //the ! show this function is a macro
}
```
### Run the program 
rustc main.rs

./main // or .\main.exe with Windows.

## The function   
- Main : Special, always the first code.
- Between the parentheses, we put the parameters.
- Function are wrapped in curly bracket
- For automated formatter : rustfmt
    
## Indentation 
4 spaces != tab

## Semicolon
 Most lines of rust end with a Semicolon

## Running and compiling
### Running 
 To run a program, we must first compile with a function 

    `rustc main.rs`

To see the binary executable
- LinMac  : ls
- - main    main.rs
- Windows : /dir /B %= the /B option says to only show the files name =%
    
    main.exe    main.pdb    main.rs

### Rust as an ahead-of-time compiled language
You can compile the program and give the executable to someone else and they can run it without having to install Rust

## Hello, Cargo! 
Creating a cargo projects   
`$ cargo new hello_cargo`
`$cd hello_cargo`

List of files created by `cargo new`
- A src Directory
  - main.rs
  - Cargo.toml
- It has created also a git repository with a .gitignore files
  - To override the behavior : cargo new --vcs=git
- A TOML format 
  - Tom's Obvious Minimal language
    - first line : the package
    - then we see the name the version and the edition
    - Finaly we will see the dependencies
- The top-level project Directory
  - Readme files
  - License information
  - TOML files


## Building and running a cargo project
To create an executable : `$ cargo build` 
    The executable is in the debug
    to run it only write  the name of the files 
        Windows
            $ hello_cargo.exe
        LinMac
            $ hello_cargo
        All in one command  
            $ cargo run
Cargo lock 
    Files at the top level  
        This files keeps traks of the exacts versions of dependencies
        This files is always update automaticaly by cargo. 
$ cargo check
    A command that quickly checks if the code is compiling without creating an executable
$ cargo -- release
    Will create an executable in target/release instand of target/Building
    
# Chapter 2 : Programming a guessing game
    Setting up  
        cargo new guessing_game
        cd guessing_game
        Test
            cargo run
    Input/output library
        use std::io; //to use a library, at the begginning of the code
    Storing values with variables
        Create a variable to store user Input   let mut guess = String::new();
            To define : let apples = 5;
            To define a mutable variable we add mut : let mut apples = 5;
    Associated function 
        We can associate a function to a type like in the guessing game 
            let mut guess = String::new();
    Calling the stdin function from the io module define earlier
            if we didnt add the module earlier  
                std::io::stdin
        io::stdin()
            .read_line(&mut guess)
                read_line take what the user types and append it into a string.
                This mean we need a mutable string.
                Here the references is mutable (reference are by default immutable like variables)
        Handling potential failure
            .expect("Failed to read line")'
            Could be read as  : io::stdin().read_line(&mut gues).expect("Failed to read line");
        io::Result (read_line return a io::result that will be handle by the expect method)
            Rust has a number of types named Result 
                The type of result is enumerations or enums
                    Can have a fixed set of possibilities knows as variants.
                Enums are often use with the conditional match
            The purpose of Result types is to encode error-handling information
            Result variant are 
                Ok : operation is successful and inside ok is the successfully generated value
                Err : operation has failed and err contains information about how or why the operation failed
            Expect method to manage io::result.
        Printing values with println! placeholders
            println1("You guessed: {}", guess);
                the bracket are the placeholders and it's will show the value  of the variable by order.
                Exemple 
                    let x = 5;
                    let y = 10;
                    println!("x = {} and y = {}", x, y);
    Generating a Secret Number
        Using a crate
            Crate are use to have more functionality. 
            Library crate cannot be used on its own.
        Opening Cargo.toml 
            Writting beneath [dependencies]
                rand = "0.8.3"
                Cargo use Semantic versioning
                We should read in this example, any version at leat 0.8.3 but below 0.9.0
        To update a crate   
            $ cargo update
        Random numbers
            use rand::Rng;
                Rng trait defines methods that random number generators implement
            rand::thread_rng()
                give us the particular random number generator, one that is local to the current thread of execution and seeded by the operating system
            gen_range() take the range in parameters
                gen_range(1..101) = 1..=100
        Render is own documentation for all the dependencies    
            $cargo doc --Opening
    Comparing the Guess to the Secret Number    
        Ordering type is another enum 
            Variants are : less, greater and equal
        Match expression are made of arms
            Arms are pattern to match against and the code that should be run if the value given to match fits that arm's pattern. 
        Type errors
            We compare the number with a string, but we need a number.
                Rust put by default the i32 (32-bit number)
        let guess : u32 = guess.trim().parse().expect("Please type a number!");
            trim : eliminate the \n and \r
            parse : parses a string into some number    
                The compiler need the size/type of the number   
                    that is why after guess there is ':' and the type (u32 in that case)
    Allowing multiple guesses with looping
        To create an infinite loop
            loop {}
    Quitting after a correct guess  
        break 
            match guess.cmp(&secret_number) {
            Orderning::Less => println!("Too small!");
            Orderning::Greater => println!("Too big!");
            Orderning::Equal => {
                println!("You win!");
                break;
            }
    Handling Invalid Input  
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num;
            Err(_) => continue;
        };

# Chapter 3 : Common programming concepts
### Keywords
Words reserved by the language only.
We cannot use these words as names of variables or functions
### 3. Variables and Mutability
We cannot change the value of a immutable variable once declare. 
To assign a mutable variable : `let mut x = 5;`

#### __Constants__ : 
- Like immutables variables, constants are values that are bound to a name and are not allowed to change
- Compare to variable, a constant cannot becomme mutable with 'mut'
- A constant is not immutable by default, it's always immutable
- Can be declare in any scope, including global scope
- A constant may be set only to a constant expression, not the result of a value that could only be computed at runtime
  - `const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;`

Le hardcodage de constance est utile pour nommer et donner un sens à une variable constance

#### __Shadowing__ :

- When we declare a new variable with the same name as a previous variable
```
    let x = 5;
    let x = x +1;
 ```
See /Rust/doc-rust-lang/Chapter3/VariablesTesting

__Compare to mutable__ :
- More secure if we don't want this variable to change except when we want it to.
- We can change the type of the variable  
- "Shadowing only changes variable within a syntactic scope, while mutation can change an outer variable in a nested scope"



```
let spaces = "    ";
let spaces = spaces.len(); 
```



## 3.2 Data types

Rust is a statically typed language : it must know the types of all variables at compile time.

The compiler can usually infer what type we want to use based on the value and how we use it.

Le compilateur peut habituellement inférer le type en fonction de la valeur de la variable, toutefois, lorsque le compilateur rencontre des cas où il parse une string, le compilateur doit savoir le type des variables à parse.

Exemple : `let guess: u32 = "42".parse().expect("Not a number!");`

Broken exemple : `let guess = "42".parse().expect("Not a number!");`
`error[E0282]: type annotations needed`

###__Scalar types__  :

Represent a __single value__. 

Four primary scalar types : Integers, floating-point numbers, booleans and characters.
        
Integers types : number without a fractional component
- i for signed (negative, zero and positive)
- u for unsigned (positive or zero)
- syntax : i or u + length (ex : i128 for signed 128bit integer). The isize or usize also depend of the architecture, if 32-bit architecture : the arch or top is i32-u32.

Integer can we wrote in : Decimal (98_222), hex (0xff), octal(0o77), binary (0b1111_0000) and byte (b'A') (u8 only) 

Integer __overflow__ behaviors :
- The program will panic at runtime
- In --release (mode), Rust performs two's complement wrapping

 __To handle overflowing manually__ : 
- Wrap with wrapping_* methods (such as wrapping_add)
- Return the None value if there is overflow with the checked
- Returning the value and a boolean indicating wheter there was overflow with the overflowing_* methods
- Saturate at the value's minimum or maximum values with saturating_*methods

#### __Floating-Point types__ : Numbers with decimal point
- Primitive float types : f32 and f64
- f64 is the default type because the modern cpu, it's almost the same speed that with f32
- All floating point are signed
- Represented according to the IEEE-754

 __Numeric Operations__ :
Rust support basic mathematical operations : addition, substraction, multiplication, division and remainder
- Integer division rounds down to the nearest integer
See `/doc-rust-lang/Chapter3/NumericOperation`

#### __The boolean type__    
Value : Can be true or false

Size : one byte
Ex : 
```
let t = true; // Implicit annotation
let f: bool = false; // Explicit type annotation
```


#### __The Character type__

Char is the most primitive Rust alphabetic type
                    
Wrap in ''

Size : A char is four bytes, which is more than ASCII accepted as char in Rust
        
## Compound types  

Primitives compound types in rust : __tuples__ and __arrays__


A general way of grouping a number of values with a variety of types into one compound type.
                
Fixed length : once declared, they cannot grow or shrink in size
                
Creating tuples 
                
Writing a comma-seperated list of values inside parentheses
```
let tup: (i32, f64, u8) = (500, 6.4, 1);
let (x, y, z) = tup; // destructure a tuple value to call individual variables of the tuple
```

__Accessing a tuple directly__ :


```
let tup: (i32, f64, u8) = (500, 6.4, 1);
let five_hundred = x.0;
let six_point_four = x.1;
let one = x.2;
```

tuples without any value is writting (), it's called unit 



Array Type
                Every element of an array must have the same type
                Syntax : let a = [1, 2, 3, 4, 5];
                Array in Rust have a FIXED length
                    To have a flexible list we use a vector not an array. 
                To define the type of element
                    let a: [i32; 5] = [1, 2, 3, 4, 5]; 
                To initialize an array to contain the same value for each element   
                    let a = [3;5]; //same as let a = [3, 3, 3, 3, 3];
                Accessing Array Elements
                    An array is a single chunk of memory of a known, fixed size that can be alocated on the stack. 
                    Accessing thtrough indexing.
                    Ex: let first = a[0]; let second = a[1];
                    Invalid Array Element Access
                        If the index is > than the number of element  = error
                        Rust check during runtime to see if it's higher and show a message error in the terminal. 
        Functions
            Main : entry point of many programs.
            fn : keyword to declare a new function
            function names
                Snake case: all lowercase with underscore to separate words.
            Curly bracket show the bound of the function : where it's start and ended.
        Parameters
            Parameters are special variable that aare part of a function's signature. 
            The concrete value of a parameters are arguments. 
            The parameters and arguments are seperated with comma. 
        Statements and Expressions
            The bodies of function are made up of a series of statements optionnaly ending in an expression. 
            Rust is an expression-based language. 
            Statements : instruction that perform action but do not return a value. 
                Function definitions are also statements
            Expression evaluate a resulting value. 
                Calling a function or a macro is an expression
                A new scope block created with curly bracket is an expression       
                    fn main() {
                        let y = {          //all in this bracket is an expression.
                            let x = 3;
                            x + 1  //expressions do not include ending semicolons, adding a semicolons turn it into a statement and will then not return a value. 
                        };
                        println!("The value of y is: {}", y);
                    }
            Compare to other language such as C or Ruby, we cannot do x= y = 6.
        Functions with Return Values
            We don't name return values but we must declare their type after an arrow (->)
            In Rust, the return value function is the value of the final expression in the block of the body of a function.
                We can use the keyword and specifying a value, but most functions return the last expression implicitly. 
        Comments
            Ignore by the compiler
            Written with // or /* comment */
        Control Flow
            The ability to run some code depending on a if condition or to run some code repeatedly while a condition is true.
            if expression   
                Branch the code depending on condition
                    Called arms
                Start with if keyword
                Condition must be a bool, if the condition isn't a bool, wwe will get an error. 
            Handling multiple conditions with else if
                You can use multiple conditions by combining if and else in an else if expression. 
                    match is better for a lot of else if
            Using if in a let statement
                Because if is an expression, it can be use on the right side of a let statement 
                    let condition = true;
                    let number = if condition {5} else {6};
            Repetition with Loops
                Repeating code with loop    
                    Infinite loop.
                    break to exit the loop
                    continue : to skip to the next iteration
                    break and continue applie to the innermost loop (if there is loops within loops)
                Label loop  
                    'counting_up: loop {} // this loop is called 'counting_up
            Returning Values from Loops 
                we can write it like this : break variables * 2; // on the last line of the loop
            Conditional Loops with while
                While the condition of the loop is true, the loop runs, otherwise it's will breaks
                    Could be done with loop, if and else, but Rust has a buil-in lnaguage construct for that : while loop
                    while number != 0 { 
                        println!("{}", number);
                        number -= 1;
                    }
            Looping Through a Collection with for
                Can be use to iterate over an elements of a collection such as an array. 
                    while index < 5 {
                        println!("the value is : {}", a[index]);

                     index += 1;
                    }
                    or
                    for element in a {
                        println!("the value is: {}", element);
                         
                    }
                Range function and reverse 
                    generate all numbers in sequence starting from one number and ending before another number
                        for number in(1..4).rev(){
                            println!("{}!}, number);
                        }
# Chapter 4 : Understanding Ownership                 
## 4.1 What is Ownership
    Enable Rust to make memory safety guarantess without a garbage collector.
    Set of rules that governs how a Rust program manages memory
        Ways to manage memory
            Garbage collection
            Manually manage memory
            Ownership
    The Stack and the Heap (la pile et le tas)
        Both are parts of memory available to your code to use at runtime
        Stacks :
            stores values in the order it gest them and removes the values in the opposite order. Last in, first out. 
                Adding data : pushing onto the stack
                Removing data : popping of the stack
                All date must have a fixed sized in a stack. 
                Unknown data sized must go in the heap. 
        Heap    
            Less organized
            Putting data through a request with an amount of space. 
                Allocating on the heap : The memory allocators finds an empty spot in the heap big enough and mark it and return a pointer (the address of that location)
                    Take more times than with Stacks
                        
        Ownership rules 
            Each value in Rust has a variable that's called its owner
            There can only be one owner at a time.
            When the owner goes out of scope, the value will be dropped. 
        Variable Scope
            The scope is the range within a program for which an item is valid. 
                A variable is valid when into scope 
                The variable remain valid until out of scope
        The String Type 
            string literals : They are immutable
            String type (the other one) : 
                Manages data allocated on the heap and as such is able to store an amount of text that is unknow to the compiler
            let s = String::from("hello");
            :: operator allow to namespace from
        Memory and Allocation
            string literal : the content is known at compile time
                The text is hardcoded directly into the final executable. 
                Fast and efficient. 
            String type : 
                Mutable and growable
                We need to allocate an amount of memory to the heap unknown at compile time
                    The memory must be requested from the memory allocator at runtime. 
                        Done when we call String::from
                    We need a way to returning this memory to the allocator when we're done with our String. 
                        Only one allocate and only one free
                With rust : the memory is automatically returned once the variable that owns it goes out of scope. 
                    with drop (automatically at the closing curly bracket)
        Ways Variables and Date Interact : *move*
            Not a shallow copy and a deep copy like other language  
            It's a move in this case. 
            For normal data type   
                let x = 5;
                let y = x; 
                Nothing special 
            With String 
                let s1 = String::from("hello");
                let s2 = s1;
                it's not copy it's a ptr. 
                So s2 copy the ptr of s1. 
                When s1 go out of scope, there would be a double free error.  (because Rust automatically calls the drop function and cleans up the heap memory of that variable when it's out of scope.)
                    That's why once we move s1 to s2, s1 doesnt work anymore. 
                Can be mutatated 
                    let mut s = String::from("hello");
                    s.push_str(", world!"); // push_str() appends a literal. 
                    println!("{}", s); // This will print 'Hello World!'
        Ways Variables and Data Interact : *Clone*
            To copy the heap data of the String and not only the stack data : Clone
                let s1 = String::from("hello");
                let s2 = s1.clone();`
        Stack-Only Data : Copy
            This is ok : 
                let x = 5;
                let y = x;
                println!("x = {}, y = {}", x, y);
            Because integer have known size and are entirely stock on the stack.
            Copy trait : if a type implements the Copy Trait, a variable is still valid after assignment to another variable. 
                Rust wont let us add copy trait to a type that has implemented the drop trait. 
            Type that implement copy    
                -All the integer type.
                -Boolean type. 
                -All floating point types. 
                -Character type
                -tuples
        Ownership and Functions
            See passing_var_fn
        Return values and Scope
            Ownership of a variable follow the same pattern every times
                assigning a value to another variables moves it.
                When a variable include data on the heap and it's go out of scope : the value will be clean up by drop (unless ownership of the data has been removed to another variable)
            We can return multiple values with tuple.
            Using a value without transferring ownership : references
    4.2 References and Borrowing
        A reference is like a pointer in that it's an address we can follow to access data stored at that address that is owned by some other variable
            But, unlike pointer : reference guaranteed to point to a valid value of a particular type. 
        The action of creating a reference is called : borrowing
        Reference are immutable by default but we can change that
            see references/src/main.rs
        Mutable references as one big restriction
            you can have only one mutable reference to a particular piece of data at a time
            It prevent data race
                -two or more pointers access the same data at the same time
                -At least one of the pointers is being used to write to the data. 
                -There's no mechanism being used to synchronize access to the data. 
            We can use curly bracket to create a new scope allowing mutiple mutable reference (just not simultaneous one)
                let mut s = String::from("hello");

                {
                    let r1 = &mut s;
                } //r1 goes out of scope here, so we can make a new reference with no problem

                let r2 = &mut s;
            We cannot have a mutable reference while we have an immutable one to the same value. 
                Multiple immutable references is allowed tho, because no one who is just reading the data has the ability to affect anyone else's reading the data. 
        Reference scope
            Start where it is introduced and continues through the last time that reference is used. 
            fn main() {
                let mut s = String::from("hello");

                let r1 = &s; // no problem
                let r2 = &s; // no problem
                println!("{} and {}", r1, r2);
                // variables r1 and r2 will not be used after this point

                let r3 = &mut s; // no problem
                println!("{}", r3);
            }
            Its called Non-Lexical Lifetimes(NLL)
                The ability of the compiler to tell that a reference is no longer being used at a point before the end of the scope. 
            Dangling References
                A pointer that references a location in memory that may have given to someone else--by freeing some memory while preserving a pointer to that memory. 
                See dangling_references 
            Reference Recap
                At any given time, you can have either one mutable reference or any number of immutable references.
                Rerefenreces must always be valid. 
## The Slice Type
    Slices : let you reference a contiguous sequence of elements in a collection rather than the whole collection. 
        Because slices are kind of references, they does not have ownership. 
    Iter (more in dept in Chapter 13)
        A method that returns each element in a collection and that enumerate wraps the result of iter and returns each element as part of a tuple 
            for (i, item) in bytes.iter().enumerate() {}
            The first element of the tuple is the index. 
    The slice type let us use a reference to a portion of the string. 
        let s = String::from("helloworld");
        let hello = &s[0..5];
        let world = &s[6..11];
### Understanding String Literals
        let s = "Hello, world!"; 
            It's a &str : a slice pointing to the specific point of the binary. 
            This is why string literals are immutable, &str is an immutable reference. 
### String Slice as Parameters
    This is less good :
        fn first_word(s: &String) -> &str {
    than this
        fn first_word(s: &str) -> &str {
### Other Slices
Slices work for array too. 
let a = [1,2,3,4,5]
let slice = &a[1..3];
assert_eq!(slice, &[2,3]);

# Chapter 5 : Using Structs to Structure Related Data
## Defining and Instantiating Structs
```
struct User {
    active: bool,
    username: String, 
    email: String, 
    sign_in_count: u64,
}
```
Inside the curly brackets, we define the names and types of the pieces of data which we call fields. 

To create an instance of that struct by specifying concrete values for each of the fields.
```
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("acab1917"), 
        email: String::from("acab1917@oneparty.org"), 
        sign_in_count: 1,
    }; 
}
```
To get a specific value from a strct :
user1.email = String::from("anotheremail@example.com);

The whole instance is mutable or not, they cannot be only a part of it mutable. 
### To create an instance with a function 
```
fn build_user(email : String, username: String) -> User {
    User {
        email: email, 
        username : username,
        active: true,
        sign_in_count: 1,
    }
}
```
The function parameters should have the same name as the struc field to make the more sense as possible. 
For the user Struct, we use String and not a string slice (&str) because we want each instance of this struct to own all of its data and for that data to be valid for as long as the entier struct is valid. 

### Field Init Shorthand Syntax
We can do it even more quickly with the field init shorthand syntax
```
fn build_user(email : String, username: String) -> User {
    User {
        email, 
        username,
        active: true,
        sign_in_count: 1,
    }
}
```
### Struct Update Syntax
Create a new instance of a struct that include most of the values from another instance but changes some. 
```
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("acab1917"), 
        email: String::from("acab1917@oneparty.org"), 
        sign_in_count: 1,
    };

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
    //work and user3 is even faster to write.
    let user3 = User {
        email: String::from("hellokitty1917@acab.urss"),
        ..user1
    };
}
```
### Tuple Structs
Tuple structs have the added meaning the struct name provide but don't have names associated with their field, rather, they just have the types of the fields. 
```
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);
```
### Unit-like Structs Without Any Fields
We can also define structs without any fields. 
Useful when we need to implement a trait on some type but don't have any data that you want to store in the type itself. 

```
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}

```

## An Example Program Using Structs
See structs_02

## Method Syntax
Method are like functions
    We can declare them with fn
    They can have parameters and a return values
    Contains code that's run when the method is called. 
Unlike functions, methods are defined within the context of a struct( or an enum or a trait object and their first parameter is alway self (the instance of the struct the method is being called on))

### Defining Methods
see method_syntax
impl : everything will be associated with the specific type, Rectangle in the example. 
```
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}

```

The self   is short for &self
We can have a mutable self, we just have to wrote &mut self as the first parameter


Why using methods instead of functions : for organization.

The user know where to find all the capabilities of a struct

We can also name a method the same name as a struct's field

```
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }
}
```

### Getters
    When we give methods with the same name as a field we want it to only return the value in the field and do nothing else. 
    Not automatic for Rust struct field

#### Where's the -> Operator 
    In C/C+, there is two operators used for calling methods 
        '.' when we're calling a method on the object directly
        '->' when we are calling the method pointer to the object and need to dereference the pointer first. 
    In Rust, there is no -> operator, instead :
        Automatic referencing and deferenceing
            Rust automatically adds in &, &mut or * so the object matches the signature of the method. So
                p1.distance(&p2); //is the same as :
                (&p1).distance(&p2);
            

#### Associated Function
All functions defined within an impl block are called associated functions

    We can define associated functions without self
        When we don't need and instance of the type to work with. 
        For exemple String::from
        Other exemple : an associated function that would have one dimension parameter and use that as both width and height for creating square Rectangle
```
    fn square(size: u32) -> Rectangle {
        Rectangle{
            width: size,
            height: size,
        }
    }
```
        And we use the :: 
            let sq = Rectangle::square(3)

#### Multiple impl Blocks
```
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```
Or this without a problem (but this one is better, because more clear):
```
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

# Enums and Pattern Matching
Enums for enumerations.
Allow us to define a type by enumerating its possible variants. 

The Rust enums is similar to the algebraic data types of functional languages such as F#, OCaml and Haskell

## Defining an Enum
Exemple, we get IP adresses that can either be v4 or v6. Because there is only a few option available, it make a good enumerate. 
We use a double colon in the creation of an instances 
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

The name of each enum variant that we define also becomes a function that construct an instance of the enum:

    IpAdd::V4() for example is a functionn call that take a String argument and returns an instance of the IpAddr type. 

We get automatically the construction function when we define an enum. 

Everything can go to an enum : strings, numeric types, structs and even another enum.


## The match Control Flow Construct
Match is a control flow construct : compare a value against a series of patterns and then execute code based on which pattern matches. 

To define a match expression that has the variants of the enum as its pattern
```
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,    //this are the arms of the code
        Coin::Nickel => 5,      //each arms is made of a pattern(Coin::Penny) and  some code.
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
No need of curly bracket for small code, but for bigger code it's important. 
```
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        } 

        Coin::Nickel => 5, 
        Coin::Dime => 10,

        Coin::Quarter => 25,
    }
```

### Matching with Option
```
   fn plus_one(x: Option<i32>) -> Option<i32> {
        match x {
            None => None,
            Some(i) => Some(i + 1),
        }
    }

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
```
Rust Matches are exhaustive, if we take out 
None in the match x, we didn't exhaust every last possibility and the code will not be valid. 

### Catch-all Patterns and the _ Placeholder
We can use other or '_' if we need a catch-all patterns. 
Must be at the end. 
```
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    other => move_player(other),
}
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}

```

## Concise Control Flow with if let
For handling values that match one pattern while ignoring the rest.  

#### The long version
```
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {}", max),
    u => (),
}
```

#### The short version
```
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {}", max);
}
```

# 7 Managing Growing Projects with Packages, Crates, and Modules
Packages : A feature of Cargo for building, testing and sharing creates. 
Crates : A tree of modules that produces a library or executable
Modules and use: for controloing the organization, scope and privacy of paths. 
Paths: a ways of naming an item, such as a struct, function or module.

## 7.1 Packages and Crates
Crates are either binary or library. 

Packages is one or more crates that provide a set of functionality. Contains also a Cargo.toml file that describe how to build those crates. 

A crate should group related functionality together in a scope. We can use for example trait of a crate as a function in the main because of the scope (example, Rng of rand can be use with rand or it can be a name of a new function in the main of my program.)

## 7.2 Defining Modules to Control Scope and Privacy
the 'use' keyword : bring a path into scope. 
the 'pub' keyword to make item public. 
the 'as' keyword for external package and the glob operator. 

Modules : 
    - Let us organize a code within a crate into groups for readability and easy reuse.
    - Control the privacy of items (privacy boundary) (public mean it's can be use outside the code and private cannot be use outside the code.)

We put the modules in the library files. 
To create a library files with cargo : cargo new --lib library-name
    
## 7.3 Paths for Referring to an Item in the Module Tree
Path can be either absolute or relative. 
In both case, the path is followed by one or mode identifiers separated with double colons (:)

Modules are privacy boundary, so if we want a function or struct to be private, we can put it in a module. 

All items in Rust are private by default. 
    - Parent module can't use the private items inside child modules
    - Child modules can use the items in their ancestor modules. 

To expose inner parts of child modules to ancestor modules : 'pub' keyword. 

```
pub fn eat_at_restaurant() {}
```

Making the module public with the pub keyword doesn't make the content public. 

```
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {}
```

Privacy for absolute path :
 - we start with crate (the root of our crate's module tree)
 - front_of_house is not pub but the child eat_at_restaurant is defined in the same modules, so we can refer to front_of_house from eat_at_restaurant. 

Privacy for relative path: 
- the path starts from front_of_house. 

### Starting Relative Path with super
We can construct relative paths starting in the parent module by using the 'super' keyword. Like the '..'
Easier if we move different module. 

### Making Structs and Enums Public
We can use 'pub' for structs and enums
But  : 
 - The pub will only make the struct public, not the field of the struct. 
 - We can make all field public with 'pub' case by case.
 - When creating an enum public, all of is variants are public. 

## 7.4 Bringing Paths into Scope with the use keyword
How to bring a path into scope and all their items : with 'use' keyword. 
For example : use crate::front_of_house::hosting
    hosting became a valid name in that scope. 

### Creating Idiomatic 'use' Path
The idiomatic way to bring add_to_waitlist into scope
```
use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
    add_to_waitlist();
    add_to_waitlist();
}
```
The long way to put add_to_waitlist into scope. :
```
use self::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}
```

#### Exception
We caan't bring two item with the same name into scope with 'use' statement. 
In that case we need to do :
```
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    //--snip--
}


fn function2() -> io::Result<()> {
    //--snip--

}
```


### Providing New Names with the as Keyword
If we have two types with the same name, we can use as to give a new local name or alias for the type. 

```
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    //--snip
}


fn function2() -> IoResult<()> {
    //--snip
}
```

### Re-exporting Names with pub use
Using 'use', the name in the new scope is private. 
Re-exporting : We can combine 'pub' and 'use' to enable the code that callls our code to refer to that name as if it had been defined in that code's scope. 

### Using External Package
We need to add the external packages we want to the Cargo.toml. 
For example : rand = "0.8.3"
And we need to write in the code :
use rand::Rng;

The std library is also a crate that's external but we don't need to write it in Cargo.toml, just in the code. 
For example  use std::collections::HashMap;


### Using Nested Paths to Clean Up Large use Lists
Not nested:
```
use std::cmp::Ordering;
use std::io;
```
Nested :
```
use std::{cmp::Ordering, io};
```
The nested paths can be at any level : 
```
use std::io::{self, Write};
```

### The Glob Operator
To defines all public items in a path into scope, we use the glob operator '*'
```
use std::collections::*;
```

## Separating Modules into Different Files 
We just put the other files in the src under name.rs
Then we can use it by written : 
```
mod front_of_house; //using a semi-colon at the place of a block ({} ) tells Rusts to load the contents of the module from another file with the same name as the module.  

pub use crate::front_of_house::hosting;

```


# 8. Common Collections
 - Data structures are called collections.  
 - Collections can contain multiples values types. 
 - They are store in the heap, so we don't need to know the size. 

Popular collection in std Rust : 
 - Vector : store a variable number of values next to each other. 
 - String : collection of characters. 
 - Hash map : allows you to associate a value with a particular key. It's a particular implementation of the more general data structure called a map.

## 8.2 Storing Lists of Values with Vectors
### Creating a New Vector

`let v: Vec<i32> = Vec::new();`

Vectors are implemented using generics (see Chapter 10)

#### vec! Macro
Using vec! let you create a new vector that holds the value you give it. 

`let v = vec![1,2,3]`

### Updating a Vector 
To add an elements : we use the push method. 

```
let mut v = Vec::new();
v.push(5);
v.push(6);
v.push(7);

```

### Dropping a Vector Drops Its Elements
Like for other struct, a vector is freed when it goes out of scope.
```
{
    let v = vec![1,2,3,4];

    //do stuff with v
} // <- goes out of scope and is freed here. 

```

### Reading Elements of Vectors
Two ways : indexing and the get method. 
```
let v = vec![1,2,3,4,5];
let third: &i32 = &v[2];
println!("The third element is {}", third);

match v.get(2) {
    Some(third) => println!("The third element is {}", third),
    None => println!("There is no third element."),
}

```

### Iterating over the Values in a Vector

```
let v = vec![100,32,72];
for i in &v {
    println!("{}", i);
}

//for mut ref

let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50; // '*' deference operator to change the value that the mutable reference refers to. 
    }

```

### Using an Enum to Store Multiple Types
Vector can store values of the same type, so we can use an enum type to have different type in the Vector. 

```
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),

];

```

## Storing UTF-8 Encoded Text with Strings

### What is a String?

In the core language, Rust has one string type, the string slice : &str (often written without the &).
The string slice is a reference to a UTF-8 encoded string type that is store elsewhere. 
Both &str and String are UTF-8 encoded. 
The Rust standard library also include : OsString, OsStr, CString and CStr
String is foir owned and str is for borrowed variant of each of those string type. 

### Creating a New String 
`let mut s = String::new();`

To add some data from the start

```

    let data = "initial contents";

    let s = data.to_string();

    // the method can also works on a literal directly.

    let bonjour = "Bonjour High".to_string();
    println!("{}, {}", s, bonjour);


```

### Updating a String
A String can grow in size and its contents can change. 

#### Appending to a String with push_str and push

```
let mut bonjour = "Bonjour High".to_string();


bonjour.push_str(" as fuck");

println!("{}, {}", s, bonjour);

```

#### Concatenation with the '+' Operator or the format! Macro

```
let s3 = bonjour + &s;
println!("{}, {}", s, s3);
```

The '+' operator use the add method whose signature looks something like : 
    `fn add(self, s: &str) -> String {something something}`

Some language don't take 1 byte each character like cyrilic (they take two)


#### Bytes, Scalar Values and Grapheme Clusters (letter-ish), the three ways to look at strings from a rustecean perspectve. 

Vector : String are stored as a vector. 

Each char doesnt have the same number of bytes for each type of alphabet

### Slicing String

We cannot index a String in Rust. When we slice string we need to tell where it's start and where it's end. 
`let s = &hello[0..4]`

It's dangerous to slices string. 

### Iterating Over 
The best way is to be explicit if we want characters or bytes. 
 Example : 

```

for c in "नमस्ते".chars() {
    println!("{}", c);
}
```
```
for b in "नमस्ते".bytes() {
    println!("{}", b);
}
```

## Storing Keys with Associated Values in Hash Maps
`HashMap<K,V>` 
This type stores a mapping of keys of type K to values of type V using a hashing functino. 
In other programming languages, we call that : hash, map, object, hash table, dictionary, or associative array.

### Creating a New Hash Map

```
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"),10);
scores.insert(String::from("Yellow"),50);
```
We created two teams (keys), one Blue with 10 points 
(values) and one Yellow with 50 points. 

Hash maps data are store on the heap. 

Hash maps are homogenous, all of the keys must be of the same type and all of the values must have the same type

Another way of constructing a hash map : using iterators and the collect method on a vector of tuples, where each tuple consists of a key and its values. 

```
use std::collections::HashMap;

let teams = vec![String::from("Blue"), String::from("Yellow")];
let initial_scores = vec![10,50];

let mut scores: HashMap<_, _> = //let Rust find the type of the data
    teams.ionto_iter().zip(initial_scores.into()).collect

```

### Hash Maps and Ownership

For types that implement the Copy trait like i32, the values are copied into the hash map.
For other types like String, the values will be moved and the hash map will be the owner of those values. 

If we instert references to values into the hash map, the values won't be moved into the hash map. The valuers that the references point to must be valid for at least as long as the hash map is valid. 

### Accessing Values in a Hash Map


```
let team_name = String::from("Blue");
let score = map.get(&team_name); //wrapped in a Some because of get (return an Option<&V>)
```

We can iterate over each key/value pair in a hash map in a similar manner as we do with vectors, using a for loop : 

```
for (key, value) in &scores {
    println!("{}: {}", key, value);
}

```

### Updating a Hash Map
Only one value by key.

#### Overwriting a value : 

```
scores.insert(String::from("Blue"), );
scores.insert(String::from("Blue"), 25);

```

#### Only Inserting a Value if the Key has no Value :
Entry is a special API that return an enum (called Entry) 


```

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```
The or_insert method on Entry : return a mutable reference to the value for the corresponding Entry key if that key existes, and if not, inserts the parameter as the new value for this key and returns a mutable reference to the new value. 

#### Updating a Value Based on the Old Value


```
let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;  //* '*' to deference count */
}

println!("{:?}", map);

```
### Hashing Functions
SipHash is the default hashing function, slower but resistance to Denial of Service(DOS)

# Chapter 9 : Error Handling

## Unrecoverable errors with panic!

When there is an unrecoverable error, Rust has the panic! macro.

"panic! print a failure message, unwind and clean up the stack and then quit."

### Unwinding or aborting

Unwinding : clean the whole stacks but it's take time. 

Abort: will stoop and not clean the stack, it's will need to be done by the operating system. To do this, we add in Cargo.toml :
```
[profile.release]
panic = 'abort'

```

To see the panic in action : 

```
//in doc-rust-lang\panic

fn main() {
    panic!("crash and burn");
}

```

### Using a panic! Backtraces

Accessing an element beyond the end of a vector :
    will cause panic in rust. 
    In C : it's called a buffer overread because it's will read beyond the end of a structure. Can lead to security vulnerabilities. 

"Backtraces in Rust work as they do in other languages: the key to reading the backtrace is to start from the top and read untril you see files you wrote."


```
RUST_BACKTRACE=1 cargo run
```

## Recoverable Errors with Result

Recall : The Result enum as two variants : Ok and Err

```
enum Result<T,E> {
    Ok(T),
    Err(E),
}
```

### Error handling for opening a file with panic!
```
use std::fs::File;

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
}
```
### Matching on Different Errors
For the same operation : opening a file, changing the behavior based on the type of failure (file not created or other problem)

```
use std::fs::File;
use std::io::ErrorKind;


fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error)
            }
        },
    };
}
```

### Shortcuts for Panic on Error: unwrap and expect
Unwrap : will panic! if it's unwrap nothing


```
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").unwrap();
}
```

Expect : will panic! and we can choose the panic message


```
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
}
```

### Propagating Errors 

"When a function's implementation calls something that might fail, instead of handling the error within the function itself, you can return the error to the calling code so that it can decide what to do."


```
use std::fs::File;
use std::io::{self, Read};

fn main() {
    println!("Hello, world!");
}

fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file, 
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}

```

### A Shortcut for Propagating Errors: the '?' Operator

```
fn read_username_from_file_shortcut() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}
```

"The ? placed after a Result values is defined to work in almost the same way as the match expressions we defined before. If the value is an Err, the Err will be returned from the whole function as if we had used the return keyword so the error value gets propagated to the calling code. "






```

```
```
```
