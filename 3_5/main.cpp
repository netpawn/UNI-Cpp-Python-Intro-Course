#include "widget.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    w.show();

        int a = 1;
        float r0; float w0;

        Planet planet1{5, 1.97};
        Planet planet2{50, 1.97};

        while(a = 1){
                planet1.move();
                planet2.move();
                cout << "X : " << planet1.get_x() << endl;
                cout << "Y : " << planet1.get_y() << endl;
        }
    return a.exec();
}
