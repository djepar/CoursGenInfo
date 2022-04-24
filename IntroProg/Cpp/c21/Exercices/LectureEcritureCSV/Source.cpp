#include"Header.h"
#include<iostream>
#include<string>

void main(void) {
	Contact_s contact[3];
	contact[0] = { "Borduas", "Godefroy", "42", {13, 12, 1919} };
	contact[1] = { "Bidule", "Marilou", "80", {14, 02, 1949} };
	contact[2] = { "Machin", "Philippe", "70", {11, 04, 1972} };

	EcrireCSV("C:\\Test1\\contacts.csv", contact, 3);

//	Contact_s contacts_lus[3];
	//LireCSV("Y:\\contacts.csv", contacts_lus, 3);
	/*for (int i = 0; i < 3; i++)
	{
		cout << contacts_lus[i] << "\n";
	}*/
}