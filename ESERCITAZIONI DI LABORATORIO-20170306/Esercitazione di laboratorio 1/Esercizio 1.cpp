//Scrivere un programma che crei due vettori di numeri interi a e b di lunghezza N. 
//Il vettore b va inizializzato con la sequenza di numeri 0, 3, 6, 9, 12, 15… 
//Il programma deve calcolare la  somma incrociata degli elementi: a[0]+b[N-1], a[1]+b[N-2], …, a[N-1]+b[0] 
//e memorizzarla nel vettore c. Il programma deve inoltre creare un vettore d della stessa lunghezza 
//con valore 1 se a[i] > b[i], 0 se a[i]=b[i] e -1  altrimenti. 
//Si visualizzino i contenuti di a, b, c, d. 

#include <iostream>
#include <cstdlib>
#include <cmath>

const int N = 6; 

using namespace std;

int main() {

	int a[N] = {0, 12, 18, 66, 78, 95};
	int b[N] = {0, -3, 6, -9, 12, -15};
	int c[N];
	int d[N];
	
	cout << "Vettore A = ";
	for (int i = 0; i < N; i++) {
		cout << a[i] << ",";
	}
	cout << endl;
	cout << "Vettore B = ";
	for (int i = 0; i < N; i++) {
		cout << b[i] << ",";
	}
	cout << endl;
	cout << "Vettore C = ";
	for(int i = 0; i < N; i++) {
		c[i] = (a[i] + b[N -( i + 1)]);
			cout << c[i] << ",";
	}
	cout << endl;
	cout << "Vettore D = ";
	for(int i = 0; i < N; i++) {
		if (a[i]>b[i]) {
			d[i] = 1;
		}
		else if (a[i] == b[i]) {
			d[i] = 0;
		}
		else if (a[i]<b[i]) {
			d[i] = -1;
		}
		cout << d[i] << ",";
	}
	cout << endl;



}

