# Les variables
## L'instruction d'affectation

La seule chose qu'on peut faire avec une variable, c'est l'affecter, soit, 'lui attribuer une valeur.'
En pseudo-code, on utilise le `<--`

Comme dans `Toto <-- 24`

'Une instruction d'affectation ne modifie que ce qui est situé à gauche de la flèche.'

`Tuto <-- Toto + 4`
    Attribue la valeur de la variable toto a tuto + 4

Grande différence entre : 
```
Debut 
Riri <-- "Loulou"
Fifi <-- "Riri"
Fin
```
Et avec :
```
Debut 
Riri <-- "Loulou"
fifi <-- Riri
Fin
```

## Les expressions

Dans une instruction d'affectation on trouve : 
    - à gauche : nom de la variable
    - à droite : expression 

Une expression est un ensemble de valeurs, reliées par des opérateurs, et équivalent à une seule valeur. 

Opérateur : un signe qui relie deux valeurs, pour produire un résultat.


# Lecture et Écriture

Syntaxe de Lire : `Lire Titi`

Syntaxe d'écrire : `Ecrire "Entrez votre nom de famille : "` puis `Lire NomFamille`


# Les tests

## Structure d'un test (aussi appelé structure alternative)
```
**Si** booléan **Alors**
    Instruction
**Finsi**
```


```
**Si** booléan **Alors**
    Instructions 1
**Sinon**
    Instructions 2
**Finsi**
```

## Condition

Une condition est une comparaison.

Comprends 3 éléments : 
- Valeur
- Opérateur de comparaison
- Une autre valeur

## Les test imbriqués
```
Variable Temp en Entier
Début
Ecrire "Entrez la température de l’eau :"
Lire Temp
Si Temp =< 0 Alors
  Ecrire "C’est de la glace"
SinonSi Temp < 100 Alors
  Ecrire "C’est du liquide"
Sinon
  Ecrire "C’est de la vapeur"
Finsi
Fin
```

# Encore de la logique

## ET, OU

'Dans une condition composée employant à la fois des opérateurs ET et des opérateurs OU, la présence de parenthèses possède une influence sur le résultat, tout comme dans le cas d'une expression numérique comportant des multiplications et des additions.'

'Toute structure de test requérant une condition composée faisant intervenir l'opérateur ET peut être exprimée de manière équivalente avec un opérateur OU, et réciproquement.'

Cette règle d'équivalence se nomme la transformation de Morgan : 

```
Si A et B Alors
  Instructions 1
Sinon
  Instruction 2
Finsi

équivaut à :

Si NON A OU NON B Alors
  Instruction 2
Sinon 
  Instruction 1
Finsi

```

## Le style 

"Dans une structure alternative complexe, les conditions composées, l'imbrication des structures de tests et l'emploi des variables booléennes ouvrent la possibilité de choix stylistiques différents. L'alourdissement des conditions allège les structures de test et le nombre des booléens nécessaires; l'emploi de booléens supplémentaires permet d'alléger les conditions et les structures de tests, et ainsi de suite."

# Les boucles

Syntaxe 

```
TantQue booléen
  Instructions
finTantQue
```

Par exemple 
```
Variable Rep en Caractère
Début
Rep <-- "X"
Écrire "Voulez vous un café? (O/N)"
Lire Rep
TantQue Rep <> "0" et Rep <> "N"
  "Vous devez répondre par O ou N. Recommencez"
  Lire Rep
FinTantQue
Écrire  "Saisie acceptée"
Fin
```

## La structure Pour...Suivant

```
Variable Truc en Entier
Début
Pour Truc <-- 1 à 15 Pas ValeurDuPas (2 par exemple)
  Écrire "Passage numéro : ", Truc
Truc Suivant
Fin
```


# Les tableaux

"Un ensemble de valeurs portant le même nom de variable et repérées par un nombre, s'appelle un tableau, ou encore une variable indicée.
Le nombre qui, au sein d'un tableau, sert à repérer chaque valeur s'appelle l'indice. 
Chaque fois que l'on doit désigner un tableau, on fait figurer le nom du tableau, suivi de l'indice de l'élément, entre parenthèses."


## Tableaux dynamique
"Il est possible de déclarer le tableau sans préciser au départ son nombre d'éléments. Ce n'est que dans un second temps, au cours du programme, que l'on va fixer ce nombre via une instruction de redimensionnement : Redim
Tant qu'on n'aa pas précisé le nombre d'éléments d'un tableau, d,une manière ou d'une auter, ce tableau est inutilisable."


