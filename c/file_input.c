#include <stdio.h>

struct coord {
    float x;
    float y;
};

int main (int argc, char *argv[])
{
    FILE *f, *b, b_r;

    f = fopen("coords.txt", "rt");
    for (int i = 0; i < 5; i++) {
        struct coord c;
        fscanf(f, "%f %f", &c.x, &c.y);
        b = fopen("coords", "wb");
        fwrite(&c, 1, 1, b);
        fclose(b);
        b_r = *fopen("coords", "rb");
        fread(&c, 1, 1, &b_r);
        printf("%f, %f\n", c.x, c.y);
        fclose(&b_r);
    }
    fclose(f);
    return 0;
}
