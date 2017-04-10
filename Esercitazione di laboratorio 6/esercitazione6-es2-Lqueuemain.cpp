// esercizio coda di stampa

#include <iostream>
#include <cstdlib>
#include <string>
#include <time.h>  // Used by timing functions

using namespace std;

const int defaultSize = 10; // Default size

#include "lqueue.h"

#include "esercitazione6-es2-LQueueTest.h"

// Main routine 
int main(int argc, char** argv) {
  srand(time(NULL));
  LQueue<Item> Qstampa;
  Item temp;
  jobstampa js;
  int Job = 1;
  int stampe_rimanenti_cur_job; // numero di pagine rimanenti da stampare per il job corrente
  bool in_stampa = 0; // flag per sapere se sto stampando qualcosa
  int tot_pagine_stampate = 0;

  for (int sec=1; sec<=8*60*60; sec++) // ciclo di simulazione per 8*60*60 secondi
  { 
    if (rand()%180==0) // se si verifica questa condizione significa che arriva un nuovo job di stampa
	{
		js.userid= rand() % 10 + 1; // utente che ha stampato
		js.dastampare = rand() % 20 + 1; // numero di pagine da stampare per questo job
		js.jobid = Job; // Job id
		js.timestamp = sec; // timestamp attuale
		temp = js;
		Qstampa.enqueue(temp); // inserisco il nuovo job in coda
		cout << "new job: " << temp << endl;
		cout << "timestamp:" << sec << " " << "numero lavori in coda:" << Qstampa.length() << endl;
		Job++; // incremento il valore del job
	}
	if (Qstampa.length()>=1) // se c'e' almeno un job in coda
	{
	 if (!in_stampa) // se non stavo già stampando allora devo iniziare a stampare un nuovo job
	  {
		 in_stampa = 1; // inizio a stampare
		 Item curjob = Qstampa.frontValue(); 
		 stampe_rimanenti_cur_job = curjob.key().dastampare; // leggo quante pagine devo stampare per il job che inizia
	  }
	 stampe_rimanenti_cur_job--; // simulo la stampa di una pagina
	 tot_pagine_stampate++;
	 if (stampe_rimanenti_cur_job==0)  //se il numero di pagine del job corrente si azzera
		{
			temp=Qstampa.dequeue(); // elimino il job dalla coda
			cout << "job removed: " << temp << endl;
			cout << "timestamp:" << sec << " " << "numero lavori in coda:" << Qstampa.length() << endl;
			if (Qstampa.length() == 0) // se non c'e' nessun altro job in attesa
			{
			  in_stampa = 0; // fermo la stampa
			}
			else // se c'e' almeno un altro job in coda non fermo la stampa
			{
			  Item curjob = Qstampa.frontValue();
			  stampe_rimanenti_cur_job = curjob.key().dastampare; // leggo il numero di pagine da stampare del job successivo che adesso è in cima alla coda
			}
		}
	}
  }
 
  cout << "tot_pagine_stampate=" << tot_pagine_stampate << endl;
 
  cout << "That is all.\n\n";
}