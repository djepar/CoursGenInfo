
fn bonjour(qui: &str) {
    println!("Bonjour {qui}");
}

fn take_five(x: i32) -> i32{
    x - 5
}
fn main() {
    let x = take_five(12);
    println!("The value of x is: {x}");
    bonjour("Ta vie est laide")
}