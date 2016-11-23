#include <iostream>
#include "planet.h"


using namespace std;

int main()
{
    int a = 1;
    float r0; float w0;
    cout << "hello wonderful people, raggio?" << endl;
    cin >> r0;
    cout << "Angolino magico?" << endl;
    cin >> w0;

    Planet planet1{r0, w0};

    while(a = 1){
            planet1.move();
            cout << "X : " << planet1.get_x() << endl;
            cout << "Y : " << planet1.get_y() << endl;
    }

}


