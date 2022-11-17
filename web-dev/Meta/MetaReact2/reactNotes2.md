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

