import os

home = os.environ.get("HOME", "")
shell = os.environ.get("SHELL", "")
notaccess = os.environ.get("sfodasoif", "Not accessible")
fruit = os.environ.get("FRUIT", "")
print("home : {} and shell : {} not accessible : {}".format(home, shell, notaccess))
print("fruit : {}".format(fruit))
