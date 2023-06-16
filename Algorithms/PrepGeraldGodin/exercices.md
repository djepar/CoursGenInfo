# à Faire 
    7 les derniers
    8 : le dernier numero
    9.6 et + 





1.1 
    a = 3
    b = 4

1.2 
    a = 2
    b = 3
    c = 1

1.3 
    a = 6
    b = 2

1.4 
    A = 13
    B = 13
    C = 13

1.5
    A = 2
    B = 2

1.6 : Swap 2 variables

```
Variables A, B, Swap en Entier
Début
Swap <-- A
A <-- B
B <-- Swap 
Fin
```

1.7 : Une variante du précédent : on dispose de trois variables A, B et C. Ecrivez un algorithme transférant à B la valeur de A, à C la valeur de B et à A la valeur de C (toujours quels que soient les contenus préalables de ces variables). 
```
Variables A, B, C, Swap en Entier
Début
Swap <-- A
C <-- B
B <-- Swap 
Fin
```

1.8 
    Ne fonctionne pas


1.9 
    Fonctionne puisque concaténation. 


2. 1
   1. 231
   2. 462

2.2
```
Début
Écrire "Veuillez écrire un nombre"
Lire Nombre
NombreCarre <-- Nombre^2
Écrire "Son carré est : NombreCarre", NombreCarre
Fin
```


2.2
```
Début
Écrire "Quel est votre prénom"
Lire Nom
Écrire "Bonjour, ", Nom, '!'
Fin
```

2.3
```
Début
Écrire "Prix de l'article"
Lire PrixHT
Écrire 'Le nombre d'article'
Lire nbArticle
Écrire 'Le taux TVA en decimal'
Lire ttva

PrixTotal <-- PrixHT  *  nbArticle * (1 + ttva)

Écrire "Le prix total est de ", PrixTotal
Fin
```

3.1 
```
Début
Écrire "Veuillez écrire un nombre"
Lire Nombre
**Si** Nombre > 0 **Alors**
    Écrire "Le nombre est positif"
**Sinon**
    Écrire "Le nombre est négatif"
**Finsi**
Fin
```


3.2
```
Début
Écrire "Veuillez écrire le premier nombre"
Lire nb1
Écrire "Veuillez écrire le deuxième nombre"
Lire nb2
**Si** (nb1 > 0 ET nb2 > 0) OU (nb1 < 0 ET nb2 < 0)
**Alors**
    Écrire "Le produit des nombres est positif"
**Sinon**
    Écrire "Le nombre est négatif"
**Finsi**
Fin
```

3.3
```
Début
Écrire "Veuillez écrire le premier nom"
Lire nom1
Écrire "Veuillez écrire le deuxième nom"
Lire nom2
Écrire "Veuillez écrire le troisième nom"
Lire nom3
**Si** (nom1 > nom2) ET (nom2 > nom3)
**Alors**
    Écrire "Les noms sont en ordre alphabétique"
**Sinon**
    Écrire "Le noms ne sont pas en ordre alphabétique"
**Finsi**
Fin
```

3.4
```
Début
Écrire "Veuillez écrire le premier nombre"
Lire nb1
**Si** nb1 > 0 
    Écrire "Le produit des nombres est positif"
**SinonSi** nb1 = 0
    Écrire "Le produit des nombres vaut zero"
**Sinon**
    Écrire "Le nombre est négatif"
**Finsi**
Fin
```

3.5
```
Début
Écrire "Veuillez écrire le premier nombre"
Lire nb1
Écrire "Veuillez écrire le deuxième nombre"
Lire nb2
**Si** nb1 = 0 OU nb2 = 0
**Alors**
    Écrire "La valeur du produit est de 0"
**SinonSi** (nb1 > 0 ET nb2 > 0) OU (nb1 < 0 ET nb2 < 0)
**Alors**
    Écrire "Le produit des nombres est positif"
**Sinon**
    Écrire "Le nombre est négatif"
**Finsi**
Fin
```

