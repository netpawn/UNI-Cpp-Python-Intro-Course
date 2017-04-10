// From the software distribution accompanying the textbook
// "A Practical Introduction to Data Structures and Algorithm Analysis,
// Third Edition (C++)" by Clifford A. Shaffer.
// Source code Copyright (C) 2007-2011 by Clifford A. Shaffer.

#ifndef LISTTEST_H
#define LISTTEST_H

#include <iostream>
#include <cstdlib>
#include <string>
#include <time.h>  // Used by timing functions
using namespace std;

#include "list.h"

// Your basic int type as an object.
class Item {
private:
  string cognome_nome;
  int minuti, secondi;
  float tempo_totale;
public:
  Item() {}
  Item(string cn, int m, int s, float tempotot)
  {
	  cognome_nome = cn; minuti = m; secondi = s; tempo_totale = tempotot;
  }
  // The following is for those times when we actually
  //   need to get a value, rather than compare objects.
  string get_cn() const { return cognome_nome; }
  int get_m() const { return minuti; }
  int get_s() const { return secondi; }
  float get_tt() const { return tempo_totale; }
};

bool operator<(Item A, Item B) { return A.get_tt() < B.get_tt(); }

// Let us print out Items easily
ostream& operator<<(ostream& os, const Item& i)
  { return os << i.get_cn() << ';' << i.get_m() 
  << " " << i.get_s() << " " << i.get_tt() << endl; }

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
void lprint(List<E>& L, int start = 0, int finish = 0, ostream& os = cout) {
  if(!finish) finish = L.length();
  int currpos = L.currPos();

  L.moveToStart();

  os << "< ";
  int i;
  for (i=start; i<finish; i++) {
    os << L.getValue() << " ";
    L.next();
  }
  os << ">\n";
  L.moveToPos(currpos); // Reset the fence to its original position
}

void selectionsort(List<Item>& L) {
	int min_pos;
	float min_value;
	Item it_curr;
	Item it_temp;
	// se lunghezza <2 non fai nulla
	for (int i = 0; i<L.length() - 1; i++) {
		L.moveToPos(i);
		it_curr = L.getValue();
		min_pos = i;
		min_value = it_curr.get_tt();
		for (int j = i + 1; j<L.length(); j++) {
			L.moveToPos(j);
			it_temp = L.getValue();
			if (it_temp.get_tt() < min_value)
			{
				min_pos = L.currPos();
				min_value = it_temp.get_tt();
			}
			L.next();
		}
		L.moveToPos(min_pos);
		it_temp = L.remove();
		L.moveToPos(i);
		L.insert(it_temp);
	}

}

void bubblesort(List<Item>& L) {
	for (int i = 0; i< (L.length() - 1); i++) {
		for (int j = (L.length() - 1); j> i; j--) {
			L.moveToPos(j);
			Item it_j = L.getValue();
			L.moveToPos(j - 1);
			Item it_jj = L.getValue();
			if (it_jj.get_tt()>it_j.get_tt())
			{
				L.moveToPos(j);
				Item removed = L.remove();
				L.moveToPos(j - 1);
				L.insert(removed);
			}
		}
	}
}

void merge(LList<Item>& Lm, LList<Item>& La, LList<Item>& Lb) {
	La.moveToStart();
	Lb.moveToStart();
	Item removed;
	int N = La.length();
	int M = Lb.length();
	for (int k = 0; k < N + M; k++)
	{
		if (La.currPos() == La.length())
		{
			removed = Lb.remove();
			Lm.append(removed);
			continue;
		}
		if (Lb.currPos() == Lb.length())
		{
			removed = La.remove();
			Lm.append(removed);
			continue;
		}
		if (La.getValue().get_tt()<Lb.getValue().get_tt())
			removed = La.remove();
		else
			removed = Lb.remove();
		Lm.append(removed);
	}
}

void mergesort(LList<Item>& Lm)
{
	if (Lm.length() < 2) return;
	LList<Item> La, Lb;
	Item removed;
	int N = Lm.length();
	for (int k = 0; k<N; k++) {
		removed = Lm.remove();
		if (k % 2) La.append(removed);
		else Lb.append(removed);
	}
	mergesort(La);
	mergesort(Lb);
	merge(Lm, La, Lb);
}



#endif

