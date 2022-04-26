/*
Given a list of integers, use a vector and return the median (when sorted, the value in the middle position) and mode (the value that occurs most often; a hash map will be helpful here) of the list.
*/

//use std::collections::HashMap;



fn main() {
    let mut sorted_lists_integer = vec![1,2,3,4,4,5,6,7,7,8,8,8];
    
     let mut sorted = false;
    while (sorted == false) {
        for i in sorted_lists_integer.iter_mut() {
            sorted = true;
            if *i < (sorted_lists_integer.next()) {
                let mut buff = *i;
                *i = *i+1;
                (sorted_lists_integer.next()) = buff; 
                sorted = false;
            }
        
        } 
    
    }
    
    for i in &mut sorted_lists_integer {
        println!("{}", *i);
    } 
    //let median = median_sorted(sorted_lists_integer);
    
}
/*
fn sorting_list(list : &mut Vec<u32>) {

}

fn median_sorted(list : Vec<u32>) {
    /*let size= list.len();
    println!("size = {}", size);

    if list.len() % 2 == 0 {
        let med = (list[size] + list[(size - 1)])/2;
        println!(" med = {}", med);
    } 
    else {
        let size = size as u32;
        let med = list[size];
        println!(" med if not % 2 == 0 : {}", med )
    } 
    */
}

 */