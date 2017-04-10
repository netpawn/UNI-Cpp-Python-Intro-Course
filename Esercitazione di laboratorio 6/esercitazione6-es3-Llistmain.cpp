// Esercizio albo d'oro Giro d'Italia

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
#include "esercitazione6-es3-ListTest.h"


// find function for Items.
int find(List<Ciclista>& L, string nome) {
	Ciclista it;
	for (L.moveToStart(); L.currPos()<L.length(); L.next()) {
		it = L.getValue();
		if (nome == it.key()) return L.currPos();  // Found K
	}
	return -1;                // K not found
}


void bubblesort(List<Ciclista>& L) {
	for (int i = 0; i< (L.length() - 1); i++) {
		for (int j = (L.length() - 1); j> i; j--) {
			L.moveToPos(j);
			Ciclista it_j = L.getValue();
			L.moveToPos(j - 1);
			Ciclista it_jj = L.getValue();
			if (it_jj.getvittorie()<it_j.getvittorie())
			{
				L.moveToPos(j);
				Ciclista removed = L.remove();
				L.moveToPos(j - 1);
				L.insert(removed);
			}
		}
	}
}



// Main routine 
int main(int argc, char** argv) {

  LList<Item> Lalbo;  
  LList<Ciclista> Lciclisti;
  
  ifstream myfile("giro_italia.txt");
  string str,nome,nazione;
  int anno;

  if (myfile.is_open()) {
	  while (!myfile.eof()) {
		  getline(myfile, str, ';');
		  istringstream token(str);
		  token >> anno;

		  getline(myfile, nome, ';');
		  getline(myfile, nazione);
		  Item temp(anno, nome, nazione);
		  Lalbo.append(temp);
	  }
	  myfile.close();
  }
  cout << "Lalbo: "; lprint(Lalbo);

  for (Lalbo.moveToStart(); Lalbo.currPos()<Lalbo.length(); Lalbo.next()) {
	  Item it = Lalbo.getValue();
	  int ciclista_trovato = find(Lciclisti, it.key());
	  if (ciclista_trovato==-1)
	  {
		  Ciclista ciclista(it.key());
		  ciclista.setvittorie(1);
		  ciclista.setminanno(it.getanno());
		  ciclista.setmaxanno(it.getanno());
		  Lciclisti.append(ciclista);
	  }
	  else
	  {
		  Lciclisti.moveToPos(ciclista_trovato);
		  Ciclista ciclista=Lciclisti.getValue();
		  ciclista.setvittorie(ciclista.getvittorie()+1);
		  if (it.getanno() < ciclista.getminanno())
			  ciclista.setminanno(it.getanno());
		  if (it.getanno() > ciclista.getmaxanno())
			  ciclista.setmaxanno(it.getanno());
		  Lciclisti.remove();
		  Lciclisti.insert(ciclista);
	  }
  }

  bubblesort(Lciclisti);
  cout << endl << "Lciclisti: "; lprint(Lciclisti);

  int max_anni_dist = 0;
  for (Lciclisti.moveToStart(); Lciclisti.currPos()<Lciclisti.length(); Lciclisti.next())
  {
	  Ciclista ciclista=Lciclisti.getValue();
	  if ((ciclista.getmaxanno() - ciclista.getminanno()) > max_anni_dist)
		  max_anni_dist = ciclista.getmaxanno() - ciclista.getminanno();
  }
  cout << "ciclisti che hanno che hanno ottenuto vittorie piu' distanziate negli anni" << endl;
  cout << max_anni_dist << endl;
  for (Lciclisti.moveToStart(); Lciclisti.currPos()<Lciclisti.length(); Lciclisti.next())
  {
	  Ciclista ciclista = Lciclisti.getValue();
	  if ((ciclista.getmaxanno() - ciclista.getminanno()) == max_anni_dist)
		  cout << ciclista.key() << endl;
  }
  cout << endl << "That is all.\n";

  return 0;
}