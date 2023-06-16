def un_six(a,b):

    print("Avant le swap : A = {} et B = {} ".format(a,b))
    swap = a
    a = b
    b = swap
    print("Après le swap : A = {} et B = {} ".format(a,b))
    
un_six(2,5)


def un_sept(a,b,c):
    print("Avant le swap : A = {} et B = {} et C = {} ".format(a,b,c))
    x = a
    a = c
    c = b
    b = x
    print("Après le swap : A = {} et B = {} et C = {} ".format(a,b,c))
    
    
un_sept(1,2,3)

def mon_quatre_deux():
    print("MON --> Quelle heure est-il?")
    heure = int(input())
    print("Quelle minute est-il?")
    minute = int(input())

    minute = minute + 1

    if minute == 60:
        heure = heure + 1
        minute = 0
    if heure == 24:
        heure = 0
        minute = 0
    print("MON --> Dans une minute, il sera :", heure, "heures et", minute, "minutes")


mon_quatre_deux()

def quatre_deux():
    print("Entrez les heures, puis les minutes : ")
    h = int(input())
    m = int(input())

    m = m + 1

    if m == 60:
        m = 0
        h = h + 1

    if h == 24:
        h = 0

    print("Dans une minute, il sera", h, "heure(s)", m, "minute(s)")

# Appel de la fonction
quatre_deux()