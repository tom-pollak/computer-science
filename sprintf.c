#include <stdio.h>
#include <string.h>

int main () {
    void *ptr;
    const char *message = "Hello World!";
    sprintf(ptr, "%s", message);
    ptr += strlen(message);
    printf("%s", (char*) &ptr);

    return(0);
}
