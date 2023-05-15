use rand::Rng;
use std::io;
use std::cmp::Ordering;

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}


fn main() {
    println!("Guess a number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);
    
   
    
    loop {
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        print_type_of(&guess);
        let guess : u32 = guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        }
        println!("You guessed: {guess}");

        print_type_of(&guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }

}


// My first try without seeing the solution :
// fn user_input() -> io::Result<()> {
//     let mut user_input = "";
//     let stdin = io::stdin();
//     stdin.read_line(&mut user_input)?;
//     if stdin == "allo" {
//         println!("The input is allo");
//     }
//     else {
//         println!("The input is : {}", user_input);
//     }
//     Ok(())
// }