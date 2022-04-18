//See chapter 6 Enum

enum IpAddrKind {
    V4(u8, u8, u8, u8), 
    V6(String),
}


fn main() {

    let home = IpAddr::V4(String::from("127.0.0.1"));

    let loopback = IpAddr::V6(String::from("::1"));
    


    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;
    
    route(four);
    route(six);
    
    println!("Hello, world!");
}
