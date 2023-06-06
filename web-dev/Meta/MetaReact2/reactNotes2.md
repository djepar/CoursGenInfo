Advanced React by Meta

# Rendering Lists in React
## Transforming lists in JavaScript
map() method : "a way to ignore everything that you do not want displayed on screen and extract only the data that your users care about."

Example of using map() : 

```
const topDesserts = data.map(dessert => {
  return {
    content : `${dessert.title} - | ${dessert.description}`,
    price : dessert.price,
  }
})
```

## Render a simple list component
```
  const listItems = data.map(dessert => {
    const itemText = `${dessert.title} - ${dessert.price}`
    return <li>{itemText}</li>
  })
```

## What are Keys in React?
React use the diffing algorithm to perform the necessary change. But sometime, there's ambiguity that need to be fix by the coder.
For example : 
```
<ul>
    <li>Beer</li>
    <li>Wine</li>
</ul>

// Then we add another li at the end (react is ok with that because it's at the end):  


<ul>
    <li>Beer</li>
    <li>Wine</li>
    <li>Cider</li>
</ul>

// Then we add another li at the start (react is not ok with that because it's at the start):  


<ul>
    <li>Cider</li>
    <li>Beer</li>
    <li>Wine</li>
</ul>
```

In React keys :
- "Keys instruct React on how to treat a specific element when updates happen"
- "Keys are identifiers that help React determine which items have changed, are added or are removed"
- "Keys instruct React on whether a specific element's internal state should be preserved when updates happen"

Same example, but with keys :
```

<ul>
    <li key="beer">Beer</li>
    <li key="wine">Wine</li>
</ul>

// Became ->

<ul>
    <li key="cider">Cider</li>
    <li key="beer">Beer</li>
    <li key="wine">Wine</li>
</ul>
```

Rules for keys : 
- "Use stable identifiers"
- Unique IDs
  - Shouldn't be neither random nor index

# Forms in React
## What are controlled components?
Controlled components : "a set of components that offer a declarative application programming interface or API to enable full control of the state of form elements at any point in time using React state"

State delegation is done through the value prop.

Value : "A special property to determine input content"

To create a controlled component : local state + value prop

To get update use the second prop : onChange callback who receives an event parameter

```
handleChange(event){
  setValue(event.target.value);
}

<form onSubmit={handleSubmit}>
...
</form>
handleSubmit(event){
  validate(value);
  event.preventDefault();
}
```

## Controlled components vs Uncontrolled components
###  Uncontrolled Inputs 
"Uncontrolled inputs are like standard HTML form inputs" :

```
const Form = () => {
  return (
    <div>
      <input type="text" />
    </div>
  );
};
```

It's in the DOM itself. We get the value by using React ref :

```
const Form = () => {
  const inputRef = useRef(null);

  const handleSubmit = () => {
    const inputValue = inputRef.current.value;
    // Do something with the value
  }

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} type="text" />
    </form>
  );
};
```


### Controlled Inputs
Controlled inputs : "accept their value as a prop and a callback to change that value. That implies that the value of the input has to live in the React state somewhere. Typically, the component that renders the input (like a form component) save that in its state" :

```
const Form = () => {
  const [value, setValue] = useState("");

  const handleChange = (e) => {
    setValue(e.target.value)
  }

  return (
    <form>
      <input
        value={value}
        onChange={handleChange}
        type="text"
      />
      </form>
  );
};
```

### The file input type 
"There are some specific form inputs that are always uncontrolled, like the file input tag."

## Create a Controlled Form Component
"The two props to add when creating a controlled range are : `value` and `onChange`. The `value` prop is used to hook the local state up and `onChange` prop is used to receive the changes and update the state accordingly"

# React Context
Props : passed to the components
  short for properties
  Components configurations
  immutable


State : Managed within the component
  "this object is a way to allow react to determine when it should re-render a component. 
  A component react is set up so that any change to the value served in the state object will trigger a rear ender of a given component states."
  Start with a Default value then change with user event
  A state is a snapshot or "a serialize double representation of one point in time"
  State is optional (and normally will slow your program if use too much   )


"The props and state together constitute the raw data that the html output derives from both props and states are plain Js objects and are deterministic."

