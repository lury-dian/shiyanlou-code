#include<stdio.h>
int main()
{
    char c;
    printf("Please input an uppercase letter:\n");
    c=getchar();
    putchar(c+32);
    return 0;
}
