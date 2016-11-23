#include<iostream>
#include<cmath>

using namespace std;

float heron(float a, float b, float c){
    float s;
    float area;

    s = (a+b+c)/2;
    area = sqrt(s*(s-a)*(s-b)*(s-c));
    return area;
}

int main(){
    float a,b,c;

    cout<<"Dammi la A =";
    cin>>a;
    cout<<"Dammi la B =";
    cin>>b;
    cout<<"Dammi la C =";
    cin>>c;
    cout << "L'area del triangolo e'= " << heron(a, b, c) << endl;

    return 0;
}
