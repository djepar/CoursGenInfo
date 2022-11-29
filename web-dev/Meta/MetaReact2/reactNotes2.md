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
