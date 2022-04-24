#include<string>
#include<iostream>
using namespace std;
#include"Header.h"



void main(void) {
	nombre_s nombresource;
	nombresource.nombreint = 3;
	nombresource.nombrefloat = 2.2;
	float floaty;
	cout << "nombresource.nombrefloat = " << nombresource.nombrefloat <<endl;
	floaty = addition(nombresource.nombreint, nombresource.nombrefloat);
	cout << "add = " << floaty;
}
