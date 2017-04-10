// From the software distribution accompanying the textbook
// "A Practical Introduction to Data Structures and Algorithm Analysis,
// Third Edition (C++)" by Clifford A. Shaffer.
// Source code Copyright (C) 2007-2011 by Clifford A. Shaffer.

#ifndef LISTTEST_H
#define LISTTEST_H

#include<list.h>

struct nuotatore {
	string nome;
	int minuti;
	int secondi;
	float tot_secondi;
};

// Your basic int type as an object.
class Item {
private:
  nuotatore nuot;
public:
  Item() { }
  Item(nuotatore n) { nuot = n; }
  // The following is for those times when we actually
  //   need to get a value, rather than compare objects.
  nuotatore key() const { return nuot; }
};

// Let us print out Items easily
ostream& operator<<(ostream& s, const Item& i)
  { return s << "(" << i.key().nome << " " << i.key().tot_secondi << ")" ; }

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

