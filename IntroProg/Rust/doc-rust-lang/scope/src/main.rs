fn main() { //s is not valid here because it's not yet declared
    let s1 = "hello"; //s is valid from this point forward

    //do stuff with s1

    let s2 = s1; //now s1 no longer valid and s2 is valid
} //this scope is over and s2 is no longer valid.  
