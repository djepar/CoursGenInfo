#include<string>
#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
#include"Header.h"

void main(void) {
	cout << "Ceci sera réécrit si le fichier existe : " << endl;
	EcrireOut();
	cout << "Lecture du fichier Bibliotheque : " << endl;
	LireIn();
	CompterChar();
	
}