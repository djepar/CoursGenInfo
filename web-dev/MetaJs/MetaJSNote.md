Programming with JavaScript by Meta

# Data Type
- Null : Absence of a value
- Undefined : Unassigned value
- Boolean : True or False
- BitInt : 2^53
- Symbol : unique identifier (a bit like a class I guess)

# Conditionals and Loops
## Swith case 
```
switch(light) {
   case 'green':
       console.log("Drive");
       break;
   case 'orange':
       console.log("Get ready");
       break;
   case 'red':
       console.log("Don't drive");
       break;
   default:
       console.log('The light is not green, orange, or red');
       break;
}
```

## Loops
### For loops 
```
for  (var i = 1; i<101; i++) {
    console.log(i)
}
```
### While loops
```
while(counter > 0){
    console.log(counter);
    counter = counter - 1;
}

```

# Arrays, Objects and Functions
## Arrays
```
function listArrayItems(arr) {
    for (var i = 0; i < arr.length; i++) {
        console.log(i, arr[i])
    }
}
var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'];
listArrayItems(colors);
```

## Objects
### Object literal
```
var assistantManager = {
    rangeTilesPerTurn: 3,
    socialSkills: 30,
    streetSmarts: 30,
    health: 40,
    specialAbility: "young and ambitious",
    greeting: "Let's make some money"
}
```
To access an element : `assistantManager.health`
We can change both with : `car["color"] = "green";
and
`car.color = "red"`

## Arrays are Objects
To add a new item at the end of an array : `fruits.push("pears");`
To remove the last item : `fruits.pop();`


## Math objet cheat sheet
Number constants:
- Pi : Math.PI
- Euler : Math.E
- The natual log of 2 : Math.LN2

Rounding methods:
- Math.ceil()
- Math.floor()
- Math.round() --> closest to .5
- Math.trunc() --> "trims the decimal, leaving only the integer"

Arithmetic and calculus methods
- Math.pow(2,3)
- Math.sqrt(16)
- Math.cbrt(8) (cubic root)
- Mat.abs(-10)
- Math.log(), Math.log2
- Math.min(listOfNum) Math.max(listofNum)
- Math.sin(), Math.cos(), Math.tan()

## String cheat sheet
- `greet.length;`
- `greet.charAt(0);`
- `"Wo".concat("rl").concat("d"); `
- `"hohoho.indexOf("h");` -->index of the first matches
- `"hohoho.lastIndexOf("h");` -->index of the last matches
- `"hohoho.split("h");` 

## Object Methods 
A variable can take a function as a value.
"If the function is a properfty of an object, it is then referred to as a method. "
```
var car = {
    car.color = "red";
}
car.turnTheKey = function(){
    console.log("The engine is running")
}
car.turnTheKey();
```
## TypeOf
`console.log(typeof(3.14))`

# Error Handling
## Try and catch
```
try {
    console.log(c+d);
} catch(err) {
    console.log("Something went wrong");
}
```
The advantage is that the program don't stop when an error occurs. 

## Syntax, logical and runtime errors
### ReferenceError
Problem with the variable not being declared or not reachable. 

### SyntaxError
"Any kind of invalid Javascript code will cause a SyntaxError"
Ex : `var a "there's no assignment operator here";

### TypeError
Error related to an invalid type. 
For example popping a number or iterating a boolean. 

### RangeError
"A RangeError is thrown when we're giving a value to a function, but that value is out of the allowed range of acceptable input values."
Ex : `(10).toString(3);

```
function addTwoNums(a,b){
    try {
        if (typeof(a) != "number") {
            throw new ReferenceError("First arg != number")
        }
        else if (typeof(b) != "number") {
            throw new ReferenceError("Second arg != number")
        } else{
            console.log(a+b)
        }
    } catch(err) {
        console.log("Error!", err)
    }

    console.log("It still works")
}
addTwoNums(5,5)
addTwoNums(5,'5')
```

# The functional programming paradigm
## First-class functions
"It means that a functoin in JavaScript is just another value that we can:
- pass to other functions
- save in a variable
- return from other functions"

## Pure Functions
"A pure function returns the exact same results as long as it's given the same values."
"Another rule for a function to be considered pure is that it should not have side-effects. A side-effect is any instnce where a function makes a change outside of itself."

## Scoping with var, let and const
"When you use let and const to declare a variable, it is scoped to the block - even within if statements and loops, like the for or while loops. Therefore, the quantity variable you create will only exist within the for loop."