3.6
```
Début
Écrire "Veuillez écrire votre âge"
Lire age
**Si** age < 8 et age > 5
**Alors**
    Écrire "Poussin"
**SinonSi** age < 10
    Écrire "Pupille"
**SinonSi** age < 12
    Écrire "Minime"
**Sinon
    Écrire "Cadet"

**Finsi**
Fin
```


## 4.1  Formuler un algorithe équivalent à 
```
Si Tutu > Toto + 4 OU Tata = "OK" Alors
  Tutu ← Tutu + 1
Sinon
  Tutu ← Tutu – 1
Finsi
```

```
Si Tutu <= Toto + 4 ET Tata != "OK" Alors
    Tutu <-- Tutu - 1
Sinon
    Tutu <--  Tutu + 1
Finsi
```


## 4.2 
Cet algorithme est destiné à prédire l'avenir, et il doit être infaillible !
Il lira au clavier l’heure et les minutes, et il affichera l’heure qu’il sera une minute plus tard. Par exemple, si l'utilisateur tape 21 puis 32, l'algorithme doit répondre :
"Dans une minute, il sera 21 heure(s) 33".
NB : on suppose que l'utilisateur entre une heure valide. Pas besoin donc de la vérifier.


```
Variables h, m en Numérique
Début
Écrire "Quelle heure est-il?"
Lire heure
Écrire "Quelle minute est-il?"
Lire minute
m <-- m + 1
Si m = 60 Alors
    Sinon
        h <-- h + 1
        m <-- 0
Finsi
Si h = 24 Alors
    h = 0
Finsi
Écrire "Dans une minutes, il sera : ", h, "heures et " , m, "minutes"
Fin
```



## 4.3
De même que le précédent, cet algorithme doit demander une heure et en afficher une autre. Mais cette fois, il doit gérer également les secondes, et afficher l'heure qu'il sera une seconde plus tard.
Par exemple, si l'utilisateur tape 21, puis 32, puis 8, l'algorithme doit répondre : "Dans une seconde, il sera 21 heure(s), 32 minute(s) et 9 seconde(s)".
NB : là encore, on suppose que l'utilisateur entre une date valide.


```

Variables h, m en Numérique
début
Écrire "Écrire h, m, s"
Lire h, m, s

s <-- s + 1
Si s = 60 Alors
    s <-- 0
    m <-- m +1 
Finsi
Si m = 60 Alors
    h <-- h + 1
    m <-- 0
Finsi
Si h = 24 Alors
    h = 0
Finsi
Écrire "Dans une minutes, il sera : ", h, "heures et " , m, "minutes", s, "secondes"
Fin
```


# 4.4
```
Variables nbr_copie, prix en numérique
Début

Écrire "Combiens de copies"
Lire nbr_copie
Si nbr_copie <= 10 Alors
    prix <-- nbr_copie * 0.10
SinonSi nbr_copie <= 30 Alors
    prix <-- (10 * 0.10 + (0.9 * (nbr_copie - 10)))
SinonSi nbr_copie > 20 Alors
    prix <-- (10 * 0.1 + (0.9 * 20)) + ((nbr_copie - 30) * 0.8))
Finsi
Écrire "Le prix est de : ", prix, "$"
Fin
```


# 4.5 
```
Variables age en numerique
Variables sexe en caractères
Variable payer_impot en booléens
Début

Écrire : "Quel âge as-tu? 
Lire age
Écrire : "Quelle est ta génitalité (H ou F)"
Lire sexe
Si sexe = 'H' ET age > 20 Alors
    payer_impot = VRAI
Sinonsi sexe = 'F' ET age >= 18 Et age <= 35 
    payer_impot = VRAI
Sinon
    payer_impot = FAUX
Finsi
Écrire "Il est ", payer_impot, "que vous allez payer des impots"
Fin
```

## 4.6
```
Début
Variables s1,s2,s3,s4 en numériques //scores
Variable c1, c2, c3, c4 en bool
Écrire "Quel est le score de chaque participant, écrire un à la suite de l'autre en %"
Lire s1, s2,s3,s4
c1 <-- s1 > 50 
c2 <-- s2 > 50 OU s3 > 50 ou s4 > 50
c3 <-- s1 > 12.5
c4 <-- s1 > s2 ET s1 > s3 ET s1 > s4
Si c1 Alors
    Écrire : "Il est élu"
Sinonsi c2 OU non c3
    Écrire : "Éliminé" 
Sinonsi c4
    Écrire : "Ballotage favorable"
Sinonsi 
    Écrire "Ballotage défavorable"
Finsi
Fin
```

