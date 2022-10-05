React Basis by Meta
# Course Introduction
## JavaScript modules, imports - exports
### Exporting Method 1 : Default Exports
Can only have one default export per JavaScript module. 
For example : 
```
function addTwo(a,b) {
    console.log(a+b);
}
export default addTwo;
```
Or 
```
export default function addTwo(a,b){
    console.log(a+b);
}
```
To import it : `import addTwo from ".addTwo";` 
Without the js extension!!!!!
### Exporting Method 2 : Named Exports
For exporting only a partial part of a JavaScript file. 
"In contrast with default exports, you can export as many items from any JavaScrip file as you want."
For example 
```
export function adTwo(a,b){
    console.log(a+b);
}
export function addThree(a+b+c){
    console.log(a+b+c);
}
```
or
```
function adTwo(a,b){
    console.log(a+b);
}
function addThree(a+b+c){
    console.log(a+b+c);
}
export { addTwo, addThree}
```
To import it : `import {addTwo} from "./addTwo";


## React Installation
To create a new React App easily without thinking of the tools 
`npx create-react-app my-app`
To update the build tooling : `npm install react-scripts@latest`

# React Components and Where They Live
## React.js overview
React is "a technology that loads a single web page and performs updates to the DOM on this single web page based on user interaction with this web page in known as a SPA."
React let us 
- "Build and compose components
- High performance rendering
- Component rendering'


SPA : Single-page application. "This is a one-page website where some of the page content changes based on user interaction."
React-js let us make a single-page application.
Advantages of SPA :
- "Rich user interfaces
- Speed
- Scalability and flexibility"

Component-based architecture --> philosophy to "build software based on reusable components of code"
A components is a "stand alone parts of a UI"

## Introduction to functional components
"React provides two types of components : functional components and class components."
Ex of Functional components 
Functional component "must be used as a JSX element"
``` 
function Welcome(){
    return <h1>"Hello"</h1>
}
```
Ex of class components 

```
class Welcome extends React.Component 
{
    render(){
        return <h1>"Hello"</h1>
    }
}
```

Render syntax : "similar to a self-closing tag in HTML".
Ex in index.js
```
ReactDOM.createRoot(
    document.querySelector('#root')
).render(<App />)
```

A function in react (App.js)
```
function App(){
    return(
        <div className='App'>
            <h1>Hello React.</h1> //this is JSX
        </div>
    );
};
export default App;
```

"React is scripted using a special syntax called JavaScript XML or JSX."
"JSX syntax looks very similar to HTML. What ares its advandates is that it allows you to write JavaAcript code inside what looks like HTML elements."
"All component names in React must be capitalized."

## Transpiling JSX
"A browser cannot understand JSX syntax."
Transpiling : "interpreting a programming language and translating it to a specific target language".
With the help of Babel, JSX is transform into plain JS code. 

## Customizing the project
Two approaches to organize by files :
- "Grouping by features
- Grouping by file type"
Better not to nest folders too deep.

className : the "class" attribute is already a reserved keyword in JSX, so to assign a class for the HTML of a React, the syntax is className.

# Component Use and Styling

## Principles of components : Props
Ex :
Index.js :
```
import React from 'react';
import reactDOM from 'react-dom/client';
import App from './App.js'
ReactDOM.createRoot(
    document.querySelector('#root')
).render(<App title="Welcome" />)
```
App.js
```
import React from 'react';
export function App(props) {
    return (
        <h1>{props.title}</h1>
    );
};
```
"Props are passed using JSX syntax : it's helpful to think of props as arguments that components can accept and are passed using JSX".
"Props are like a JavaScript object, in that they can accept many data types including strings, integers, functions, arrays and objects."
We can never change the props in the component. 

## Introducing JSX
Let developper to "write HTML directly inside JavaScript code"
"You can define how React renders a component using a regular JavaScript function"
"The HTML code must be wrapped in a top level element, such as a div tag."

## Props and children
"There is a special prop known as props.children".

## Styling JSX elements
Ways to add style with React

### With a link 
Add a link HTML element in the head of the index.html

### Inline style
Ex :
```
function Promo(props){
    return (
        <div className="promo-section">
            <div>
                <h1 style={{color:"tomato", fontSize:"40px", fontWeight:"bold"}}>
                    {props.heading}
                </h1>
            </div>
            <div>
                <h2>{props.promoSubHeading}</h2>
            </div>
        </div>
    );
}
export default Promo;
```
### Inline with variable
```
function Promo(props){
    const styles = {
        color: "tomato",
        fontSize: "40px"
    }
    return (
        <div className="promo-selection">
            <div>
                <h1 style={styles}>
                    {props.heading}
                </h1>
            </div>
            <div>
                <h2>{props.promoSubHeading}</h2>
            </div>
        </div> 
    );
}
```

## JSX syntax and the arrow function
JSX function declaration
```
function Nav(props){
    return (
        <ul>
            <li>{props.first}</li>
        </ul>
    )
}
```
JSX Function expression
```
const Nav = function(props){
    return (
        <ul>
            <li>{props.first}</li>
        </ul>
    )
}
```
Components as Arrow Functions 
```
const Nav = (props) => {
    return (
        <ul>
            <li>{props.first}</li>
        </ul>
    )
}
```
"The arrow itself can be though of as the replacement for the function keyword.
The parameters that this arrow funtion accepts are listed before the arrow itself"

Ex of the smallest possible function 
`const example = function() {}`
`const example = () => {}`

"Another interesting thing about arrow functinos is the implicit return. However, it only works if it's on the same line of code as the arrow itself. In other words, the implicit return works if the entire component is a single line of code."
`const Nav = () => <ul><li>Home</li></ul>`

### Using Arrow Functions in Other Situations
For the forEach() built-in array method. `[10,20,30].forEach(item => item * 10)`

## Embedded JSX expressions
"Allows JavaScript values to be inserted into HTML of React element"

Ex :
```
function formatName(firstName, surname) {
    return firstName + " "  + surname;
}
```
Embedded Functions Output :
`const result = <p>{ formatName("Jane", "Wilson")}</p>`

Expressions in HTML Attributes
`const url = "photo.png";`
`const result = <img src={url}></img>;`


## Ternary operators and functions in JSX
there is a easier way to do if...else conditional with the ternary operator.
Syntax : `name == Bob ? "Yes, it is Bob" : "I don't know this person";`

### Using ternary expressions in JSX
```
function Example() {
    return (
        <div className="heading">
            <h1>{Math.random() >= 0.5 ? "Over 0.5" : "Under 0.5"}</h1>
            </div>
    );
};
```
### Using function calls in JSX
"Another way to work with an expression in JSX is to invoke a function. Function invocation is an expression because every expression returns a value, and function invocation will always return a value, even when that return value is undefined"
For example with the Math.floor and Math.random
```
function Example2() {
    return (
        <div className="heading">
            <h1>Here's a random number from 0 to 10:
                {Math.floor(Math.random()*10)+1}
            </h1>
        </div>
    );
};
```

```
function Example3() {
    const getRandomNum = () => Math.floor(Math.random()*10)+1
    return (
        <div classname="heading">
            <h1>Here's a random number from 0 to 10: { getRandomnum()} </h1>
        </div>
    );
};
```

## Expressions as props
Ex : 
```
const bool = false;
const str1 = "just";