**Stateless components** : "have only props and no state there's not much going on besides the render function and all their logic revolves around the props they receive"
  Easy to follow and test

**Stateful components** : both props and state
  Can be use for : 
    - client-server communication
    - data processing
    - Responding to user events

## Context
An alternative to passing data

Use for the **props drilling problem**, when passing data through all component tree levels (even components that do not need it)

** Context application programming interface (Context API)** :
  - Alternative way to pass data
  - Useful for global state

## How re-rendering works with Context
"When it comes to the default behavior of React rendering, if a component renders, React will recursively re-render all its children regardless of props or context."

"Imagine the following component structure, where the top level component injects a Context provider at the top : 
`App (ContextProvider) > A > B > C`
```
const App = () => {
  return (
    <AppContext.Provider>
    <ComponentA />
    </AppContext.Provider>
  );
};
const ComponentA = () => <ComponentB />;
const ComponentB = () => <ComponentC />;
const ComponentC = () => null;
```
"
It's will re-render like this : 
`App (contextProvider) -> A -> B -> C`

Can be bad for the performance. "To mitigate this issue, you cna make use of the top level API React.memo()."

"If your component renders the same result given the same props, you can wrap it in a call to `React.memo` for a performance boost by memoizing the result"

**Memoization** : "is a programming technique to accelerates performance by caching the return values of expensive function calls. "

```
const App = () => {
  return (
    <AppContext.Provider>
    <ComponentA />
    </AppContext.Provider>
  );
};
const ComponentA = React.memo(() => <ComponentB />);
const ComponentB = () => <ComponentC />;
const ComponentC = () => null;
```

"A good rule of thumb is to wrap the React component right after your context provider with `React.memo`."

New scenario from the previous example "where the context value that gets injected is defined as an object called value with two properties, 'a' and 'b', being both strings. Also, ComponentC is now a consumer of context, so any time the provider `value` prop changes, `ComponentC` will re-render. "

```
const App = () => {
  const value = {a: 'hi', b: 'bye'};
  return (
    <AppContext.Provider value={value}>
    <ComponentA />
    </AppContext.Provider>
  );
};
const ComponentA = React.memo(() => <ComponentB />);
const ComponentB = () => <ComponentC />;
const ComponentC = () => {
  const contextValue = useContext(AppContext);
  return null;
};
```

"imagine that the value prop from the provider changes to `{a: 'hello', b: 'bye'}`.

If that happens, the sequence of re-render would be : 

`App (ContextProvider) -> C`"

The problem is the ComponentC get re-rendered even though the provider value doesn't seem to change (ish paraphrasé)

"Because object comparison in JavaScript is done by reference. Every time a new re-render happens in the App component, a new instance of the value object is created, resulting in the provider performing a compaison agaisnt its previous value and determining that it has changed, hence informing all context consumers that they should re-render." 

To resolve this we use `useMemo`


```
const App = () => {
  const a = 'hi';
  const b = 'byes';
  const value = useMemo(() => ({a,b}), [a,b]);
  return (
    <AppContext.Provider value={value}>
    <ComponentA />
    </AppContext.Provider>
  );
};
const ComponentA = React.memo(() => <ComponentB />);
const ComponentB = () => <ComponentC />;
const ComponentC = () => {
  const contextValue = useContext(AppContext);
  return null;
};
```


# Getting started with hooks
## Revising useState hook
Array destructuring : "a way to get individual items from an array of items and save thoes individual items as separate components"

Exemple : 
```
let veggies = [parsley, onion, carrot];
const [v1, v2, v3] = veggies;
```
We can give any name we want to the items of the new array. 

Object destructuring : we have to destructured a property of an object using that exact properties name as the name of the destructured variable. 

For that reason, React use a Array data structure used as return value of **useState hook**

## Working with complex data in useState

How to use object as state variables when using useState

Intuitively we could try "of holding state in an object and updating it based on user-generated events" 

