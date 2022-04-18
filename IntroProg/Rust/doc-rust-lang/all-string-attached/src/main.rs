fn main() {

    let data = "initial contents";

    let s = data.to_string();

    // the method can also works on a literal directly.

    let mut bonjour = "Bonjour High".to_string();
   

    bonjour.push_str(" as fuck");

    println!("{}, {}", s, bonjour);

    let s3 = bonjour + &s;

    println!("{}, {}", s, s3); //we cannot use bonjour anymore 
}
