#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> lista = {};
    vector<int> sup_lista = {};
    vector<int> inf_lista = {};

    int val, tot = 0, count = 0;
    cout <<"Valore? 0 Per terminare "; cin >> val;
    while (val !=0) {
        tot += val; ++count;
        lista.push_back(val);
        cout <<"Valore ? 0 Per terminare "; cin >> val;
    }
    float media = tot/count;
    cout << "La media e': " << media << endl;
    cout << "la lista contiene " << lista.size() << " elementi." << endl;
    for (auto x: lista){
         if (x < media){
             inf_lista.push_back(x);
                }
         else{
             sup_lista.push_back(x);
                }

           }
        cout << "N sotto la media: " << endl;
        for (auto x: inf_lista){

            cout << x << endl;
        }
        cout << "N pari o sopra la media: " << endl;
        for (auto x: sup_lista){

            cout << x << endl;
           }


return 0;
}
