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