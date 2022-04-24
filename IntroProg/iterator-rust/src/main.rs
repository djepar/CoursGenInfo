//https://www.youtube.com/watch?v=yozQ9C69pNs

fn main() {

   //sugar_coated_iteration 
   for i in vec![1,2,3,4] {
       println!("the value is {} ",i )
    }

    //the sugar-free version of iteration
    let mut iter = vec!["a", "b", "c"].into_iter();
    while let Some(e) = iter.next() {
        println!("the value is {} ",e )

    // Consumes vs borrow
    let vs = vec![1,2,3];
    for v in vs {
        //will consumes vs, owned v
    }
    for v in vs.iter() {
        //borrow vs, & to v
    }
    for v in &vs {
        //equivalent to vs.iter()
    }
}

