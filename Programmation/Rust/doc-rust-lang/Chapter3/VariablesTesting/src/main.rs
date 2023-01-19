fn main() {
    println!(" ****** Mut vs Shadowing :  Exercice 1 --> Scope*****");

    //Variable
    let x = 5; 
    println!("The value of x is : {x}");
    //Mutable variable
    let mut y = 5;
    println!("The value initial mutable variable of y is : {y}");
    y = 6;
    println!("y = 6");
    println!("The value of y is now: {y}");


    // Shadowing 
    let z = 5;
    println!("The value before shadowing of z is : {z}");
    let z = z + 6;
    println!("The value once shadowing z is z + 6 : {z}");
    {
        println!(" ****** Inside the nest *****");
        println!("Inside, z is : {z}");       
        println!("let z = z + 3");       
        
        let z = z + 3;
        println!("The value in the nested shadowing of z is z + 3 : {z}");       
    }
    println!(" ****** Outside the nest *****");

    println!("The value outside of the nested once shadowing of z is : {z}");


    println!(" ****** Mut vs Shadowing : Exercice 2 --> Changing Type *****");
    println!("--- Shadowing ---");
    println!("let space_shadowing = '    ';  ");
    let space_shadowing = "       "; 
    println!("let space_shadowing = space_shadowing.len();") ;
    let space_shadowing = space_shadowing.len();
    println!("println!({space_shadowing}");
    println!("{space_shadowing}");
    println!("-- Mutable : !!!!!generate error!!!! --");
    println!("let mut spaces_Mut = '   '");
    let mut spaces_Mut = "   ";
    //spaces = spaces.len();
    println!("spaces = spaces.len()");
    println!("error[E0308]: mismatched types");

    

}