function Example(props){
    return (
        <div>
            <h2>The value of the toggleBoolean prop is: {props.toggleBoolean.toString()}</h2>
            <p>The value of the math prop is: <em>{props.math}</em></p>
            <p>The value of the str prop is: <em>{props.str}</em></p>
        </div>
    );
};

export default functoin App(){
    return (
        <div className="App">
            <Example 
            toggleBoolean={!bool}
            math={(10+20)/3}
            str={str1 + ' another ' + ' string '}
            />
        </div>
    );
};
```

## Embedding in attributes
```
import avatar from './avatar.png'

function Logo(props){
    const userPic = <img src={avatar}/>
    return userPic;
}

function App() {
    return (
        <div>
            <h1>Hello World!</h1>
            <Logo />
        </div>
    );
}

export default App;
```

# Dynamic events and how to handle them
## Types of events 
"Evevents are the process by which JavaScript interacts with HTML and can occur when the user or the browser manipulated a page."
For examples : clicks, movements or commands. 
### Event Groups
"""
- Clipboard events
- Composition events
- Keyboard events
- Mouse events
- Selection events
- Touch events
- Wheel events
- Animation events
"""

## Eventful issues
using the try...catch syntax to find error easily.

Reminder of JS try..catch :
```
try {
    (5).toUpperCase();
}
catch(e){
    console.log(`Oops, you can't uppercase a number. 
        Trying to do it resulted in the following`, e);
}
```

ReferenceError in React (prop should be props)
```
function NumBillboard(props){
    return(
        <>
            <h1>{prop.num}</h1>
        </>
    )
}
export default NumBillboard;
```

## Syntax for handlers
Event (click a button) --> Event Handler(onClick) --> Action (open menu)

Event handling in HTML 
```
<button id="js-btn"
onclick="clickhandler()">Click me!</button>
```
In React
1. ""Plug into" HTML element on which to listen to an event"
```
const jsBtn = document.getElementById('js-btn')
jsBtn.addEventListener('click', function(){
    console.log('clicked')
})
```
2. "Use addEventListener method on the document object"
```
<button
onclick={clickHandler}>
Click me!</button>
```

## Event handling and embedded expressions
### Handling events using inline anonymous ES5 functions
```
<button onclick={function(){console.log('first example')}}>
    An inline anonymous ES5 function event handler
</button>
```

### Handling events using inline anonymous ES6 functions (arrow functions)
```
<button onClick={() => console.log('second example')}>
    An inline anonymous ES6 function event handler
