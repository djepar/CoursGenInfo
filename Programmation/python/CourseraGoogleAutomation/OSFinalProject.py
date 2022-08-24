import re
import operator #(maybe????)

"""
Exercice 1 : Regex
"""

#To get INFO message like 'ticky : INFO Closed ticket '
INFOPattern = r"ticky: INFO ([\w ]*) \[#([\d]*)\] \(([\w]*)\)"

ticketINFO = re.search = (INFOPAttern, line)

#For the username
ticketINFO.group(3)

# To get ERROR message
ErrorPattern = r"ticky: ERROR ([\w ]*) \(([\w]*)\)"
ticketERROR = re.search(ErrorPattern, line)

#For the type of request 
ticketERROR.group(1)

#For the username
ticketERROR.group(2)

"""
Exercice 2 : Dictionary sorting operations
"""
sorted(fruit.items(), key=operator.itemgetter(1)) #Changing the itemgetter let us change between the element of the dict : key or value
#For an inverse list :
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)


"""
Exercice 3 : How to use csv_to_html.py
In bash:
First of all, we need to give executable permission to the script:
sudo chmod +x csv_to_html.py

sudo chmod  o+w /var/www/html

./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html
"""

#Generating reports
