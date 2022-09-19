HTML and CSS in depth
by Meta

# Semantic and Meta Tags
## Metadata cheat sheet
### Name 
"The name of the property can be anything you like, although browsers usually expect a values they understand"
`<meta name="author" content="name">

### Content
"The content field specifies the property's value."
`<meta name="language" content="english">`

### Charset 
"The charset is a special field that lets you specify the character encoding used for the pages so that the browser can display it properly."
`<meta charset="UTF-8"`

### HTTP-equiv
"This field stands for HTTP equivalent, and it's used to simulate HTTP response headers. This is rare to see, and it's recommended to use HTTP headers over HTML http-equiv meta tags."
`<meta http-equiv="refresh" content="30">`

### Basic meta tags for SEO :
"""
<meta name="description"/> provides a brief description of the web page 

<meta name=”title”/> specifies the title of the web page 

<meta name="author" content="name"> specifies the author of the web page  

<meta name="language" content="english"> specifies the language of the web page 



<meta name="robots" content="index,follow" /> tells search engines how to crawl or index a certain page 

<meta name="google"/> tells Google not to show the sitelinks search box for your page when showing search results 

<meta name="googlebot" content=”notranslate” /> tells Google you don’t want to provide an automatic translation for your page if the user uses a different language  

<meta name="revised" content="Sunday, July 18th, 2010, 5:15 pm" /> specifies the last modified date and time on which you have made certain changes 

<meta name="rating" content="safe for kids"> specifies the expected audience for your page 

<meta name="copyright" content="Copyright 2022"> specifies a Copyright 
<meta http-equiv="..."/> tags

 <meta http-equiv="content-type" content="text/html"> specifies the format of the document returned by the server 

<meta http-equiv="default-style"/>  specifies the format of the styling document 

<meta http-equiv="refresh"/> specifies the duration of the page before it’s considered stale 

<meta http-equiv=”Content-language”/> specifies the language of the page 

<meta http-equiv="Cache-Control" content="no-cache"> instructs the browser how to cache your page 
<meta name="format-detection" content="telephone=yes"/> indicates that telephone numbers should appear as hypertext links that can be clicked to make a phone call 

<meta name="HandheldFriendly" content="true"/> specifies that the page can be properly visualized on mobile devices 

<meta name="viewport" content="width=device-width, initial-scale=1.0"/> specifies the area of the window in which web content can be seen

"""

## Bare bones layout
See the bare bone layout

## UX with meta tags
### Open Graph Protocol
"The Open Graph Protocol is a set of metadata rules that allows web pages to describe themselves to social networks. Social media platforms use these meta tags to create a preview of the shared web page."
Looks like `<meta property="og:title" content="My First Web page />` :always start with og (for open graph)

## Setting up a social media card
A meta tag can:
- "inform social media platforms of the content type such as video or webiste."
- "determine what title will be displayed in the preview of a website on a social media platform"
- "informe the social media platform what the preferred preview image is."



To set up a social media card : 
```
<meta property="og:title" content="Our Menu"
<meta property="og:type" content="website">
<meta property="og:image" content="logo.png">
<meta property="og:url" content="https://littlelemon">
<!-- Optional tags -->
<meta property="og:description" content="Little Lemon is blablabla">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="Little Lemon">

```

# Forms and validation
Form validation : Ensure that data is valid and conforms to defines rules. 
"Client-side validation checks for errors as soon as they are typed into the form. The web browser does this by validating the submitted data agaisnt the specified input type. The web browser will show an error message if the wrong type of input has been submitted."


## Client side validation
Required attribute :
 `<input type="text" id="user" name="user" required>` 

 Minlength and maxlength : `<input type="text" id="user" name="user" required minlength="3" maxlength="12">`
So if the part of the form is not filled, it's can be submitted.

Min and max attributes : "determines the minimum and maximum values allowed for an input field. They are usually applied to numerical text inputs, range inputs or date"
Ex : `<input type="number" id="quantity" name="quantity" min="1" max="10">`

Multiple : "indicates that the user can enter more than one value in a single input field. This attribute can only be used for email and file input types."
Ex: `<input type="file" id="gallery" name="gallery" multiple>`

Pattern : "Defines a particular pattern that an input field value has to fullfill to be considered valid. This attribute expects a regular expression to specify the pattern. It works with text, date, search, URL, tel, email and password input types. For example, you can restrict phone numbers to be only from the UK"
`<input type="tel" id="phone" name="phone" pattern="^(?:0|\+?44)(?:\d\s?){9,10}$">`



CSS for invalid data : 
```
<style>
    input:focux:invalid {
        border:2px solid red;
    }
</style>
```
## Form submission 
With the get or post method :
`<form method="get"></form>` or `<form method="post"></form>`

