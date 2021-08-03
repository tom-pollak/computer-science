#include <stdio.h>
int x;

int main (int argc, char *argv[])
{
    /* x = 3 * 4 << 2; printf("%d", x); */
    printf("%d\n", ~(4 - 5));
    printf("%d\n", 4 && 3);
    printf("%d\n", 4 & 3);
    printf("%d\n", 9 || 12 >> 32);
    printf("%d\n", 12 >> 32);
    return 0;
}
