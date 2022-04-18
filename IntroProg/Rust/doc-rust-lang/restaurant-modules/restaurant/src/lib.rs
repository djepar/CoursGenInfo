#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
mod back_of_house {
    pub struct Breakfast {
        pub toast: String, 
        seasonal_fruit: String,
    }
    pub enum Appetizer {
        Soup, 
        Salad,
    }
    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}


mod front_of_house;

pub use crate::front_of_house::hosting

use crate::front_of_house::hosting;
//the relative path would have been like : 
// use self::front_of_house::hosting;

pub fn eat_at_restaurant() {
    let mut meal = back_of_house::Breakfast::summer("rye")
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);
    
    //the next line cannot compile because it's not public. 
    //meal.seasonal_fruit = String::from("blueberries");

    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
    

    //absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    //relative path
    front_of_house::hosting::add_to_waitlist();

    hosting::add_to_waitlist();
    //add_to_waitlist(); if we did use crate::front_of_house::hosting::add_to_waitlist;
}

