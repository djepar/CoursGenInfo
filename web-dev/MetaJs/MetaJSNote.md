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