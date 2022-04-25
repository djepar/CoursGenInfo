#Les bases
    http://www.binaryconvert.com/
    https://www.h-schmidt.net/FloatConverter/IEEE754.html
    https://babbage.cs.qc.cuny.edu/ieee-754.old/decimal.html
    Les règles sont les mêmes pour tous les systèmes numériques
        Les bases = nombre de chiffre (base 3 = 3 chiffres, etc)
        Nombres = Les chiffres qui sont assemblés en colonnes.
        Chaque colonne vaut base x + la précédente, EN PARTANT DE LA DROITE. 

    L'hexadécimal est utilisé pour racourcir pour les utilisateur.trices des nombres très grands, comme des adresses IPv6.
## Convetir un entier
Regarder si signé ou pas signée.
Si signé : 
    Positif : 
        1. Transformer l'entier en binaire
        2. Compléter avec des zéros non significatifs si nécessaire.

    Négatif:
        Le bit le plus à gauche est le bit de signe : 1 = négatif 0 = positif
        1. Transformer la valeur absolue de l'entier en binaire.
        2. Compléter avec des zéros non significatifs si nécessaires.
        3. Complémenter (à partir de la droite, recopier les chiffres jusqu'aux premier 1 inclusivement et inverser les autres. )

    


Si pas signé: 
    Positif :
        1. transformer l'entier en binaire.
        2. Compléter avec des zéros non significatifs si nécessaire.
    Négatif: 
        Impossible


## Convertir Reel 
### Convertir Reel décimal vers binaire
1. Convertir la partie entière de nombre décimal en binaire
2. Convertir la partie fractionnaire en binaire. 
3. Concaténer. 
4. Normaliser pour obtenir la forme mantisse*base^exposant 
5. Convertir l'exposant avec la méthode +127/1023 puis mettre en binaire
6. Enlever le 1 de la mantisse et placer la mantisse dans la section de bit 22 à 0
7. Mettre le bit de signe (dernier : 23e ou 63e) : 0 pour un nombre positif, 1 pour un nombre négatif
8. convertir en hexadécimal
### Convertir Reel binaire vers décimal
1. Convertir le binaire ne hexadécimal
2. Récupérer la mantisse(ajouter 1 au début)
3. Récupérer l'exposant des bits 23 à 30 inclusivement (8 bits) pour du 32 bits ou 62 à 52  (11 bits) - 127 /-1023
4. Dénormaliser 
5. Convertir en décimal
6. Ajuster le signe : bit 31 ou 63 = signe.

Gabarit général : 
32 bits 
    31e bit |  30 à 23 (8bits) | Bits 22 à 0 (23 bits)
    Signe   |   Exposant       | Mantisse
64 Bits
    63e bit |  62 à 52 (11bits) | Bits 51 à 0 (52 bits)
    Signe   |   Exposant       | Mantisse
# Les unités de mesures
## Hertz : calcul de la fréquence
    -Méga-hertz(MHZ) = 1 million d'impulsion par seconde
    -Giga-hertz(GHz) = 1 Ghz = 1000 MHz, soit 1 000 000 000 (mille million)

## Micron et nanomètre : mesuré le très petit
    -Le micron (µ). 
        -Un micron = 1 millionième de mètre.
    -Le nanomètre (nm). 
        -Un micron = 1000 nanomètres.
    Ex : .18 µ = 180 nm.





# Carte-mère 
Circuit imprimé principal sur lequel les autres composants sont soudés ou connectés. 
## Composants d'une carte-mère
Composants secondaires du chipset
    Se retrouve éparpillés sur la carte.
composant principal 
    Normalement recouvert d'un dissipateur de chaleur. 
Connecteurs de barettes de mémoire. 

# Le CPU (central processing unit), processeur ou micro-processeur.
    La composante la plus rapide d'un ordinateur. 
    Fait référence à l'ensemble des composants gravé sur une puce. 
    Une puce est un carré de silicium sur lequel est gravé le CPU sous forme de circuit. 

## Caractéristiques principales des processeurs :
    -Largeur 
        -Largeur du bus : la taille du circuit fait référence à la finesse de la gravure de ce circuit. C'est la plus petite distance possible entre 2 composants du CPU.
            -Plus la taille est petite, moins il y a de distance entre deux composants et permet de placer plus de composant sur une même puce.
        -Largeur des bus
            -Donnée
            -Adresses
            -Régistre
        -Mémoire adressable (parfois écrit Mémoire Max.) : 2^n = RAM possible
        avec N bits de bus d’adresse, je peux adresser 2N cases mémoires (octets).
        La mémoire adressable est la mémoire maxium 
            Si 128go de mémoire adressable : 
            128 go *1024*1024 = 17 179 869 184 octets 
            Donc il y a 2^34 adresses
            Si 1To de mémoire adressable   
                2^40 adresses ou 1To de mémoire adressable
        -Mémoire cache : Mémoire additionnelle située entre le RAM et le processeur pour stocker les commandes les plus utilisés. 
            -Fonctionne par cascade : Cherche dans L1, si pas dans L1, cherche dans L2 puis L3.


    -Sa fréquence /vitesses (nombres de cycles par secondes, la cadence à laquelle le CPU peut fonctionner, indique en MHz ou en GHz)
        -C'est un petit cristal sur la carte-mère ou sur le processeur qui émet un certain nombre d'impulsion par seconde (** cycle**).
        -**Vitesse d'Horloge** : 
            Si DDR / 2
            Définition : !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            Avant L'Intel80486DX2 : le CPU suie la fa vitesse d'horloge de la carte-mère
            Après : CPU supérieur à la carte-mère et calculé en facteur multiplicatif de la carte-mère 
                Ex: 4x (plus vite que la carte-mère)
        -**Taux de transfert** 
            Pour calculer le taux de transfert du RAM au CPU par seconde.
            Vitesse de la RAM * 2 (si DDR) * Nombre de barettes par canaux) * taille du régistre en octet / 8 (les spécifications de RAM prennent toujours en compte le DDR, donc on fait pas *2 dans ces cas-là )
                2600 Mhz* 8
            Reponse Mb/s gb/s ou Mo/s ou Go/s
        -Nombre de coeurs et hyperthreading
            Les coeurs permettent des opérations simultanément. 
            L'hyperthread permet à un même coeur de faire plus d'une opération si le logiciel est programmé pour le permetttre. 
        


