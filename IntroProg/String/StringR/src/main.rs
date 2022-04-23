/* 
Inspired by https://www.youtube.com/watch?v=Mcuqzx3rBWc
*/
fn main() {

    //creating string 

    let s1 = "Привет миру";
    let s2 = String::from("Привет миру!");
    let s3 = "Привет миру".to_string();
    let s4 = "Привет миру".to_owned();
    let s5 = &s4[..];
    println!("s1 = {} \n s2 = {} \n s3 = {}\n s4 = {} \n s5 = {}", s1,s2,s3,s4,s5);

    //adding string on string

    let mut s: String = String::from("foo");
    s.push_str("bar");
    println!("{}", s);
    s.replace_range( .., "baz");
    println!("{}", s);

    //concatenation

    let s_a = String::from("Hello, ");
    let s_b = String::from("world!");
    let s_ab = s_a + &s_b;
    println!("{}", s_ab);

    let s_aa = ["first", "second"].concat();
    let s_ab = format!("{}{}", "first", "second");
    let s_ac = concat!("first", "second");


    let test= String::from("test");
    let test_okok = test + "okok";
    // format macro, take more time and space because it copy every string. 

    let s_z = String::from("tic");
    let s_y = String::from("tac");
    let s_x = String::from("toe");

    let s = format!("{}-{}-{}", s_z, s_y, "toe");
    println!("{}-{}", s, s_x)
}