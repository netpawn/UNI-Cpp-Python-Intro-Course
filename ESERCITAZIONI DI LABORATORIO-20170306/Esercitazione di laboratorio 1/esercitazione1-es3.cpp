//E’ noto che noto  che esiste una definizione matematica della radice quadrata 
//che si basa sulla seguente sequenza numerica : x_1 = 1, x_(n + 1) = 1/2(x_n + a/x_n) 
//dove a è un numero reale positivo.
//Si può dimostrare che : lim(i→∞)⁡ x_i = √a
//Si scriva un programma in cui si calcola la radice quadrata di tre numeri 
//memorizzati in un array.
//Il ciclo di  calcolo della radice può fermarsi quando la differenza 
//tra sqrt(a) e x_(n + 1) diventa inferiore ad un valore di soglia (es : 0.001).
//Utilizzare la funzione abs() per calcolare la differenza in valore assoluto.


#include <iostream>
using namespace std;
#include <cstdlib>

int main() {
	float xi, xi1;
	float a[3]= {35.0, 84.0, 100.0};
	
	for (int i=0; i<3; i++)
	{
	 xi1 = 1.0;
	 do {
		 xi = xi1;
	     xi1 = 0.5*(xi + a[i]/xi);
	 } while (abs(sqrt(a[i])-xi1)>0.001);
	 cout << "Valore finale di radice di " << a[i] << " :" << xi1 << endl;
	}
	return 0;
}