Problems
- Security threat
- URL length limited by web server
- URL length limited by browser

Security choice : HTTP Post
"The HTTP POST method is more secure than the HTTP GET method. When a form is submitted using the Post method, the form data is inserted into the content of the HTTP request instead of append at the end of the URL as is done with the GET method.

## Submit
### Action and method 
"The action attributes specifies to which web address the form must be sent. This address is the location of server-side code that will process the request."
Ex : `<form action="/login"></form>`
Action can be a full url, an absolute path or a relative path.

"The method attribute specifies which HTTP method is used to submit the form; GET or POST.
Ex `<form method="post></form>` or `<form method="get"></form>`
By default, it's GET.

"Forms are not the only way to submit data to the web server [...] developers often submit HTTP  requests directly via code and send data as part of the HTTP request body in a text format called JavaScript Object Notation, or JSON"

# Media Elements
## Video and audio 
Video format valid : .mp4 .ogg .webm 
Audio format valid : .mp3 .wav .ogg

Type attribute : 
```
<video width="320" height"240">
    <source src="dance.mp4" type="video/mp4">
    <source src="dance.ogg" type="audio/mpeg"> <!-- Fallback if the file format is not supported or a problem occurs. -->
</video>
```

## Embedded players 
```
<audio loop controls>
    <source src="music.ogg" type="audio/ogg">
</audio>
```

## Images
Normal image : `img src="photo.png" width="320" alt="My Profile Photo">`

"To ensure that screen reader accessibility software can interpret images displayed in the browser. To support this, the <img> tag is combined with the <figure> and the <figcaption> tags to provide a description of the image. The <img> tag is added inside the <figure> tag and the <figcaption> is specified after it."

```
<figure>
    <img src="photo.png" width="320" alt="My Profile Photo">
    <figcaption>A photo of myself on a beach in 2015</figcaption>
</figure>
```
Supported file types :
"""
- .APNG – Animated Portable Network Graphics 

- .AVIF – AV1 Image Format 

- .GIF – Graphics Interchange Format 

- .JPEG / .JPG – Joint Photographic Expert Group image format 

- .PNG – Portable Network Graphics 

- .SVG – Scalable Vector Graphics 

- .WEBP – Web Picture Format 

"""

## iFrames 
"An iFrames is a HTML element that allows you to place embed content from another website into a webpage."
`<iframe src="https://www.example.com" width="200" height="150"></iframe>`

For security purpose, we can disable camreand and microphone access :
`iframe src="https://www.example.com" allow="camera 'none'; microphone 'none';"></iframe>`
Sandbox attribute to disable download or popups : `<iframe src="https://www.example.com" sandbox=" "></iframe>` 
With empty value, all the sandbox restrictions will apply. 

## iFrame as a picture
Ex: `<iframe src="placeholder.png" width="200" height="350" sandbox=" "allow="payment 'non'; camera 'none'; microphone 'none'">

## The canvas element
- Interactive image : GIF, webP
  - Zero interativity
  - Embed animated content.
- 2D canvas : "allows 2D graphics to be drawns in the web browser." Good for videogame and animation.  
 
- WebGL 
  - Work with the GPU of the computer
  - Good for 3D.



# Creating layouts
"In essence, the idea behind any CSS web layout is to create an optimally designed web page that has a good view ports at any given point."

## Flexbox 
"Flexbox is a type of container. 
Flexvox overcome the limitations caused by containers such as block and inline because it does a better job of sclaing over larger web pages and also provides more dynamic control of the containers."
"The most common use of flexbox in CSS are creating a responsive search bar, navigation bar and image gallery."

# CSS Selectors
Attribute selectors : 
Syntax : 
- `[attr=value]{}` :element with an href matching the value
- `[attr~=value]{}` : elements whose class attribute contains the value
- `[attr$=value]{}` : ending with
- `[attr*=value]{}` : contain the value
And more

nth-of-type and nth-child selectors
Ex : 
```
li:nth-of-type(2){
    color:aqua;
}
```

Ex :
```
ul:nth-child(2){
    color:aqua;
}
```
Star selectors (*) --> select all element on the web-page. 

## Selectors and their specificity

"""
- Every selector will have a score and place in the hierarchy
- In the case of selectors with equal specificity, the latest or last written rule the one that will be applied
- In general, ID selector should be appliedin cases where you need to be certain about a rule.
- Universal selectors have zero specificity value.
"""

## Pseudo-class selector
Order : LVHA --> :link, :visited, :hover, :active


# CSS Effects

Effect : "A change which is a result or consequence of an action or other cause"

Animation : "Graphics in motion transitioning over time."


