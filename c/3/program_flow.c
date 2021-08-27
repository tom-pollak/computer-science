#include <stdio.h>

int addmult(int x, int y, int z);

int addmult(int x, int y, int z) {
    return (x + y) * z;
}

int main() {
    int x = 0;
    int y = 0;

    y = addmult(3, 4, 5);
    printf("Addmult(3, 4, 5) = %d\n", y);

    printf("These numbers are less than 10");
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", i);
    }

    
    x = 2;
    printf("These are numbers less than 100");
    while (x < 100) {
        printf("%d\n", x);
        x = x * x;
    }

    printf("This loop runs until it gets to 49, then it prints and stops\n");

    x = 30;
    do {
        if (x > 49)
        {
            printf("%d", x);
            break;
        }
        x++;
    } while (1);

    switch (x - y)
    {
    case 0:
        printf("True");
        break;
    default:
        printf("False");
    }
}