## Tâches effectuées par le CPU
    -Executer les instructions des programmes
    -Gérer les communications avec ses périphériques

## L'éxécutions des instructions des programmes par le CPU
    Par commodité, les représentations schématique représentent la mémoires en RAM. 

## Les composantes du CPU

### Régistres
    -Case mémoire à l'intérieur du CPU. 
    -Stocke temporairement les informations nécessaires pour l'exécution des opérations
        -Signaux de contrôle
        -Données
        -Adresses
    -On parle d'un processeur 32 ou 64 bits en faisant références à la quantité du régistres. 

### UAL
    Unité arithémtique et logique (pour les calculs)
### Coprocesseur mathématiques

### Lots d'instructions
    L'ensemble des instructions lisibles par le micro-processeur écrit en langage-machine. 
    Lors de l'écriture de programme plus complexe, un compilateur traduit le langage de programmation en langage-machine. 

    Listes des instructions
        -Les premières sur la 8086 
        -Instructions MMX (57 instructions, surtout multimédia), sort avec Pentium 1
        - Instruction SSE (70 nouvelles instructions multimédias pour améliorer les effets 3D. Ses instructionns continennent également les instructions MMX)
        -Instructions SSE2(144 nouvelles instructions : effets 3D, traitement audi, SSE2 contient SSE)
        -Instructions SSE3(13 nouvelles instructions, amélioration des calculs plus complexes)
        Technologie de virtualisations

### Unité de contrôe : 
-   Composante qui dirige les opérations à l'intérieur du CPU. 
    -   Controleur de Ram et controleur vidéo mis sur le CPU pour aller plus vite,  puisque la fréquence de la carte mère est inférieure à celle du CPU. 

    

### Bus 
    Voies de communications entre toutes les composantes de l'ordinateur. 

    Les types de Bus
    -Les bus de contrôle véhiculent les commandes du CPU vers la RAM. 
    -Les bus d'adresses véhiculent les adresses de l'unité de contrôle à la RAM. 
    -Les bus de données servent à véhiculer le contenu des adresses de la RAM.

### La cache
    L1 : 8k au départ, toujours sur le processeur.
    L2 : commence sur la carte-mère puis sur le processeur. 
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## Les étapes d'éxécution d'une instruction. 
    -Étape 1 : 
        -L'unité de contrôle demande à la RAM de lui envoyés les prochaines instructions à exécutée. 
        -La RAM envoie la valeur demandée dans un des régistres du CPU.
    -Étape 2 :
        -L'unité de contrôle demande à la RAM le contenu des variables.
        -La RAM envoie **une copie** du contenu des variables de la RAM dans un des régistres. 
    -Étape 3 :
        -L'unité de contrôle demande l'exécution de l'opération arithmétique par l'UAL (unité arithémtique et logique).
    -Étape 4 :
        -L'unité de contrôle place le résultat de l'opération arithémtique dans un autre régistre du CPU.
    -Étape 5 : 
        -L'unité de contrôle demande à la RAM de placer le résultat dans la variable résultante. (exemple C si l'instruction était C = A+B)
        -L'unité de contrôle demande ensuite à la RAM de lui envoyer l'instruction suivante. 

