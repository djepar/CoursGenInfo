# Week 1
## Describe the relative and absolute positioning. 
- Static Positioning : normal position in the document layout flow. 
  - `position: static;`
- Absolute positionting : "an element is positioned relative to the nearest positioned ancestor, it uses the document body and moves along with page on scrolling." 
  - `position : absolute;`
- Relative positioning : "is like static positioning but once the positioned element has taken its place, the final position including the overlap feature can be modified."
  - `position : relative;`
- Fixed positioning : "usually fixes an element in place relative to the visible portion of the viewport, hence it always stays in the same place even if the page is scrolled." 
  - `position : fixed;`

## Use z-index and stack order to change the Rendering Order of HTML Elements
The z-index specifie the stack order of an element.
- The term z-index is a reference to the z-axis." 
- "A greater z-axis avalue is at the top of the stack."
- "A lower z-axis value is at the bottom of the stack."
- "All web-pages have a z-axis"
- "By default, all positioned elements have a z-index of auto, which is effectively zero."