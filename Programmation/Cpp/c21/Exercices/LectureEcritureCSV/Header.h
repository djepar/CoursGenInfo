#ifndef HEADER_H
#define HEADER_H

#include <ostream>
#include <fstream>
#include <string>


struct Date_s
{
	int Jour,
		Mois,
		Annee;
};

struct Contact_s
{
	std::string Nom,
		Prenom,
		Telephone;
	Date_s DateNaissance;
};

void EcrireCSV(string path, Contact_s contacts[], int nbreContact);
#endif // !HEADER_H