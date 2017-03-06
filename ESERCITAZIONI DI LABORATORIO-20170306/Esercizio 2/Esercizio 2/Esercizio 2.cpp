#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {

	int a[31], b[31];
	int giornoa = 1;
	int giornob = 1;
	
	for(int i=0;i < 31; i++) {
		a[i] = 0, b[1]= 0;

	}

	cout << "Benvenuto collega A, inserisci i giorni in cui sei libero (0  per terminare)"<< endl;

	while (giornoa != 0 ) {
		if (giornoa >= 1 && giornoa < 31) {
			cin >> giornoa;
			a[giornoa-1] = 1;
			}
	}

    cout << "Benvenuto collega B, inserisci i giorni in cui sei libero (0  per terminare)"<< endl;

	while (giornob != 0 ) {
		if (giornob >= 1 && giornob < 31) {
			cin >> giornob;
			b[giornob-1] = 1;
			}
	}

	cout << "Giorni dove sono liberi entrambi i colleghi A e B "<< endl;
	for(int i = 0; i < 31; i++) {
		if (a[i] == 1 && b[i] == 1) {
			cout << "Nel giorno " << i+1 << endl;
		}
	}
}