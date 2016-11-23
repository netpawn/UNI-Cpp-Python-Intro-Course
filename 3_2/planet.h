#ifndef PLANET_H
#define PLANET_H

class Planet {
public:
    Planet(float r0, float w0);
    void move();
    float get_x();
    float get_y();

    static const int V = 1;

private:
    float r;
    float w; float v;
};

#endif // PLANET_H
