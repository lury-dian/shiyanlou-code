#include<stdio.h>
int main()
{
    float r,pi;
    int hight;
    hight =3;
    pi = 3.1415926;
    float area,volume;
    printf("Please input circle radius:\n");
    scanf("%f",&r);
    area = pi*r*r;
    volume = area*hight;
    printf("Cylinder buttom circle area is %.2f, Cylinder volume is %.2f\n",area,volume);

    return 0;
}