# 4.7
```
Début
Variables c1,c3,c4 en bool
Variable c2_Nbr d'accident en numerique
Écrire : "Vrai ou faux, avez-vous plus de 25 ans? 
Lire c1
Écrire : "Combien d'accident"
Lire c2_nbr
Écrire : "Vrai ou faux, avez-vous votre permis depuis plus de deux ans? "
Lire c3
Écrire : "Plus de 5 ans dans la compagnie"
c4

Si Non(c1) // moins de 25 ans
    Si non(c3) // - de deux ans
        Si c2_nbr > 0   // Responsable d'accident
            Écrire : Refusé
        Sinonsi 
            Écrire : Rouge
    Sinonsi c2_nbr < 0 // + de deux ans
        Écrire : Orange
Sinon // + 25 ans
    Si c3 // + de deux ans
        Si c2_nbr < 0 ET non(c3)
            Écrire : Vert
        Sinonsi c2_nbr <= 1
            Si c4   // +  de 5 ans
                Écrire : Vert
            Sinon
                Écrire : Orange
        Sinonsi c2_nbr < 2
            Si c4   // +  de 5 ans
                Écrire : Orange
            Sinon
                Écrire : Rouge
        Sinon
            Écrire : Refusé



    Sinonsi c4 ET NON(c2) ET NON(c3) // 
        Écrire : Orange
    Sinonsi
        Écrire : Rouge
    Finsi
Sinonsi
    Si c4 
Finsi
Fin
```

# 4.8
```
Début
Variables jour, mois, annee en numerique
Variable jour_valide, estBissextile, mois_valide en bool
Variables listesMois, en liste
Listedesmois = [1,3,5,7,8,10,12]
Écrire : "le jour, le mois et l'année"
Lire jour, mois, annee
mois_valide = vrai
jour_valide = vrai

Si mois > 12 OU mois < 1 alors
    mois_valide <-- faux
Finsi


//bissextile 
Si annee % 4 = 0 alors
    Si annee % 100 = 0 alors
        Si annee % 400 = 0 alors
            estbissextile <-- vrai
        Sinon
            estbissextile <-- Faux
        Finsi
    Sinon
        estbissextile <-- Vrai
    Finsi
Sinon
    estbissextile <-- Faux
Finsi


Si mois dans listedesmois alors
    Si jour <> 31 alors
        jour_valide <-- Faux
Sinonsi mois = 2
    Si estBissextile Alors
        Si jour  = 29 alors
            jour_valide <-- Vrai
        Sinon
            jour_valide <-- Faux
        Finsi
    Sinon
        Si jour = 28 alors
            jour_valide <-- Vrai
        Sinon
            jour_valide <-- Faux
        Finsi
Sinon
    si jour = 30 alors
        jour_valide <-- Vrai
    Sinon
        jour_valide <-- Faux
    Finsi
Finsi
Si jour_valide ET mois_valide alors
    Écrire : "La date est valide"
Sinon
    Écrire: "La date n'est pas valide"
Finsi

fin
```

# 5.1 
```
Variable nbr en numerique
Debut
Écrire "Veuillez rentrer un nombre entre un et trois."
nbr <-- 0
Tantque nbr < 1 ET nbr > 3
    Lire nbr
    Si nbr < 1 ET nbr > 3 Alors
        Écrire : "Saisie éronnée, recommencez"
    Finsi
FinTantQue
Écrire : "Saisie acceptée"
Fin
```

# 5.2
```
Variable nbr en numerique
Debut
Écrire "Veuillez rentrer un nombre entre 10 et 20."
nbr <-- 0
Tantque nbr < 20 ET nbr > 10
    Lire nbr
    Si nbr < 10 Alors
        Écrire : "Doit etre plus grand"
    Sinonsi nbr > 20 Alors
        Écrire : "Doit etre plus petit"
    Finsi
FinTantQue
Écrire : "Saisie acceptée"
Fin
```


