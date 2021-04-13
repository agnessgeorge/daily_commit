#include <stdio.h>

void triArea(int base, int height)
{
    int area = (base * height) / 2;
    printf("%d\n",area);
}

int main()
{
    triArea(3, 2);
    triArea(7, 4);
    triArea(10, 10);

}
