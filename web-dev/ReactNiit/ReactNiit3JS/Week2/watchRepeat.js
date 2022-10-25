
// Creating an Array
let carMake = new Array("nissan", "bonjour", "BMQ")

console.log(carMake);

// Adding an element at the end
carMake.push("allo");

console.log(carMake);

// Adding an element at the start of the array
carMake.unshift("Audi");
carMake.unshift("Velcro");

console.log(carMake);

// Removing the element at the end

carMake.pop();
console.log(carMake);

// Removing the element at the front
carMake.shift();
console.log(carMake);


// New array 
let cars = []
let make = "Eagle";
let model = "Talon TSI";
let color = "Blue";

let car = [];
car.push(make);
car.push(model);
car.push(color);
cars.push(car);
console.log(cars);

