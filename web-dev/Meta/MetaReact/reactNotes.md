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

Transpiling : "interpreting a programming language and translatint it to a specific target language".