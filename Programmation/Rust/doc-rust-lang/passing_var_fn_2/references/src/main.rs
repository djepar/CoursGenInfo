fn main() {
    let s1 = String::from("Hello");

    let len = calculate_length(&s1); 

    println!("The length of '{}' is {}. ", s1, len);

    let mut s2 = String::from("hello");


    change(&mut s2);
    println!("{}", s2);
}

fn calculate_length(s: &String) -> usize {  //it's important, the paremeter is with an ampersand because it's take a reference

    s.len()
}  //Here, s goes out of scope. But because it does not have ownership of what
  //it refers to, nothing happend

/* fn change(some_string: &String) {
    some_string.push_str(",world");
} */   //this show that reference are immutable

fn change(some_string: &mut String) {
    some_string.push_str(",world");
}