/*
Exercice 2.4 Écrire un programme qui calcule la somme des cubes des nombres de 1 à 100. Faire afficher le résultat.

Quel est le résultat demandé? L'impression de tous les cubes des nombres un à cent. Donc, un long

Diagramme d'action
    Pour (i=0, i < 100, i++)
        total = i*i*i
        Ecrire "Ceci est un total "

*/
#include<iostream>

void Cube(void) {
    long total;
    for(int i = 0; i < 100; i++) {
        total = i*i*i;
        std::cout << "The cube of " << i << " is " << total;
    }

}
/*
Exercice 2.5 Afficher les 20 premiers entiers naturels (1 à 20), leur racine carrée, leur carré et leur cube.
Quel est le résultat demandé? 
*/
