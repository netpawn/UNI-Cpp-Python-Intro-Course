//Definire una struct “tipolibro” con gli attributi: titolo (string), autore (string), anno di edizione (int) e prezzo (int). 
//Scrivere un programma che legga da tastiera i dati di N (costante definita nel programma) libri memorizzandoli in un array di strutture tipolibro. 
//Il prezzo di ciascun libro deve essere generato in modo casuale all'interno del programma (per generare un numero casuale intero compreso tra 0 e N si utilizzi la funzione rand()%N).
//Il programma deve quindi calcolare il prezzo medio dei libri inseriti, determinare il libro con prezzo maggiore 
//e il libro con l'anno di edizione piu' vecchio. 
//Il programma deve anche salvare su un file di testo le informazioni di ciascun libro (ogni riga deve contenere titolo, autore, anno di edizione e prezzo di un libro).


#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#include <cstdlib>
#include <ctime>
const int N=4;

struct tipolibro {
	string titolo;
    string autore;
	int anno;
	float prezzo;
};

int main() {
	    tipolibro libri[N];
		int i;
		ofstream myfile("libri.txt");
		float prezzomedio = 0.0, prezzomassimo = 0.0;
		int idprezzomassimo =-1, idtitolovecchio=-1, minanno =1000000;

		srand(time(NULL));
		for (i = 0; i<N; i++)
		{
		 cout << "Inserire i dati del libro " << i << " (titolo autore anno)" << endl;
		 cin >> libri[i].titolo >> libri[i].autore >> libri[i].anno;
		 libri[i].prezzo = rand() % 201; // rand()%N restituisce un numero casuale compreso tra 0 e N-1
		 cout << "prezzo generato casualmente=" << libri[i].prezzo << endl;
		 myfile << libri[i].titolo << " " << libri[i].autore << " " << libri[i].anno << " " << libri[i].prezzo << endl;
	
		 // eseguo i calcoli in questo ciclo 
		 prezzomedio += libri[i].prezzo;
		 if (libri[i].prezzo>prezzomassimo)
			{
				prezzomassimo = libri[i].prezzo;
				idprezzomassimo = i;
			}
		 if (libri[i].anno<minanno)
			{
			    minanno = libri[i].anno;
				idtitolovecchio = i;
			}
		 }
		 cout << "Il prezzo medio dei libri e' " << prezzomedio / N << endl;
		 cout << "Il libro con il prezzo maggiore e' " << libri[idprezzomassimo].titolo << endl;
		 cout << "Il libro piu' vecchio e' " << libri[idtitolovecchio].titolo << endl;
		return 0;
}