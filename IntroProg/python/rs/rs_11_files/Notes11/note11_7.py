# 11.7 With Statements
# with <create some object that understands context> as <some name>:
# do some stuff with the object
   # ...
#The context manager automates the process of doing common operations at the start of some task, 
# as well as automating certain operations at the end of some task. 
# In the context of reading and writing a file, 
# the normal operation is to open the file and assign it to a variable. 
# At the end of working with a file the common operation is to make sure that file is closed.
with open("mytext.txt") as md: # Ouvre le document et lui attribue la variable md
    print(md)
    for line in md:
        print(line)
print(md)
