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



