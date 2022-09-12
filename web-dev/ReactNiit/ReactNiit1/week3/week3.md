# Creating a style sheet
1. Create an HTML document
2. Create a css file
3. Link the HTML to the CSS file with a link tag under the head
`<link rel="stylesheet" src="styles.css">`

# CSS counter :
first : `counter-reset : section;`

## Incrementation
    ex:

```
h3::before {
    counter-incerment: section;
}
```

## Display a counter
h3::before {
    counter-incerment: section;
    content: "Section" counter(section)
}
```