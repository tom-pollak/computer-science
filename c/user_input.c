#include <stdio.h>

int main (int argc, char *argv[])
{
    int int1, int2;
    printf("Enter two integers: ");
    scanf("%d %d", &int1, &int2);
    printf("Difference: %d\n", int1 - int2);
    return 0;
}