```
Tableau Notes[] en Numérique
Variable nb en Numérique
Début
Ecrire "Combien y a-t-il de notes à saisir ?"
Lire nb
Redim Notes[nb-1]
```
# Techniques rusées

## Tri d'un tableau 

### Tri par sélection

```
//boucle principale : le point de départ se décale à chaque tour. 
Pour i <-- 0 à 10
//on considère provisoirement que t[i] est le plus petit element
    posmini  <-- i
// on examine tous les éléments suivants
    Pour j  <-- i + 1 à 11
        Si t[j] <t[posmini] Alors
            posmini  <-- j
        Finsi
    j suivant

// A cet endroit, on sait maintenant o`u est le plus petit élément. Il ne reste plus qu'à effectuer la permutation
    temp  <-- t[posmini]
    t[posmini]  <-- t[i]
    t[i] <-- temp
//On a placé correctement l'élément numéro i, on passe à présent au suivant
i suivant
```

Variation de l'algorithme de triage


```
//boucle principale : le point de départ se décale à chaque tour. 
Pour i <-- 0 à 10
// on examine tous les éléments suivants
  Pour j  <-- i + 1 à 11
    Si t[j] <t[i] Alors
      temp  <-- t[i]
      t[i]  <-- t[j]
      t[j]  <-- temp

    Finsi
  j suivant
i suivant
```

Recherche dans une liste à l'aide d'un drapeau
```
Tableau Tab[19] en Numerique
Varaible N en Numerique
Debut
Ecrire "Entrez la valeur à rechercher"
Lire N
i <-- 0
TantQue N <> T[i] et i < 19
  i <-- i + 1
Fin Tant Que

Si N = Tab[i] Alors
  Ecrire " N fait partie du tableau"
Sinon
  Ecrire " N ne fait pas partie du tableau"
FinSi
Fin
```

## Tri de tableau + flag = tri à bulles

```
Variable Yapermute en Boolen 
Debut
...
Yapermut <-- Vrai
TantQue Yapermut
  Yapermut <-- Faux
  Pour i <-- 0 à 10
    Si t[i] > t[i + 1] alors
      temp <-- t[i]
      t[i] <--  t[i+1]
      t[i+1] <-- temp
      Yapermut <-- Vrai
    Finsi
  i suivant
FinTantQue
Fin
```
# Tableaux multidimensionnels

Syntaxe `Tableau Cases[7,7] en Numerique`
"Il n'y a aucune différence qualitative entre un tableau à deux dimensions [i,j] et un tableau à une dimension [i*j]. De même que le jeu de dames qu'on vient d'évoquer, tout problème qui peut être modélisé d'une manière peut aussi être modélisé de l'autre. Simplement, l'une ou l'autre de ces techniques correspond plus spontanément à tel ou tel problème, et facilite donc (ou complique, si on a choisi la mauvaise option) l'écriture et la lisibilité et l'algorithme."

# Les fonctions prédéfinies

Syntaxe : `A <-- Sin(35)`

Parties d'une fonction
- Nom de la fonction.
- Deux parenthèses
- Les arguments ou paramètres

# Les fichiers

## Organisation des fichiers
Binaire et texte

## Structure des enregistrements
- Délimitation : utilise des caractères de délimitation. Aucun espace perdu mais plus lent à la lecture

- Champs de largeur fixe : gaspillage de place mémoire mais très rapide

## Types d'accès
- "Accès séquentiels "on ne peut accéder qu'à la donnée suivant celle qu'on vient de lire. On ne peut donc accéder à une information qu'en ayant au préalable examiné celle qui la précède. Dans le cas d'un fichier texte, cela signifie qu'on lit le fichier ligne par ligne (enregistrement par enregistrement).
- Accès direct (ou aléatoire) : "on peut accéder directement à l'enregistrement de son choix, en précisant le numéro de cet enregistrement. Mais cela veut souvent dire une gestion fastidieuse des déplacements dans le fichier."
- Accès indexé : "pour simplifier, il combine la rapidité de l'accès direct et la simplicité de l'accès séquentiel (en restant toutefois plus compliqué). il est particulièrement adapté au traitement des gros fichiers, comme les bases de données importantes. "

## instruction (fichier texte en accès séquentiel)
1. Ouvrir ;  `Ouvrir "Exemple.txt" sur 4 en Lecture
   1. numero de canal --> un seul par document
   2. Type de manipulation : lecture, ecriture (rewrite everything) et ajout

