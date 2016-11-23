#include "planet.h"
#include <cmath>

Planet::Planet(float r0, float w0)
{
    r = r0; w = w0; v = V;
}
void Planet::move(){
    w += v;
}
float Planet::get_x(){
    return r * cos(w);
}
float Planet::get_y(){
    return r * sin(w);
}
