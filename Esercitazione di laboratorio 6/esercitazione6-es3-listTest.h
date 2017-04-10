// From the software distribution accompanying the textbook
// "A Practical Introduction to Data Structures and Algorithm Analysis,
// Third Edition (C++)" by Clifford A. Shaffer.
// Source code Copyright (C) 2007-2011 by Clifford A. Shaffer.

#ifndef LISTTEST_H
#define LISTTEST_H

#include<list.h>


// Your basic int type as an object.
class Item {
private:
  int anno;
  string nome;
  string nazione;

public:
  Item() {}
  Item(int a, string n, string country) { anno = a; nome = n; nazione = country; }
  // The following is for those times when we actually
  //   need to get a value, rather than compare objects.
  string key() const { return nome; }
  string getnazione() const { return nazione; }
  int getanno() const { return anno; }
};

// Let us print out Items easily
ostream& operator<<(ostream& s, const Item& i)
  { return s << "(" << i.getanno() << " "<< i.key() << " " << i.getnazione() << ")"; }


class Ciclista {
private:
	string nome;
	int vittorie;
	int min_anno_vittoria;
	int max_anno_vittoria;
public:
	Ciclista() {}
	Ciclista(string n) { nome = n; vittorie = 0; }
	// The following is for those times when we actually
	//   need to get a value, rather than compare objects.
	string key() const { return nome; }
	void setvittorie(int v) { vittorie=v; }
	void setminanno(int a) { min_anno_vittoria = a; }
	void setmaxanno(int a) { max_anno_vittoria = a; }
	int getminanno() const { return min_anno_vittoria; }
	int getmaxanno() const { return max_anno_vittoria; }
	int getvittorie() const { return vittorie; }
};

ostream& operator<<(ostream& s, const Ciclista& i)
{
	return s << "(" << i.key() << " " << i.getvittorie() << ")";
}


// Assert: If "val" is false, print a message and terminate
// the program
void Assert(bool val, string s) {
  if (!val) { // Assertion failed -- close the program
    cout << "Assertion Failed: " << s << endl;
    exit(-1);
  }
}

// Print out the list (including showing position for the fence)
// Print list contents
template <typename E>
void lprint(List<E>& L) {
  int currpos = L.currPos();

  L.moveToStart();

  cout << "< ";
  int i;
  for (i=0; i<currpos; i++) {
    cout << L.getValue() << " ";
    L.next();
  }
  cout << "| ";
  while (L.currPos()<L.length()) {
    cout << L.getValue() << " ";
    L.next();
  }
  cout << ">\n";
  L.moveToPos(currpos); // Reset the fence to its original position
}





#endif