# 5.3 
```
Variables nbr, nouveau_nbr en numerique
Debut
Écrire "Veuillez rentrer un nombre
Lire nbr
nouveau_nbr <-- nbr + 1
Tantque nouveau_nbr < nbr + 10
    Écrire nouveau_nbr
    nouveau_nbr <-- nouveau_nbr + 1
FinTantQue
Fin
```


# 5.4
```
Variables nbr, nouveau_nbr en numerique
Debut
Écrire "Veuillez rentrer un nombre"
Lire nbr
nouveau_nbr <-- nbr
Pour nouveau_nbr <-- nbr + 1 à nbr + 10 
    Écrire nouveau_nbr
nouveau_nbr Suivant
Fin
```

# 5.5
```
Variables nbr, i en numerique
Debut
Écrire "Veuillez rentrer un nombre"
Lire nbr
Écrire "La table de multiplication de ce nombre est : "
Pour i <-- 1 à 10
    Écrire nbr,  " x  ", i, " = ", i * nbr
i suivant
Fin
```


# 5.6
```
Variables nbr, somme, i en numerique
Debut
Écrire "Veuillez rentrer un nombre"
Lire nbr
Somme <-- 0
Pour i <-- 1 à nbr
    somme <-- somme + i
i Suivant
Écrire somme
Fin
```
# 5.7

```
Variables N, i, F en Entier
Debut
Ecrire "Entrez un nombre : "
Lire N
F ← 1
Pour i ← 2 à N
  F ← F * i
i Suivant
Ecrire "La factorielle est : ", F
Fin

```

# 5.8
```
Variables nbr, plusgrand, position i en numerique
Debut
plusgrand  <-- 0
Pour i <-- 1 à 20
    Écrire "Veuillez rentrer le nombre # ", i
    Lire nombre
    Si nombre > plusgrand OU i = 1 Alors
        plusgrand  <-- nombre
        position  <-- i
    Finsi
i Suivant
Écrire "Le plus grand de ces nombres est : ", plusgrand
Écrire "Il a été saisie en position numéro : ", position
Fin
```

#

# 5.9
```
Variables nombre, plusgrand, position i en numerique
Debut
plusgrand  <-- 0
i <-- 0
nombre <-- 1
Tantque nombre <> 0 
    i <-- i +1

    Écrire "Veuillez rentrer le nombre # ", i
    Lire nombre
    Si nombre > plusgrand OU i = 1 Alors
        plusgrand  <-- nombre
        position  <-- i
    Finsi
FintantQue
Écrire "Le plus grand de ces nombres est : ", plusgrand
Écrire "Il a été saisie en position numéro : ", position
Fin
```

# 5.10 

```
Variables prix, sommes,  i, montant, reste en numerique
Debut
i <-- 0
somme  <-- 0

Écrire "Veuillez ecrire le prix"
Lire prix
Tantque prix <> 0
    Écrire "Veuillez ecrire le prix"
    Lire prix
    somme  <-- somme + prix
FintantQue
Ecrire "Vous devez: ", somme, "euros"
Ecrire "Montant verse : "
Lire montant
Reste  <-- montant - somme
Tant que reste   <>  0
    Tant que reste > 10
        Écrire "10 euros"
        reste  <-- reste -10
    FinTantQue
    Tant que reste > 5
        Écrire "5 euros"
        reste  <-- reste - 5
    FinTantQue
    Tant que reste > 0
        Écrire "1 euro"
        reste  <-- reste - 1
    FinTantQue
FinTantQue
Fin
```





# 5.11  PAS FINI
```
Variables n, n_fact, np_fact, p_fact, nbr_chevaux_joue, i,j,k, y , x en numerique
Debut
Écrire "Combien de chevaux partants"
Lire n
Écrire "Combien de chevaux joues"
Lire p


n_fact <-- 1
Pour i ← 2 à n 
  n_fact ← n_fact * i
i Suivant

np_fact <-- 1
Pour j <-- 2 à (n-p)
    np_fact <-- np_fact * j
j Suivant


p_fact <-- 1
Pour k <-- 2  à  p
    p_fact <-- p_fact * p
k suivant

x <-- n_fact / np_fact
y = n_fact / ( p_fact * np_fact)

Écrire "Dans l'ordre : une chance sur", x, " de gagner"

Écrire "Dans le désordre : une chance sur", y, " de gagner"

```

