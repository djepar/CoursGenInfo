# Adding Interactivity
## Updating Objects in State
While using state, it's better to replace than to mutate, so "Treat state as read-only"

### Local mutation is fine
Ex : 
```
const nextPosition = {};
nextPosition.x = e.clientX;
nextPosition.y = e.clientY;
setPosition(nextPosition);
```
What is bad is this : 
```
position.x = e.clientX;
position.y = e.clientY;
```

### Copying objects with the spread syntax
When "you will want to include _existing_ data as part of the new object you're creating"
Ex : 
```
function handleEmailChange(e) {
    setPerson({
        ...person, 
        email : e.target.value
    });
}
```
"Note that the `...` spread syntax is __shallow___--it only copies things one level deep. This makes it fast, but it also means that if you want to update a nested property, you'll have to use it more than once"

### Write concise update logic with Immer
Two ways to treat __nested__ objects
- flatten the structure
- Use the Immer library 
  - "Lets you write using the convenient but mutating syntax and take care of producing the copies for you"

"""
__To try Immer__:
- Add use-immer to your package.json as a dependency
- Run npm install
- Then replace import { useState } from 'react' with import { useImmer } from 'use-immer'
""
Ex : 
```
function handleNameChange(e) {
    updatePerson(draft => {
      draft.name = e.target.value;
    });
  }
```

## Updating Arrays in State
"Arrays are just another kind of object. Like with objects, you should treat arrays in React state as read-only"
- Adding
  - Not : push and unshift
  - Instead : concat, [..arr]
- Removing
  - Not : pop,shift, splice
  - instead : filter, slice
- Replace
  - Not : splice, arr[i]
  - Instead : map
- Sorting 
  - Not : reverse, sort
  - Instead : copy the array first

The difference between slice and splice
- "slice lets you copy an array or a part of it"
- "splice mutates the array (to insert or delete items).

Example of adding 
```
setArtists( // Replace the state
  [ // with a new array
    ...artists, // that contains all the old items
    { id: nextId++, name: name } // and one new item at the end
  ]
);
```

Example of deleting
```
<ul>
{artists.map(artist => (
    <li key={artist.id}>
    {artist.name}{" "}
        <button onClick={() => {
            setArtists(
                artists.filter(a => a.id !== artists.id)
            );
        }}>
            Delete
        </button>
    ))}
    </li>
</ul>
```