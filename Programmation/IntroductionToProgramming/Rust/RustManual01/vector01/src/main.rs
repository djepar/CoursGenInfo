fn main() {
    let v = vec![1,2,3,4,5]; //no need to give the type in that cas.e 

    let third: &i32 = &v[2];
    println!("The third element is {}", third);

    match v.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }



    let mut v2: Vec<i32> = Vec::new();


    {
        let mut i = 0;
        while i < 5 {
            v2.push(i);
            i+= 1;
        }
        v2.pop();
    }
    for i in &v2 {
        println!("{}", i);
    }
    #[derive(Debug)]
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }
    
    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    
    ];

    for j in &row {
        println!("{:?}", j);
    }

}
