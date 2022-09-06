# Layout with CSS box model
The CSS box : 
Margin > Border > Padding > Content

# Display property 
- Block : displays an element as a block
- inline-block : displays an element as an inline-level block container.
- flex : displays an element as a block-level flex container. 
- inline-flex : displays an element as an inline-level flex container. 
- grid : displays an element as block-level grid container. 
-inline-grid : displays an element as an inline-level grid container. 
-flow-root : displays the content of a block container box using the flow layout. 

# CSS specificity 
"Based on the matching rules that are composed of different CSS selectors."
"Only applied when multiple declarations target the same element."
## Rules and Principles of CSS Specificity 
- "For selectors with an equal specificity, the latest rule counts.
- "For selectors with an unequal specificity the more specific rule counts."
- "Rules with specific selectors result in greater specificity."
- "The last rule defined overrides previous, conflicting rules."
- "The embedded style sheet has greater specificity than other rules."
- "the specificity of ID selectors is gerater than the specificity of attribute selectors"
- "IDs are used to incerase specificity"
- "A class selector beats any number of element selectors"
- "the specificity of the universal selector and inherited selectors is zero, zero, zero, zero"
- " The CSS Specificity Calculator calculates CSS specificity. "

# BEM Convention
Block : Is independent, reusable and a parent item
`.btn {}`
Element : Is non-independent and a child item. 
`.btn__price {}
Modifier : Represents different styles of classes and is used for both blocks and elements. 
`.btn--orange {}`