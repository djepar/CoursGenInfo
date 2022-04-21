fn main() {
    let x = 5;
    println!("The value of x is  : {}", x);
    let x = 6; //shadowing the first x
    println!("The value of x is  : {}", x);

    //addition
    let sum = 5 + 10;
    println!("{}",sum);
    //substraction

    let difference = 95.5 - 4.3;
    println!("{}",difference);
    // multiplication

    let product = 4 * 30;
    println!("{}",product);
    //division
    let quotient = 56.7 / 32.2;
    let floored = 2 / 3; //results in 0;
    println!("{}",quotient);
    println!("{}",floored);
    //remainder 

    let remainder = 43 % 5;
    println!("{}",remainder);
}

