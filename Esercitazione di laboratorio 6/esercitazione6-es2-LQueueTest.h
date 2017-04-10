// From the software distribution accompanying the textbook
// "A Practical Introduction to Data Structures and Algorithm Analysis,
// Third Edition (C++)" by Clifford A. Shaffer.
// Source code Copyright (C) 2007-2011 by Clifford A. Shaffer.

#ifndef LQUEUETEST_H
#define LQUEUETEST_H

#include<stdlib.h>

struct jobstampa {
	int timestamp;
	int dastampare;
	int userid;
	int jobid;
};

// Your basic int type as an object.
class Item {
private:
  jobstampa job;
public:
  Item() { }
  Item(jobstampa j) { job = j; }
  // The following is for those times when we actually
  //   need to get a value, rather than compare objects.
  jobstampa key() const { return job; }
  void setdastampare(int pagine) { job.dastampare=pagine; }
  // Overload = to support Item foo = 5 syntax
  //void operator= (jobstampa input) { job = input; }
};

// Let us print out Items easily
ostream& operator<<(ostream& s, const Item& i)
  { return s << "(" << i.key().jobid << " " << i.key().userid << " " << i.key().timestamp << " " << i.key().dastampare << ")"; }



// Assert: If "val" is false, print a message and terminate
// the program
void Assert(bool val, string s) {
  if (!val) { // Assertion failed -- close the program
    cout << "Assertion Failed: " << s << endl;
    exit(-1);
  }
}



#endif