</button>
```

### Handling events using separate function declarations
```
function App(){
    function thirdExample(){
        console.log('third example');
    };
    return(
        <div className="thirdExample">
            <button onClick={thirdExample}>
                using a separate function declaration
            </button>
        </div>
    );
};
export default App;
```

### Handling events using separate function expressions
```
function App(){
    const fourthExample = () => console.log('fourth example');
    return(
        <div className="fourthExample">
            <button onclick={fourthExample}>
                using a separate function expression
            </button>
        </div>
    );
};
export default App;
```

## JavaScript bind()
"The bind() method creates a new function that, when called, has its this keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called" (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind)

```
var foo = {
    x:3
}
var bar = function(){
    console.log(this.x);
}
bar(); //undefined
var boundFunc = bar.bind(foo);
boundFunc(); //3
``` 
(https://www.smashingmagazine.com/2014/01/understanding-javascript-function-prototype-bind/)

"There are two ways you can get around this [using bind]" (https://reactjs.org/docs/handling-events.html#gatsby-focus-wrapper)

### Public class fields syntax 
```
class LoggingButton extends React.Component {
    //this syntax ensures `this` is bound within handleClick
    handleClick = () => {
        console.log('this is:', this);
    };
    render(){
        return (
            <button onClick={this.handleClick}>
                Click me
            </button>
        );
    }
}
```
(https://reactjs.org/docs/handling-events.html#gatsby-focus-wrapper)

## Synthetic events
Normalize behavior for all browser. 

## Passing a function vs calling a fct
Calling (WRONG in this case)= `return <button onClick={this.handleclick()}>Click me</button>`
Passing = `<button onClick={this.handleClick}>Click me</button>`
### How to pass a paremeter to an event handler then
Like this : `button onClick={() => this.handleClick(id)}/>`
Or : `<button onClick>={this.handleClick.bind(this, id)}/>`

# Data and Events
## Parent-child data flow

Using a centralized point of data : 
- "Allow you to edit multiple items at the same time if they reference the same data, reduces odds of typing errors, and is more efficient when data changes often"
Ex : 
Initialy
```
//Promo Heading Component
function PromoHeading(){  // --> Parent component
    return (
        <h1>80% off sale!</h1> // --> Child component
    )
}
export default PromoHeading;

```
Then
```
//Promo component
const data = {
    heading : "99% off all items!"
    callToAction: "Everything must go!"
}
function Promo(){
    return(
        <div>
        <PromoHeading
        heading={data.heading}
        callToActoin={data.callToAction}
        />
        </div>
    )
}

//PromoHeading component
function PromoHeading(props){
    return (
        <h1>{props.heading}</h1>
        <h2>{props.callToAction}</h2>
    )
}
```

## Children and data
"State data is a component's internal data, which it can control and mutate. Props data is outside of the component and is immutable"

## Hooks
useState hook : Manage the state 
First, import the useState : `import React, {useState} from 'rect';`

Provide any name : `const [showMenu, setShowMenu] = useState(false);`
Without array destructuring :
``` 
var menustate = useState(false);
var showmenu = menuState[0]; //Access first item in array
var setShowMenu = menustate[1]; //Access second item in array
```

"Calling the useState hook does two things : 
- Creates a state variable with an initial value (showMenu)
- Creates a function to set that state variable's value (setShowMenu)"

"Hooks can be called only at the top level and only form React functions"

"In React, state is always referred to the local state of a component."

## What is State
"Data in a component that determines behavior. "

"A child component will receive the data via properties, passing state that's set in a parent stateful component."

useState hook : " Enables use of components for controlling state"

"In React, State is kept in a state of variables. The main way to change State is to alter these variables."

### Stateless component
```
function App(){
    return <h1>A completely stateless component!</h1> //--> only render the text
};
```
### Stateful component
```
function App(){
    const [ word, setWord ] = React.useState("Hello");

    return (
        <div>
            <h1>A state value: {word}</h1> // --> Render a variable
    )
}
```

## Observing state

`const [date, setDate] = React.useState(new Date());`
Where is the date is where we can __access date state__ and the setDate is where we __update state__.


## Managing state
"Lifting state up is about cutting the state from the child component and moving it to the parent component's code, with the intent of making the state available in sibling components".

## Prop drilling
"A situation where you are passing data form a parent to a child component, then to a grand child component, and so on, until it reaches a more distant component further down the component tree, where this data is required."

"The more layers there are, the more repetitive and unnecessary this feels."

## React state management
Context API is easier then Prop drilling. 
To put in place a Context APi, it's require a Context Provider ("component that store the state") which will be use by Context Consumer ("Component that will use the state")

For help wiht immutable variable in Rect : https://github.com/immerjs/immer and https://github.com/kolodny/immutability-helper


## Pure function
From : https://beta.reactjs.org/learn/keeping-components-pure

- Same input, same output
- It's doesn't "change objects or variables that existed before it was called"

### Side Effects
"Components should only *return* their JASX, and not *change* any objects or variables that existed before rendering"

Event Handler can content side effet, because it's the point to change how the website look.