# Object Oriented Programming
"The thing to remember about Objects s that they exist in a hierarchal structure. Meaning that the original base or super class for everything is the Object class, all objects derive from this class. this allows us to utilize the Object.create() to create or instantiate objects of our classes. 
```
class Animal { /**/}
var myDog = Object.create(Animal)
console.log(Animal)
```
"A more common method of creating objects from classes is to use the new keyword. When using a default or empty constructor method, JavaScript implicitly calls the Object superclass to create the instance."

```
class Animal { /* ...class code here... */ }

var myDog = new Animal()

console.log (Animal)
```

## Constructor 
"Constructor functions, commonly referred to as just "constructors", are special functions that allow us to build instances of these built-in native objects. All the constructors are capitalized."
"To use a constructor function, I must prepend it with the operator new"
`new Date()`


## Creating a classes
```
class Train {
    constructor(color, lightsOn) {
        this.color = color;
        this.lightsOn = lightsOn;
    }
    toggleLights() {
        this.lightsOn = !this.lightsOn;
    }
    lightsStatus() {
        console.log('Lights on?', this.lightsOn);
    }
    getSelf() {
        console.log(this);
    }
    getPrototype() {
        var proto = Object.getPrototypeOf(this);
        console.log(proto);
    }
}
```
### Using polymorphism

```
class HighSpeedTrain extends Train {
    constructor(passengers, highSpeedOn, color, lightsOn) {
        super(color, lightsOn);
        this.passengers = passengers;
        this.highSpeedOn = highSpeedOn;
    }
    toggleHighSpeed() {
        this.highSpeedOn = !this.highSpeedOn;
        console.log('High speed status:', this.highSpeedOn);
    }
}
```
# Advanced JavaScript Features
## De-structuring arrays and objects
Copying a part of an object 
Ex : 
```
let {PI} = Math; 

let introduction = ["Bonjour", "le", "monde"]
let [greeting, pronoun] = introduction;
console.log(greeting);//"Bonjour";
console.log(pronoun);//"le";

//To skip item
let [greeting,, world] = introduction;
```
## For of loops and objects
"A for of loop cannot work on an object directly, since an object is not iterable"
"Arrays are iterable"

### Built-in methods
- Object.keys() : `console.log(Object.keys(car2)); // ['speed', 'color']
- Object.values()
- Object.entries() //return keys and values

Ex : To loop over an object keys 
```
for( key of Object.keys(clothingItem)) {
    console.log(keys, ":", clothingItem[key])
}
```

```
// Task 1
var dairy = ['cheese', 'sour cream', 'milk', 'yogurt', 'ice cream', 'milkshake'] 
function logDairy() {
    for (el of dairy) {
        console.log(el)
    }
}

    // Task 2
const animal = {
    canJump: true
};
const bird = Object.create(animal);

bird.canFly = true;

bird.hasFeathers = true;
function birdCan() {
    for (prop of Object.keys(bird)) {
        console.log(`${prop}: ${bird[prop]}`)
    }
}
birdCan(bird)
// Task 3
function animalCan() {
    for (let i in bird) {
        console.log(`${i}: ${bird[i]}`) //in this one we see canjump!!!!!!
    }
}

animalCan();
```

## Data Structures examples
### Working with arrays in JavaScript
#### forEach() Method : "a function that will work on each array item"
```
const fruits = ['kiwi', 'manga', 'apple', 'pear'];
function appendIndex(fruit, index){
    console.log(`${index}. ${fruit}`)
}
fruits.forEach(appendIndex);
```
#### The filter() method : filters "based on a specific test"
```
const nums = [0,10,20,30,40,50];
nums.filter(function(num){
    return num > 20;
})
```
#### The map method
"This method is used to map each array item over to another array's item, based on whatever work is performed inside the function that is passed-in to the map as a parameter."
```
[0,10,20,30,40,50].map( function(num) {
    return num / 10
})
```
### Working with Objects in JavaScript
#### Object to array 
```
const result = [];
const drone = {
    speed: 100,
    color: 'yellow'
}
const droneKeys = Object.keys(drone);
droneKeys.forEach( function(key) {
    result.push(key, drone[key])
})
console.log(result)
```
### Working with Maps in JavaScript
To create a new map : `new Map();`

```
let bestBoxers = new Map();
bestBoxers.set(1, "The Champion");
bestBoxers.set(2, "The Runner-up");
bestBoxers.set(3, "The third place");

