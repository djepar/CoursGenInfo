import urllib.request
def retrieve_page(url):
    # Retrieve the contents of a web page. 
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.read()
    return dta


the_text = retrieve_page("https://runestone.academy/runestone/books/published/thinkcspy/Files/FetchingSomethingFromTheWeb.html")
print(the_text)