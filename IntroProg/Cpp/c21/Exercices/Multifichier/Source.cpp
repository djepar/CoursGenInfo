#include<iostream>


void main(void) {
	int i = 42;
	if (i > 0) {
		int j = 0;
		i += j; //fin de vie de j
	}
	else {
		int k = 8;
		if (k < 10) {
			int l = 10;
			k *= l;
			i += k; // fin de fvie de l
		}
		// fin de vie de k
	}
	//fin de vie de i
}