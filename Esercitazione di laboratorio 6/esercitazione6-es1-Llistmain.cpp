// esercizio nuotatori

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <time.h>  // Used by timing functions

using namespace std;

// Include the link template class
#include "link.h"

// Include the linked list template class
#include "llist.h"

// Generic list test commands
#include "esercitazione6-es1-ListTest.h"

const int best_swimmers = 10;

void selectionsort(List<Item>& L) {
	int min_pos;
	int min_value;
	Item it_curr;
	Item it_temp;
	// se lunghezza <2 non fai nulla
	for (int i = 0; i<(L.length() - 1); i++) {
		L.moveToPos(i);
		it_curr = L.getValue();
		min_pos = i;
		min_value = it_curr.key().tot_secondi;
		for (int j = i + 1; j<L.length(); j++) {
			L.moveToPos(j);
			it_temp = L.getValue();
			if (it_temp.key().tot_secondi < min_value)
			{
				min_pos = L.currPos();
				min_value = it_temp.key().tot_secondi;
			}
			L.next();
		}
		L.moveToPos(min_pos);
		it_temp = L.remove();
		L.moveToPos(i);
		L.insert(it_temp);
	}

}



// Main routine 
int main(int argc, char** argv) {

	LList<Item> Lnuotatori;

	nuotatore swimmer;
	string dati;
	int centesimi;

	ifstream myfile("50rn.txt");
	if (myfile.is_open()) {
		while (!myfile.eof()) {
			getline(myfile, swimmer.nome, ';');
			getline(myfile, dati);
			istringstream token(dati);
			token >> swimmer.minuti >> swimmer.secondi >> centesimi;

			swimmer.tot_secondi =  (float) ((swimmer.minuti * 60 * 100) + (swimmer.secondi * 100) + centesimi) / 100;
			Item temp(swimmer);
			Lnuotatori.append(temp);
		}
	}
	myfile.close();

    cout << "Lnuotatori: "; lprint(Lnuotatori);
	selectionsort(Lnuotatori);
	cout << endl << "Lnuotatori: "; lprint(Lnuotatori);

	ofstream myoutput_file("top_ten.txt");
	Lnuotatori.moveToStart();
	cout << "best " << best_swimmers << " swimmers" << endl;
	for (int i = 0; i < best_swimmers; i++) {
		Item temp=Lnuotatori.getValue();
		cout << endl << temp;
		if (i!=0) myoutput_file << endl;
		myoutput_file << temp.key().nome << " " << temp.key().tot_secondi;
		Lnuotatori.next();
	}

	myoutput_file.close();
	Lnuotatori.clear();

    cout << endl << "That is all.\n";

  return 0;
}