```
import { useState } from "react"; 
 
export default function App() { 
  const [greeting, setGreeting] = useState({ greet: "Hello, World" }); 
  console.log(greeting, setGreeting); 
 
  function updateGreeting() { 
    setGreeting({ greet: "Hello, World-Wide Web" }); 
  } 
 
  return ( 
    <div> 
      <h1>{greeting.greet}</h1> 
      <button onClick={updateGreeting}>Update greeting</button> 
    </div> 
  ); 
} 
```

It's costly because it's change the whole object. 

### The suggested approach

"to copy the state object and then update the copy." with -> `...`

```
import { useState } from "react"; 
 
export default function App() { 
  const [greeting, setGreeting] = useState({ greet: "Hello, World" }); 
  console.log(greeting, setGreeting); 
 
  function updateGreeting() { 
    const newGreeting = {...greeting}; 
    newGreeting.greet = "Hello, World-Wide Web"; 
    setGreeting(newGreeting); 
  } 
 
  return ( 
    <div> 
      <h1>{greeting.greet}</h1> 
      <button onClick={updateGreeting}>Update greeting</button> 
    </div> 
  ); 
} 
```

### Updating the state object using arrow functions 

How to change the state object when only one propertie change and the rest remain unchanged.

``` 
import { useState } from "react"; 
 
export default function App() { 
  const [greeting, setGreeting] = useState( 
    { 
        greet: "Hello", 
        place: "World" 
    } 
  ); 
  console.log(greeting, setGreeting); 
 
  function updateGreeting() { 
    setGreeting(prevState => { 
        return {...prevState, place: "World-Wide Web"} 
    }); 
  } 
 
  return ( 
    <div> 
      <h1>{greeting.greet}, {greeting.place}</h1> 
      <button onClick={updateGreeting}>Update greeting</button> 
    </div> 
  ); 
} 
```

## Side Effects 

Pure function  : 
  - had no side effects
  - Always return the same out put

Example of a pure function : 
```
function EstablishedYear(props) {
  return <h1>Established year: {props.year}</h1>
}
function App() {
  return <EstablishedYear year={2030}/>

}
export default App;
```

Impure function : 
  - has side effects
  - Performs a side effect 
      - invoke console.log
      - invoke fetch
      - invoke geolocation

Example of an impure function
```
function ShoppingCart(props) {
  const total = props.count * props.price;
  console.log(total)
  return <h1>Total: {total}</h1>
}
export default function App(){
  return (
    <ShoppingCart items={5} pricePerItem={10}/>
  )
}
```
## useEffect hoook


With useEffect hook
```
function ShoppingCart(props) {
  const total = props.count * props.price;
  useEffect(()=> console.log(total), []);

  return <h1>Total: {total}</h1>
}
```


"The code you place inside the `useEffect` hook always runs after your component mounts or, in other words, after React has updated the DOM"

If there is no second argument, "the effect will run after every render." : 

```
useEffect(() => {
  document.title = "Little Lemon";
});
```

"A way to instruct React to skip applying an effect is passing an array as a second parameter to `useEffect` : 

```
useEffect(() => {
  document.title = `Little Lemon, v${version}`;
}, [version]); // only re-run the effect if version changes.
```

"React doesn't limit you in the number of effects your component can have. In fact, it encourages you to group related logic together in the same effect and break up unrelated logic into different effects."

``` 
function MenuPage(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    document.title = 'Little Lemon';
  }, []);

  useEffect(() => {
    fetch(`https://littlelemon/menu/${id}`)
    .then(response => response.json())
    .then(json => setData(json));
  }, [props.id]);
}
```

## Effects with Cleanup

To avoid memory leak, we need to clean up resources when some side effects are in effect. 

Example ("you may want to set up a subscription to an external data source. In that scenario, it is vital to perform a cleanup after the effect finishes its executions")

```
function LittleLemonChat(props) { 
  const [status, chatStatus] = useState('offline'); 

  useEffect(() => { 
    LemonChat.subscribeToMessages(props.chatId, () => setStatus('online')) 

    return () => { 
      setStatus('offline'); 
      LemonChat.unsubscribeFromMessages(props.chatId); 
    }; 
  }, []); 

  // ... 
} 
```

# Rules of Hooks and Fetching Data with Hooks

## Hooks rules

- Only call hooks from a React component function
  - This mean we should not call hooks from JS function, but only from React component
  - The setState can be use wherever
- Only call hooks at the top level
  - "The second rule means you must call your hooks before a return statement outside of loops, conditions or nested functions."
- You can call multiple state of effect hooks
  - "There can be multiple hook calls as long as they are always in the same order."
- Make multiple hook calls in the same sequence
  - The condition must be inside de hook.

## Things to know before fetching data

"Fetch is used to make a server requests to retrieve some JSON data from it. 
Fetch API is a set of functionalities that we have at our disposal to use in JavaScript to make such server request."

"When JavaScript uses the fetch function it is delegating duties to an external API so that it can continue its process. This is known as asynchronous JavaScript"

## Data fetching using hooks

"there is only one more ingredient that you need to keep in mind when working with React, namely, that fecthing data from a third-party API is considered a side-effect.
[...]
you need to use the useEffect hook to deal with using the Fetch API calls in React."

```
import { useState, useEffect } from "react"; 
 
