#include<iostream>
#include<cmath>
using namespace std;

float heron(a&, b&, c&){
    float a, b, c;
    float s = (a + b + c)/2;
    float area = sqrt(s * (s -a) * (s - b) * (s- c));
    return area;
}

main(){
    float a, b, c;
    float s = (a + b + c)/2;
    cout << "Dammi i valori di a, b e c " << endl;
    cin >> a >> b >> c;
    cout << heron(a, b, c);
}
