fn main() {
    let fibo_number = fibo(16);
    println!("{}", fibo_number);
}

fn fibo(n:i32) -> i32{
    if n == 0 { 
        return 0;
    } else if n == 1 {
        return 1 ;
    } else {
        return fibo(n-1) + fibo(n-2)
    }
    
}