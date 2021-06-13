#include <stdio.h>
#include <string.h>

int main() {
    unsigned char sentence1[25] = "It's a nice day today. ";
    unsigned char sentence2[25] = "It really is.";
    unsigned char firstbit[25];

    strncpy(firstbit, sentence1, 25);
    strncat(firstbit, sentence2, 25);

    printf("%s\n", firstbit);

}
