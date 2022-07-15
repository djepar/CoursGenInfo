import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    pass
  
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp = str(datetime.datetime.fromtimestamp(timestamp))
  timestamp = timestamp[:10]
  return timestamp
print(file_date("bonjour.txt"))