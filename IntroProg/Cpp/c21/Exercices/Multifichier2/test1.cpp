#include<iostream>
#include"Header.h"
using namespace std;
int Var1 = 1; /*Varaible externe visible dans tout le monde et même dans les autres modules (variables globales)*/

static int Var2 = 2; /*Variable dont la visibilité est restreinte au module */

extern Var6; /*Variable qui a été définie dans un autre module*/

int Fct2(int Var10); /*Declaration de fonction*/

int Fct3(int Var8); /*Declaration de fonction*/

int Fct1(int Var9); /*Declaration de fonction*/
void main(void) {
	int Var3 = 2;
	cout << "main : Var1 1: " << Var1
		<< "Var1 2 : \n" << Var2
		<< "Var1 3 : \n" << Var3
		<< "Var1 4 : \n" << Var4
		<< "Var1 5 : \n" << Var5
		<< "Var1 6 : \n" << Var6
		<< "Var1 7 : \n" << Var7
		<< "Var1 8: \n" << Var8;



	
}

int Fct1(int Var9) { /*Définition de fonction*/
	int Var3 = 4; /*Définition et déclaration d'une variable locale*/
	register int Var4; /*Variable de classe register*/
	static int Var5; /*Variable locale mais à durée de vie permanente */
	extern var7; /*Variable locale définie dans un autre module*/
	cout << "fct1 : \n var1  " << Var1 << "\n var 2 : " << Var2 << "\n var 3 : " << Var3;
} 
