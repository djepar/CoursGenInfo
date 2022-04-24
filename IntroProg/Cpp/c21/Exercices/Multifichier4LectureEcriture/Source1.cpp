#include<string>
#include<iostream>
#include<fstream>
#include<conio.h>
#include<Windows.h>
using namespace std;
#include"Header.h"

void EcrireOut() {
	fstream Bibliotheque;
	char Car;
	Bibliotheque.open(".\\bibliotheque.txt", ios::out);

	Car = _getch();
	while (Car != '\r') {
		Bibliotheque << Car;
		Car = _getche();

	}
	Bibliotheque.close();
	return;
}
void LireIn() {
	fstream Bibliotheque;
	char Car;
	Bibliotheque.open(".\\bibliotheque.txt", ios::in);
	if (Bibliotheque.fail())
	{
		MessageBoxA(NULL, "Le fichier ne peut être ouvert",
			"ERREUR", MB_OK | MB_ICONSTOP);
		exit(EXIT_FAILURE);
	}

	Car = Bibliotheque.get();
	while (!Bibliotheque.eof()) {
		cout << Car;
		Car = Bibliotheque.get();

	}
	Bibliotheque.close();
	return;
}
void CompterChar() {
	fstream Bibliotheque;
	int NombredeChar;
	Bibliotheque.open(".\\bibliotheque.txt", ios::in);
	if (Bibliotheque.fail())
	{
		MessageBoxA(NULL, "Le fichier ne peut être ouvert",
			"ERREUR", MB_OK | MB_ICONSTOP);
		exit(EXIT_FAILURE);
	}

	NombredeChar = 0;
	Bibliotheque.get();
	while (!Bibliotheque.eof()) {
		NombredeChar++;
		Bibliotheque.get();
	}
	Bibliotheque.close();
	cout << "Le fichier contient : " << NombredeChar << " caractères.";
}