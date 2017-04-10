#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <time.h>

using namespace std;

#include "link.h"

#include "llist.h"

#include "esercitazione6-es1-ListTest.h"

//#include "Llistmain_test_sort.cpp"

const int best_swimmers = 10;

int main() 
{
	int m, s, cs;
	float tempotot;
	string cn;
	LList<Item> Nuotatori(100);

	ifstream myfile("50rn.txt");
	if (myfile.is_open()) 
	{
		while(!myfile.eof()) 
		{
			getline(myfile, cn, ';');
			myfile >> m >> s >> cs;
			tempotot = ((m*60*100)+(s*100)+cs)/100.0;
			Item A(cn, m, s, tempotot);
			Nuotatori.append(A);
		}
	}
	selectionsort(Nuotatori);
	lprint(Nuotatori, 0, 10);
	
	ofstream fileout("top_ten.txt") ;
	if (fileout.is_open()) 
	{
		lprint(Nuotatori, 0, 10, fileout);
	}
	Nuotatori.clear();
	return 0;
}