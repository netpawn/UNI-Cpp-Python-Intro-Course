//Due colleghi intendono fissare una riunione, pertanto devono identificare dei giorni nei quali sono 
//entrambi liberi da impegni. A tale scopo, si realizzi un programma che permetta a ciascuno di 
//immettere i propri giorni di disponibilità da tastiera, e che identifichi tutti i giorni nei quali entrambi sono liberi. Il programma deve chiedere i giorni di disponibilità ad entrambi i colleghi in successione (ciascuna persona può inserire un numero arbitrario di giorni di disponibilità, utilizzare il valore 0 per indicare la fine della sequenza dei giorni in cui ciascuna persona è libera da impegni). 
//Si consideri che la riunione sia nel mese corrente, quindi non interessa acquisire mese e anno,  ma solo i giorni. Si memorizzi la disponibilità di ciascuna persona in un array di interi positivi di 31 elementi in cui il valore 1 rappresenta un giorno disponibile e un valore 0 rappresenta un giorno impegnato.
//E’ necessario verificare che i giorni siano numeri interi compresi tra 1 e 31. Il programma deve alla fine visualizzare tutti i giorni in cui entrambe le persone sono libere da impegni.


#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
	int C1[31], C2[31]; // comunque non può avere liberi più di 31 giorni 
	int giorno;
	//inizializza i due vettori di disponibilità a 0
	for (int i = 0; i<31; i++)
	{
		C1[i] = 0;
		C2[i] = 0;
	}
	cout << "Giorni liberi del collega 1" << endl;
	// leggo i giorni liberi del collega 1 da mettere in C1 
	do
	{
		cout << "Inserisci il giorno libero (1-31) o zero per terminare: " << endl;
		cin >> giorno;
		if (giorno>0 && giorno<=31)	
			C1[giorno-1]=1;
	} while (giorno != 0);
		
	
	cout << "Giorni liberi del collega 2"<< endl;
	// leggo i giorni liberi del collega 2 da mettere in C2 
	do
	{
		cout << "Inserisci il giorno libero (1-31) o zero per terminare: " << endl;
		cin >> giorno;
		if (giorno>0 && giorno <= 31)
			C2[giorno-1] = 1;
	} while (giorno != 0);

	// verifico giorni disponibili ad entrambi
	for (int i = 0; i<31; i++)
	{
		if ((C1[i] == 1) && (C2[i] == 1))
			cout << endl << "Il giorno " << i+1 << " e' libero per entrambi" << endl;
	}
	return 0;
}