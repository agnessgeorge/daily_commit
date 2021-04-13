#include <stdio.h>

void howManySeconds(int hours)
{
    int seconds = hours * 60 * 60;
    printf("%d\n",seconds);
}

int main()
{
    howManySeconds(2);
    howManySeconds(10);
    howManySeconds(24);

}