## Adresses en RAM
    Les adresses servent à l'ordinateur tandis que le nom
    .0 1des variables sert aux personnes qui programment. 


## Communication entre le GPU et les autres composants
    Le CPU  s'occupe principales des instructions d'ordre mathématiques, des tests et des boucles, le reste est fait par ses périphériques. 
    Le CPU communique avec les **contrôleurs de chacun des périphériques **. 
    Les contrôleurs sont représentés par un carré bleu dans les schémas. 

## Multi-coeur et Hyperthreading 
    L'hyperthreading ou multithreading permet au processeur de faire deux actions(fils ou thread) presque simultanément.
        L'hyperthreading est la capacité de simulé un deuxième processeur appelé processeur logique. 
        Augmentation de la performance d'environ 25%
        Le programme doit inclure la capacité de multhreadés pour fonctionner. 
    Multicoeur
        Faire des opérations simultanéments.
    Turbo-boost : accèlerent temporairement la cadence du processeur. (+ de chaleur)
## Historique des CPU 

### Structure de base : l'intel 8086
    L'Intel 8086, mis en marché en juin 78 est le premier à être commercialisé au public. 
    -Fréquence : 5-10 MHz
    -Régistres : 16bits 
    -Bus de donnes : 16 bits
        Signé 2^(n-1),(2^(n-1))-1 : 
            -Valeur minimum : 2^15 (-32768)
            -Valeur max :  2^15-1 (32767)
        Non-signé (0, 2^n-1) : 
            -Valeur minimum : 0
            -Valeur max : 2^16-1
    -Bus d'adresses : 20 bits
    -Mémoire adressable : 1 Mo
        
        Bus d'adresses = 20 bits alors 2^20 = 1 048 576 adresses possible
        En ram, une adresse = 1 octet de donnée
        1048 576 octets /1024 =1024 ko
        1024 ko / 1024 = 1mo

    L'Intel 80286 
        En février 82
        Bus d'adresses plus grands (24 bits) donc plus de mémoire adressable.
            2^24 /1024/1024 = 16 mo de **mémoire adressable** 
        Coprocesseur mathématique intégré dans le CPU, (en plus de l'UAL qui était déjà-là)
    
    L'Intel 80386 dx
        En octobre 85
        Les trois bus ont une largeur de 32 bits. 
        Si adresses =32 bits, alors 4 Go de mémoire adressable

    L'Intel 80386 SL (portables)
        En Octobre 90
        Tension diminue à 3.3 volts.
        Moins chaud. 
    
    L'Intel80486
        Avril 89
        Ajout de la cache L1 de 8k
    
    L'Intel80486 DX2
        La vitesse de la carte-mère et la vitesse du CPU diffère. 

    Pentium 1 
        Bus de données :64 bits (prend deux cycles pour que les régistres se remplissent, puisqu'ils ont 32 bits)
        Cache : 2* 8k (instructions et données)
        Cache L2 sur carte-mère (256K ou 512k)

    Pentium 1 MMX
        Ajout des instructions MMX : 57 instructions par rapport aux générations précédentes. 
        Coprocesseur mathématique intégré :
    
    Xeon : haut de gamme : pour serveur
    Celeron : entré de gamme

    PIII :
        Février 1999
        Instruction SSE (70 nouvelles instructions multimédias pour améliorer les effets 3D. Ses instructionns continennent également les instructions MMX)

    PIIIv2
        Vitesse du CPU : 1GHZ, le MHZ est dépassé. 
        L2 intégrés à la vitesse du CPU. 
    
    P4 
        Instructions SSE2(144 nouvelles instructions : effets 3D, traitement audi, SSE2 contient SSE)
    
    P4v2 
        Quelques modèles ont l'hyperthreading qui permet de simuler un deuxième 
    P4v3
        SSE3
        Technologie de virtualisation (virtualisation technology)

    Pentium D (Dual Core)
        Physiquement, le Pentium 4 est reliés par un bus sur une même puce (2 circuits)


    Pentium Core 2 Duo
        Physiquement 2 core côte à côte sur une même puce (1 circuit)
           
    Core i7 v1
        Cache L3 : 8Mo intégrée
        Contrôleur de RAM et contrôleur vidéo intégrés
            Avant 
                CPU ---- Bus ---- Contrôleur de RAM ----- Bus -----RAM
            Après
                CPU(comprenant le contrôleur ram) -----Bus -----RAM
            Avantage : le CPU gagne du temps car il n'a pas à aller sur la carte-mère pour faire la requête au contrôleur de RAM (la fréquence de la carte-mère est inférieurs à celle du CPU)



    