```
Variables Truc, nom, Prenom, Tel, Mail en Caracteres
Debut
Ouvrir "Exemple.txt" sur 4 en Lecture
LireFichier 4, Truc
Nom <-- Mid(Truc, 1, 20)
Prenom <-- Mid(truc, 21, 15)
Tel <-- Mid(Truc, 36, 10)
Mail <--(Truc, 46, 20)
```

```
Tableaux Nom[], Prenom[], Tel[], Mail[] en Caractere
Debut
Ouvrir "Exemple.txt" sur 5 en lecture
i <-- -1
Tantque Non EOF(5)
  LireFichier 5, Truc
  i <-- i + 1
  Redim Nom[i]
  Redim Prenom[i]
  Redim Tel[i] 
  Redim Mail[i] 
  Nom[i] <-- Mid(Truc, 1, 20)
  Prenom[i] <-- Mid(truc, 21, 15)
  Tel[i] <-- Mid(Truc, 36, 10)
  Mail[i] <--(Truc, 46, 20)
FinTantQue
Fermer 5
Fin
```
Plus simple :
```
Ouvrir "Exemple.txt" sur 3 en Ajout
Varaible Truc en Caract'res
Varaibles Nom*20, Prenom*15, Tel*10, Mail*20 en Caracteres
Nom ← "Jokers"
Prénom ← "Midnight"
Tel ← "0348946532"
Mail ← "allstars@rockandroll.com"
Truc ← Nom & Prénom & Tel & Mail
Ecrire Fichier 3, TrucCaractere
```

## Stratégies de traitement (de fichiers textes)
- Modification direct 
  - Pour supprimer un élément d'un fichier : "on programme alors une boucle avec un test, qui recopie dans un deuxième fichier tous les tous éléments du premier fichier sauf un; et il faut ensuite recopier intégralement le deuxième fichier à la place du premier fichier... ouf.
- Utiliser des tableaux
  - Le principe fondamental de cette approche est de commencer, avant toute autre chose, par recopier l'intégralité du fichier de départ en mémoire vive. ensuite on ne manipule que cette mémoire vive. Et lorsque le traitement est terminé, on recopie à nouveau dans l'autre sens, depuis la mémoire vive vers le fichier d'origine. "
    - Plus rapide et plus facile à prog

## Données structurées
Variable structurée : "Une série d'emplacements pour des données de type différents." Permet de : "pouvoir calquer chacune des lignes du fichier en mémoire vive, et considérer que chaque enregisterment sera recopié dans une variable et une seule qui lui sera adaptée."

```
Structure Bottin
  Nom en Caractere * 20
  Prenom en Caractere * 15
  Tel en Caractere * 10
  Mail en Caractere * 20
Fin Structure

Variable Individu en Bottin
Variable Individu2 en Bottin

Individu <-- "Joker", "Midnight", "4509993333", "from@age.mmm"


Individu2.Nom <-- "Joker" "Midnight", "4509993333", "from@age.mmm"
Individu2.Prenom <-- "Midnight"

Individu2.Tel <--  "4509993333"

Individu2.Mail <-- "from@age.mmm"
```


Tableaux de données structurées
```
Structure Bottin
  Nom en Caractere * 20
  Prenom en Caractere * 15
  Tel en Caractere * 10
  Mail en Caractere * 20
Fin Structure

```
```
Tableau MesPotes[] en Bottin
Debut
Ouvrir "Exemple.txt" sur 3 en Lecture
i <-- -1 
tantque Non EOF(3)
  i <-- i + 1
  Redim Mespotes[i]
  LireFichier 3, Mespotes[i]
FinTantQue
Fermer 3
Fin
```
# Procédures et fonctions
Syntaxe : 
```
Fonction RepOuiNon() en caractère
Truc <-- ""
TantQue Truc <> "Oui" et Truc <> "Non"
  Ecrire "Taper Oui ou Non"
  Lire Truc
FinTantQue
Renvoyer Truc
fin

Ecrire "Etes-vou marié?"
Rep1 <-- RepOuiNon()
```


# Notions Complémentaire
## Programmation structuré
"Une règles d'hygiène absolue est de programmer systématiquement de manière structurée, sauf impératif contraire fixé par le langage (ce qui est aujourd'hui de plus en plus rare)

## Interprétation et compilation
Fait

##

