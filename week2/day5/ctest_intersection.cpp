#include <iostream>
#include <float.h>
using namespace std;

#define pdd pair<double, double>

void displayPoint(double X, double Y)
{
    printf("%f %f", X, Y);
}

void lineLineIntersection(int A1, int B1, int C1, int A2, int B2, int C2)
{
    double a1 = A1;
    double b1 = B1;
    double c1 = C1;

    double a2 = A2;
    double b2 = B2;
    double c2 = C2;

    /*double determinant = a1*b2 - a2*b1;
    printf("Det %f\n", determinant);*/

    double x = (b1*c2 - b2*c1)/(a1*b2 - a2*b1);
    double y = (a2*c1 - a1*c2)/(a1*b2 - a2*b1);

    displayPoint(x, y);
}

int main(){
    int A1, B1, C1, A2, B2, C2;

    cin >> A1 >> B1 >> C1 >> A2 >> B2 >> C2;

    lineLineIntersection(A1, B1, C1, A2, B2, C2);

    return 0;
}