# 6.1

```
Tableau Note[6] en Numérique
Debut
Pour i <-- 0 à 6
    Note[i] = 0
i Suivant
Fin
```

# 6.2 
```
Tableau Voyelle[6] en Numérique
Debut
Voyelle[0] <-- "a"
Voyelle[1] <-- "e"
Voyelle[2] <-- "i"
Voyelle[3] <-- "o"
Voyelle[4] <-- "u"
Voyelle[5] <-- "y"
Fin
```

# 6.3
```
Tableau Note[8] en Numérique
Debut
Pour i <-- 0 à 8
    Ecrire "Ecrire la note numero", i +1 
    Lire Note[i]
i Suivant
Fin
```


# 6.7 
```
Tableau Note[8] en Numérique
Variable moy en numérique
Debut
moyenne <-- 0
Pour i <-- 0 à 8
    Ecrire "Ecrire la note numero", i +1 
    Lire Note[i]
    moyenne <-- moyenne + Note[i]
    Ecrire "Au tour # ", i, "la moyenne est de ", moyenne / i +1
i Suivant
Ecrire " La moyenne / 9
Fin
```

# 6.8
```
Tableau Notes[] en Numérique
Variable nb, i, pos, neg en Numérique
Début
Ecrire "Combien y a-t-il de notes à saisir ?"
Lire nb
pos <-- 0
neg <-- 0
Redim Notes[nb-1]

Pour i <-- 0 à nb-1
    Ecrire "Entrer le numero #, i + 1
    Lire Notes[i] 
    Si Notes[i] > 0
        pos  <-- pos +1
    SinonSi Notes[i] < 0
        neg <-- neg +1
    Finsi
i suivant
Ecrire neg
Ecrire pos
```

# 6.9 
```
Tableau Notes[] en Numérique
Variable nb, i, somme en Numérique
Début
Ecrire "Combien y a-t-il de notes à saisir ?"
Lire nb
Redim Notes[nb-1]
somme <-- 0
Pour i <-- 0 à nb-1
    Ecrire "Entrer le numero #, i + 1
    Lire Notes[i] 
    somme <-- somme + Notes[i] 
i suivant
Ecrire somme
```


# 6.10
```
Tableau Notes[] en Numérique
Variable nb, somme en Numérique

somme <-- 0
Pour i <-- 0 à nb-1
    Notes[i] <-- T1[i] + T2[i]
i suivant 
Ecrire somme
```

# 6.11
```
Tableau T1[ti], T2[tk]en Numérique
Variable  somme, partiel en Numérique
partiel <-- 0
somme <-- 0
Pour i <-- 0 à ti   
    Pour k <--0 à tk
        partiel <-- T1[i] * T2[k]
    k suivant
    somme <-- partiel + somme
i suivant 
Ecrire somme
```

# 6.12
```
Tableau Notes[] en Numérique
Variable nb, i, pos, neg, temp en Numérique
Début
Ecrire "Combien y a-t-il de notes à saisir ?"
Lire nb
pos <-- 0
neg <-- 0
Redim Notes[nb-1]

Pour i <-- 0 à nb-1
    Ecrire "Entrer le numero #, i + 1
    Lire temp
    Notes[i] <-- temp +1 
    Si Notes[i] > 0
        pos  <-- pos +1
    SinonSi Notes[i] < 0
        neg <-- neg +1
    Finsi
i suivant
Ecrire neg
Ecrire pos
```

# 7.1

