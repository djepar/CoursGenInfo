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
