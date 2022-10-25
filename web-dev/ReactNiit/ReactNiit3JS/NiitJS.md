# Week 2

## Filter, transform and aggregate data using Array functions
Data munging (or data wrangling) "is the process of transforming and mapping data from one raw data form into another"
To be more understandable

Array :
- "is a sequential storage of data"
- "is a dynamicallly created object"
- "has indices to access elements"

Diffent from array in other language : 
"""
- An empty array can be created in JavaScript
- Arrays in JavaScript are not of a fixed length
- Dynamic typing in JavaScript creates heterogeneous arras"
"""
Array Operations :
- Intertion
  - push(), unshift()
- Removal
  - pop(), shift(), splice()
- Search
  - find(), indexOf()
- Traversal 
  - forEach()
- Aggregation 
  - reduce()
- Transformation
  - map(), filter(), slice()

Chaining array functions : 
Ex from https://www.geeksforgeeks.org/chaining-of-array-methods-in-javascript/
```
   const products = [
  
        // Here we create an object and each
        // object has a name and a price
        { name: 'dress', price: 600 },
        { name: 'cream', price: 60 },
        { name: 'book', price: 200 },
        { name: 'bottle', price: 50 },
        { name: 'bedsheet', price: 350 }
    ];
    const sale = products.
    .filter(
        product => product.price > 100)
    .map(product => `the ${product.name] is ${product.price/2} rupees`); 

```

### Object in JavaScript
"Stand alone entity with properties and type."
"""
- Object is a collection of properties
- Property is an association between key and value
- Property value can be a data as well as a function
"""

Creating an object with an initializer
```
let myCar = {
    type: "Honda ZXI",
    color: 'red',
    wheels: 4,
    engine : {
        cylinders: 4,
        size: 2.2;
    }
}
```
Creating  using a constructor
```
function Engine(cylinders, size){
    this.cylinders = cylinders;
    this.size = size;
}
function Car(make, model, year, cylinders, size){
    this.make = make;
    this.model = model;
    this.year = year;
    this.engine = new Engine(cylinders, size);
}
let jack_car = new Car("Eagle", "Talon TSi", 1993, 4, 2.2);
```