console.log(bestBoxers);
```

### Working with Sets in JavaScript
To create a new set : `new Set();`

"The Set constructor can, for example, accept an array. 
This means that we can use it to quickly filter an array for unique members."
```
const repetitiveFruits = ['apple','pear','apple','pear','plum', 'apple'];
const uniqueFruits = new Set(repetitiveFruits);
console.log(uniqueFruits);
```

### Spread Operator 
"The spread operator is characterized by three dots."

#### Add new members to arrays without using the push() methods
```
let veggies = ['onion', 'parsley'];
veggies = [...veggies, 'carrot', 'beetroot'];
console.log(veggies);
```
#### Convert a string to an array using the spread operator.
```
const greeting = "Hello";
const arrayofCars = [...greeting];
console.log(arrayofChars); // ['H', 'e', 'l', 'l', 'o']
```
#### Copy either an object or an array into a separate one
```
const car1 = {
    speed: 200,
    color: 'yellow'
}
const car 2 = {...car1}

car1.speed = 201

console.log(car1.speed, car2.speed)
```
### Rest operator
"The rest operator allows you to take items from an array and use them to create a separate sub-array."
#### Join arrays using the rest operator
```
const fruits = ['apple', 'pear', 'plum']
const berries = ['blueberry', 'strawberry']
const fruitsAndBerries = [...fruits, ...berries] // concatenate
console.log(fruitsAndBerries); // outputs a single array
```
#### Join objects using the rest operator
```
const flying = { wings: 2 }
const car = { wheels: 4 }
const flyingCar = {...flying, ...car}
console.log(flyingCar) // {wings: 2, wheels: 4}
```





```
// Define a destructuring object with two regular variables and one rest variable:
const { firstName, lastName, ...otherInfo } = {
  firstName: "Oluwatobi",
  lastName: "Sofela", 
  companyName: "CodeSweetly",
  profession: "Web Developer",
  gender: "Male"
}

// Invoke the otherInfo variable:
console.log(otherInfo);

// The invocation above will return:
{companyName: "CodeSweetly", profession: "Web Developer", gender: "Male"}
```
(from https://www.freecodecamp.org/news/javascript-rest-vs-spread-operators/)

### Rest parameters 
"The rest arameter syntax allows a function to accept an indefinite number of arguments as an array, providing a way to represent variadic function in JavaScript" (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
```
function sum(...theArgs) {
  let total = 0;
  for (const arg of theArgs) {
    total += arg;
  }
  return total;
}

console.log(sum(1, 2, 3));
// expected output: 6

console.log(sum(1, 2, 3, 4));
// expected output: 10
```
## Arrow Function
``` 
//Normal function 
function sum(a,b) {
    return a + b
}
//Arrow functions
let sum 2 = (a,b) => a+b


//Normal function
function isPositive(number){
    return number >= 0
}
//Arrow function 
let isPositive = number => number >= 0

//Normal function
function randomNumber() {
    return Math.random
}
//Arrow function
let randomNumber() = () => Math.random
```
# JavaScript in the Browser
## JavaScript modules
Export with `export {name, draw, functionArea, reportPerimeter};`
To import : `import {name, draw, functionArea, reportPerimeter} from 'path';` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

## JavaScript DOM manipulation
"The DOM is an in-memory representation of the active HTML document. Any changes made are local and do not affect the document stored on the webserver."

## JavaScript selectors
`document.querySelector('p')`
`document.querySelectorAll('a')`
`document.getElementbyId('heading')`
`document.getElementsbyClassName('powershell')`

## Event Handling
User-triggered events : 
```
<button type="button" class="btn btn-lg btn-primary" onclick="clickHandler()">
Primary Button
</button>
<script>
    const target = document.querySelector('body')
    function handleClick() {
        console.log('clicked the body')
    }
    target.addEventListener('click', handdleClick)
</script>
```
## Create content from output
```
let answer = prompt('What is your name?');
if (typeof(answer) === 'string') {
    var h1 = document.createElement('h1')
    h1.innerText = answer;
    document.body.innerText = '';
    document.body.appendChild(h1);
}
```

## Moving data around on the web
"data interchange format based on Javascript objects." --> JSON (JavaScript Object Notation)

### JSON rules 
- Must be parse properly, otherwise won't be parse as a JS object. 
- "Only a subset of values in JavaScript can be properly stringified to JSON and parsed from a JavaScript object into a JSON string."
- "These values include :
    - primitives value : strings, numbers, bolleans, null
    - complex values: objects and arrays (no functions!)
    - Objects have double-quoted strings for all keys
    - Properties are comma-delimited both in json objects and in JSON arrays, just like in regular JavaScript code'
    - String properties must be surronded in double quotes.
    - Number properties are represented using the regular JavaScript number syntax
"
Ex ; `'[{ "color": "blue" }, {"color: "red"}]'`

### To manipulated a JSON object
```
const jsonStr = '{"greeting":"hello"}'
JSON.parse(jsonStr) // {greeting:'hello'}
const aPlainObj = JSON.parse(jsonStr)
const = data = {firstName : "John", lastName = "Doe"}
JSON.stringify(data) // create the json of it. 