export default function App() { 
  const [btcData, setBtcData] = useState({}); 
  useEffect(() => { 
    fetch(`https://api.coindesk.com/v1/bpi/currentprice.json`) 
      .then((response) => response.json()) 
      .then((jsonData) => setBtcData(jsonData.bpi.USD)) 
      .catch((error) => console.log(error)); 
  }, []); 
 
  return ( 
    <> 
      <h1>Current BTC/USD data</h1> 
      <p>Code: {btcData.code}</p> 
      <p>Symbol: {btcData.symbol}</p> 
      <p>Rate: {btcData.rate}</p> 
      <p>Description: {btcData.description}</p> 
      <p>Rate Float: {btcData.rate_float}</p> 
    </> 
  ); 
} 
```

In case there is a delayed, we should put two renderer "whether or not the data has been successfully fetched."

Example : 
```
return someStateVariable.length > 0 ? (
  <div>
    <h1>Data returned : </h1>
    <h2>{someStateVariable.results[0].price} </h2>
  </div>
) ; (
  <h1>Data pending...</h1>
);
```

## Fetching data

"The fetchData function initially fetches data from the randomuser.me API, next it retrieves a response form the API in JSON format, and finally updates the state variable with the returned data."


# Advance hooks

## useReducer

useState : 
  - Initial state

useReducer :
  - Initial state and reducer function


Example of useReducer : 

```
import {useReducer} from 'react';
import './App.css';

const reducer = (state, action) => {
  if (action.type === 'buy_ingredient') return {money: state.money - 10};
  if (action.type === 'sell_a_meal') return {money: state.money + 10};
  return state
}

fucntion App() {
  const initialState = {money: 100};
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div className="App">
      <h1> Wallet: {state.money}</h1>
      <div>
        <button onClick={() => dispatch({type: 'buy_ingredients'})}>Shopping for veggies</button>
        <button onClick={() => dispatch({type: 'sell_a_meal'})}>Serve a meal to the customer</button>
      </div>
    </div>
  )
}

export default App;
``` 

## When to choose useReducer vs useState

useState :
  - When the data is less complex (primitive data like string numbers or booleans.) 

useReducer
  - for more complex data like arrays and objects. 


## useRef to access underlying DOM

Example : 

```
import React from "react";
import './App.css';

fucntion App() {
  const formInputRef = React.useRef(null);

  const focusInput = () => {
    formInputRef.current.focus();
  }
  return (
    <>
      <h1>Using useRef to access underlying Dom</h1>
      <input ref={formInputRef} type="text" />
      <button onClick={focusInput}>
      Focus input
      </button>
    </>
  );
}

export default App;

```

## Custom hooks

"In essence, hooks give you a repeatable, streamlined way to deal with specific requirements in your React apps. For example, the `useState` hook gives us a reliable way to deal with state updates in React components."

"A custom hook is simply a way to extract a piece of functionality that you can use again and again. Put differently, you can code a custom hook when you want to avoid duplication or when you do not want to build a piece of functionality from scratch across multiple React projects. By coding a custom hook, you can create a reliable and streamlined way to reuse a piece of functionality in your React apps."

Example : 
```
import { useState} form "react";
import useConsoleLog from "./useConsoleLog";



