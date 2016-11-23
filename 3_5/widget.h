#ifndef WIDGET_H
#define WIDGET_H

#include <QtWidgets>
#include <vector>
#include "planet.h"

class Widget : public QWidget
{
    Q_OBJECT
private:
    QPixmap screen{600, 400}; QPainter painter{&screen};
    std::vector<Planet*> planets = {new Planet(5, 1.97), new Planet(50, 1.97)};
    painter.setBrush(QColor{0, 0, 255});
    painter.drawEllipse(QPoint{300, 50}, 20, 20);
public:
    void timerEvent(QTimerEvent *event);
    void paintEvent(QPaintEvent *event);
    void keyPressEvent(QKeyEvent *event);
    Widget();
    ~Widget();
    QLabel label; label.setPixmap(screen); label.show();
};

#endif // WIDGET_H
