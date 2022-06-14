#11.1 Working with Data Files
# open --> open('filename', 'r') Ouvre un fichier qui se nomme "filename" et l'utiliser pour le lire. Retourne une référence pour le dossier de l'objet.
# open --> open('filename', 'w') Ouvre un fichier qui se nomme "filename"et l'utiliser pour  écrire. Retourne une référence pour le dossier de l'objet.
# close--> filevariable.close()
ccfile = open("ccdata2.txt", "r")

ccfile.close()

