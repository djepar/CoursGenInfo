# Chapter 1

## Installation : 
### Linux and MacOs
curl --proto 'https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
### Windows
Download and install rustup on the website

### Troubleshooting
rustc --version

## HelloWorld
### Create a Project Directory
mkdir /projects
cd projects
mkdir hello_word 
cd hello_world
    
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
        $ cargo new hello_cargo
        $cd hello_cargo
    List of files created by this command
        A src Directory
            With a main.rs
        a Cargo.toml
        It has created also a git repository with a .gitignore files
            To override the behavior : cargo new --vcs=git
        A TOML format 
            Tom's Obvious Minimal language
            first line : the package
            then we see the name the version and the edition
            Finaly we will see the dependencies
        The top-level project Directory
            Readme files
            License information
            TOML files
    Building and running a cargo project
        $ cargo build
            to create an executable 
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

Chapter 3 : Common programming concepts
    Keywords
        Words reserved by the language only.
        We cannot use these words as names of variables or functions
    Variables and Mutability
        A immutable variable once bound to a name can't change that value.
        To have a mutable variable 
            let mut x = 5;
    Constants
        Like immutables variables, constants are values that are bound to a name and are not allowed to change
        Compare to variable, a constant cannot becomme mutable with 'mut'
        A constant is not immutable by default, it's always immutable
        Can be declare in any scope, including global scope
        A constant may be set only to a constant expression, not the result of a value that could only be computed at runtime
            const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
    Shadowing
        When we declare a new variable with the same name as a previous variable
            let x = 5;
            let x = x +1;
        Compare to mutable  
            More secure if we don't want this variable to change except when we want it to.
            We can change the type of the variable  
                let spaces = "    ";
                let spaces:u32 = spaces.len(); //pas sur si c'est bon
    Data types  
        Rust is a statically typed language : it must know the types of all variables at compile time.
        The compiler can usually infer what type we want to use based on the value and how we use it. 
                
        Scalar types    
            Represent a single value. 
            Rust has four primary scalar types : Integers, floating-point numbers, booleans and characters.
                Integers types : number without a fractional component
                    i for signed
                    u for unsigned
                    number for number of bit
                    i8 u8, etc until 128 bit
                    arch isize usize
                    Integer can we wrote in 
                        Decimal, hex, octal, binary and byte (u8 only)
                    Integer overflow
                        Two behaviors
                            The program will panic at runtime
                            In --release (mode), Rust performs two's complement wrapping
                    To handle overflowing
                        Wrap with wrapping_* methods (such as wrapping_add)
                        Return the None value if there is overflow with the checked
                        Returning the value and a boolean indicating wheter there was overflow with the overflowing_* methods
                        Saturate at the value's minimum or maximum values with saturating_*methods
                Floating-Point types    
                    Numbers with decimal point
                        f32 and f64 are the two primitive float types.
                            f64 is the default type because the modern cpu, it's almost the same speed that with f32
                        All floating point are signed
                        Represented according to the IEEE-754
                Numeric Operations
                    Rust support basic mathematical operations : addition, substraction, multiplication, division and remainder
                        Integer division rounds down to the nearest integer
                The boolean type    
                    Can be true or false
                    Size : one byte
                    Ex : let t = true;
                    Explicit type annotation
                        let f: bool = false; 
                The Character type      
                    Char is the most primitive rust alphabetic type
                    Wrap in ''
                    A char is four bytes 
                    More than ASCII accepted as char in Rust
        Compound types  
            Primitives compound types in rust : tuples and arrays
            tuples  A general way of grouping a number of values with a variety of types into one compound type.
                Fixed length : once declared, they cannot grow or shrink in size
                Creating tuples 
                Writing a comma-seperated list of values inside parentheses
                let tup: (i32, f64, u8) = (500, 6.4, 1);
                let (x, y, z) = tup; // destructure a tuple value to call individual variables of the tuple
                Accessing a tuple directly
                    let tup: (i32, f64, u8) = (500, 6.4, 1);
                    let five_hundred = x.0;
                    let six_point_four = x.1;
                    let one = x.2;
                tuples without any value is writting (), it's called unit Type
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
            Expression evaluate ti a resulting value. 
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
            Written with //
        Control Flow
            The ability to run some code depending on a if condition or to run some code repeatedly while a condition is true.
            if expression   
                Branch the code depending on condition
                    Called arms
                start with if keyword
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
    Enable rust to make memory safety guarantess without a garbage collector.
    Set of rules that governs how a rust program manages memory
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

Why using methods instead of functions : for organization
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
    We can do this :
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
Allow us to define a type by enuymerating its possible variants. 
The Rust enums is similar to the 
    algebraic data types of functional languages such as F#, OCaml and Haskell

## Defining an Enum
Exemple, we get ip adresses that can either be v4 or v6. Because there is only a few option available, it make a good enumerate. 