function App() {
  const [count, setcount] = useState(0);
  useConsoleLog(count);

  function increment(){
    setCount(prevCount => prevCount + 1)
  }
  return (
    <div>
    <h1>Count: {count}</h1>
    <button onClick={increment}> Plus 1</button>
    </div>
  );
}

export default App;

```

Other page of the example (a file name useConsoleLog.js)

```
import {useEffect} from "react";

function useConsoleLog(varName) {
  useEffect(() => {
    console.log(varName);
  }, [varName]);
}

export default useConsoleLog;

```


# JSX Deep Dive

## JSX, Components and Elements

JSX : Syntax extension to JavaScript (JS)

React : Uses JSX to describe UI appearance

## Component composition with children

Containment : "refers to the fact that some components donèt know their children ahead of time. This is especially common for components like a sidebar or a dialog."

Example of a dialog

```
function Dialog(props){
  return (
    <div className="modal">
      {props.children}
    </div>
  );
}

function ConfirmationDialog() {
  return(
    <Dialog color="blue">
      <h1 className="Dialog-title">
        Thanks!
      </h1>
      <p className="Dialog-message">
      We'll process your order in less than 24 hours.
      </p>
    </Dialog>
  );
}
```

## Types of Children

"In JSX expressions, the content between an opening and closing tag is passed as a unique prop called children."

### The "types of JavaScript values that are ignored as children and don't render anything."

#### String Literals
"String lietrals refer to simple JavaScript strings. They can be put between the opening and closing tags, and the children prop will be that string."

1. "JSX removes whitespaces at the beginning and end of a line, as well as blank lines"
2. "New lines adjacent to tags are removed"
3. "JSX condenses new lines that happen in the middle of string literals into a single space"

#### JSX Elements
"You can provide JSX elements as children to display nested components"

``` 
<Alert>
  <Title/>
  <Body/>
</Alert>
```

"JSX also provide JSX elements as children to display nested components"
<Alert>
  <div>Are you Sure?</div>
  <Body/>
</Alert>
```

"A React component can also return a bunch of elements without wrapping them in an extra tag. For that, you can use React Fragments either using the explicit component imported from React or empty tags, which is shorter syntax for fragment. A react Fragment component lets you group a list of children without adding extra nodes to the DOM."

They are both equivalents
```
return (
  <React.Fragment>
    <li>Pizza margarita</li>
    <li>Pizza diavola</li>
  </React.Fragment>
);

return (
  <>
    <li>Pizza margarita</li>
    <li>Pizza diavola</li>
  </>
);
```

#### JavaScript Expression
"You can pass any JavaScript expression as children by enclosing it within curly braces. {}. The bellow expressions are identical:"
```
<MyComponent>Little Lemon </MyComponent>
<MyComponent>{'Little Lemon'}</MyComponent>
```

The last one is less used by convention.
```
function Dessert(props) {
  return <li>{props.title}</li>
}

function List() {
  const desserts = ['tiramisu', 'ice cream', 'cake'];
  return (
    <ul>
    {desserts.map((dessert)) => <Item key={dessert} title={dessert} />}
    </ul>
  );
}
```

#### Function

"Suppose you insert a JavaScript expression inside JSX. In that case, React will evaluate it to a string, a React element, or a combination of the two. However, the children prop works just like any other prop, meaning it can be used to pass any type of data, like a functions.


Function as children is a React pattern used to abstract shared functionality that you will see in detail in the next lesson."

## Manipulating children dynamically in JSX

2 Apis : 

### React.CloneElement
As a react global object
```
Import React from 'react';

React.cloneElement(...)
```

Named import
```
Import {cloneElement} form 'react'
cloneElement(...)
```

Syntax : React.cloneElement(element, [props])
- Modify children properties
- Add to children properties
- Extend the functionality of children 

```
const buttonElement = {
  type: SubmitButton,
  props: {
    color: "green",
    children: "Submit!",
  },
};

const output = React.cloneElement(buttonElement)


--> the output 

{
  type:SubmitButton,
  props:{
    color: "green",
    children: "Submit!",
    disabled: false,
  },
};
```

### React.children
A really useful function is React.Children.map(children, callback)


 

