fn main() {
    let x  = five();
    let y = plus_one(x);
    println!("The value of x is: {} and y is {}", x, y);
}

fn plus_one(x: i32) -> i32 {
    x+1
}

fn five() -> i32 {
    5
}