```
Tableau list[] en Numerique
Variable nb_entre, i, j,  en Numerique
Variable Flag en Boolen
Écrire "Combien d'entrée dans le tableau"
Lire nb_entre
Redim list[nb_entre - 1]
flag <-- faux

Pour i <-- 0 à nb_entre -1
    Ecrire "Entrer le numero #, i + 1
    Lire list[i]
i suivant


Pour j <-- 1 à nb_entre - 1
    Si list[j] <>  list[j -1] + 1 Alors
        flag <-- faux
j suivant

Si Flag alors
  Ecrire "Les nombres sont consécutifs"
Sinon
  Ecrire "Les nombres ne sont pas consécutifs"
FinSi
Fin
```
 
Autre manière de le faire

```
Tableau list[] en Numerique
Variable nb_entre, i, j,  en Numerique
Variable Flag en Boolen
Écrire "Combien d'entrée dans le tableau"
Lire nb_entre
Redim list[nb_entre - 1]
flag <-- faux

Pour i <-- 0 à nb_entre -1
    Ecrire "Entrer le numero #, i + 1
    Lire list[i]
i suivant

i <-- 1
TantQue list[i] = list[i - 1] + 1 et i < Nb - 1
    i <-- i + 1
FinTantQue
Si list[i] = list[i - 1] + 1 Alors
    Ecrire "Les nombres sont consecutifs"
Sinon
    Ecrire "Les nombres ne sont pas consecutifs"
FinSi
```

# 7.2

```
//boucle principale : le point de départ se décale à chaque tour. 
Pour i <-- 0 à N - 2
    posmax  <-- i
    Pour j  <-- i + 1 à 11
        Si t[j]  > t[posmax] Alors
            posmax  <-- j
        Finsi
    j suivant
    temp  <-- t[posmax]
    t[posmax]  <-- t[i]
    t[i] <-- temp

i suivant
```

```
Variable Yapermute en Boolen 
Debut
...
Yapermut <-- Vrai
TantQue Yapermut
  Yapermut <-- Faux
  Pour i <-- 0 à n - 2
    Si t[i] < t[i + 1] alors
      temp <-- t[i]
      t[i] <--  t[i+1]
      t[i+1] <-- temp
      Yapermut <-- Vrai
    Finsi
  i suivant
FinTantQue
Fin
```


# 7.3
```
Variable temp,n, mi_n en numerique 
Debut
...
Si N % 2 = 0 Alors
    mi_n = n / 2
Sinon
    n - 1 / 2
FinSi


Pour  i  <-- 0 à mi_n 
    temp = list[N - 1]
    list[N - 1 - i] = list[i]
    list[i] = temp
i suivant
Fin
```


# 7.5
```
Variable flag en bool
flag = faux
Variable lemot en caractere
Pour i <-- N - 1
    si t[i] = lemot
    Ecrire le mot est a l'indice 
i suivant

Ecrire : flag

```


```
Debut
...

Trouve <-- faux
Fin <-- N -1
tantQue Non Trouve Et Debut <= Fin
    milieu <--  (debut + fin) / 2
    Si T[milieu]=X Alors
        Trouver <-- Vrai
    Sinon T[milieu] <  X Alors
        Debut <-- milieu + 1
    Sinon
        Fin <-- milieu -1 
    FinSi
FinTantque
Fin
```


# 8.1
```
Tableau Cases[5,12] en Numerique
Debut
Pour i <-- 0 à 5
    Pour j <-- 0 à 12
        Cases[i, j] <-- 0
    j suivant
i suivant
Fin
```


```
Tableau T[12,8] en Numerique
Variable plusgrand en Numerique
Debut
...
plusgrand <-- T[0,0]
Pour i <-- 0 à 12
    Pour j <-- 0 à 8
        Si plusgrand < T[i,j] Alors
            plusgrand <-- T[i,j]
        FinSi
    j suivant
i suivant
Fin
```

# 9.2 
```
Variable length en Numerique
Varaible mot en caracteres
Debut
Ecrire "Entrez un mot"
Lire mot
Ecrire "Ce mot contient : ", len(mot)
```


# 9.3
```
Variable length, compteur en Numerique
Varaible phrases en caracteres
Debut
Ecrire "Entrez un mot"
Lire phrases
compteur <-- 1
length <-- len(phrases)
Pour i de 0 à length 
    Si phrases[i] = " " Alors
        compteur <-- compteur + 1
    Finsi
i suivant
Ecrire "Cette phrase contient : ", compteur, "mots"
```

