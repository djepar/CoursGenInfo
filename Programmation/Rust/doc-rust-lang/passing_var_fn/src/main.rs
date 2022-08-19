fn main() {
    let s = String::from("hello"); //s comes into scopes

    takes_ownership(s);  //s's value moves into the function
                        //no longer valid here
    
    let x = 5;  //x comes into scope

    makes_copy(x); // x would move into the function, 
                    //but i32 is Copy, so it's okay to still
                    // use x aftwerward

    println!("x: {}", x);

} // x goes out of scope, then s. 

fn takes_ownership(some_string: String) { // some_string comes into scope
    println! ("{}", some_string);
} //Here some_string goes out of scope and 'drop' is called. 
    //The backing memory is freed. 

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer); 
} //Here, some_integer goes out of scope. Nothing special happens. 