# 9.4


# 9.5 
```
Variable length, indice, en Numerique
Varaible phrase, nouvelleChaine en caracteres

Debut
Ecrire "Entrez une phrase"
Lire phrase
Ecrire "Quel emplacement a supprimer"
Lire indice

L <-- Len(phrase)
phrase <-- Mid(phrase, 1, Nb - 1) & Mid(phrase, nb + 1, L - Nb)
Ecrire phrase
Fin
```

# 9.6
```
Variable length, indice, en Numerique
Varaible phrase, nouvelleChaine en caracteres

Debut
Ecrire "Entrez une phrase"
Lire phrase

L <-- Len(phrase)
Pour i de 0 à L 
    phrase[i] <-- char(ascii(phrase[i]) + 1)   
    Finsi
i suivant
Fin
```


# 10.2 
```

Quel résultat cet algorithme produit-il ?
Variable Truc en Caractère
Début
Ouvrir "Exemple.txt" sur 5 en Lecture
Tantque Non EOF(5)
  LireFichier 5, Truc
  Pour i <-- 1 à Len(Truc)
    Si Mid(Truc, i, 1) = "/" Alors
        Ecrire " "
    Sinon
        Ecrire Mid(Truc, i, 1)
    FinSi
  i suivant
FinTantQue
Fermer 5
Fin
```

# 10.3 

```

Varaibles Nom*20, Prenom*15, Tel*10, Mail*20, Lig en Caracteres
fini <-- faux
Ouvrir "Example.txt" sur 5 en Ajout
Ecrire "Entrez le nom : "
Lire Nom
Ecrire "Entrez le prénom : "
Lire Prénom
Ecrire "Entrez le téléphone : "
Lire Tel
Ecrire "Entrez le nom : "
Lire Mail
Lig <-- Nom & Prenom & Tel & Mail
EcrireFichier 5, Lig
Fermer 5
Fin
```


# 11.1
```
Fonction Somme(n1, n2,n3,n4,n5) en Numerique
    Renvoyer n1+n2+n3+n4+n5
Fin Fonction
```


# 11.2 
```
Fonction Nbr_voyelle(chaine) en Numerique
    compteur <-- 0
    voyelle = ["a", "e", "i", "o", "u", "y"]
    Pour i <-- 0, Len(chaine) 
        Pour j <-- Len(voyelle)
            Si chaine[i] = voyelle[j] Alors
                compteur <-- compteur + 1
            FinSi
    i suivant
    Renvoyer compteur
Fin Fonction
```

Autre facon

```
Fonction NbVoyelles(Mot en Caractere) en Numérique
Variables i, nb, en Numérique
nb <-- 0
Pour i <-- 1 à Len(Mot)
    Si Trouve("aeiouy", Mid(Mot, i, 1)) <> 0 Alors
        nb <-- nb + 1
    Finsi
i suivant
Renvoyer nb
FinFonction
```


# 11.3 

```
Fonction Trouver(chaine1, chaine2) en Caractere
Variable i, ... en Numerique

Tantque i > Len(chaine1) - Len(chaine2) ET chaine2 <> Mid(chaine1, i, Len(chaine2))
    i <-- i + 1
FinTantQue
Si chaine2 <> Mid(chaine1, i, Len(b)) Alors
    Renvoyer 0
Sinon
Finsi
REnvoyer i
FinFonction
```
# 11.4
```
Fonction Purge(chaine, car) en Caractere
Variable i, en Numerique
Variable nouveau_string

    Pour i <-- 1 à Len(chaine) 
        Si chaine[i] = car Alors
            nouveau_string <-- Mid(chaine, i, 1)     
        i suivant   

    Retourner chaine

```
# 11.5

```
Fonction Purge(phrase, car) en Caractere
    Variable i, en Numerique
    sortie
    Pour i <-- 1 à Len(phrase) 
        Si chaine[i] = car Alors
            sortie <-- Mid(chaine, 0, i) & Mid(chaine, i, len(chaine + 1))
    i suivant   
```