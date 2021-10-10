#include "stdio.h"
#include "stdlib.h"
#include "string.h"

struct s {
  int x;
  int y;
};

int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

void intswap(int *x, int *y) {
  int tmp = *x;
  *x = *y;
  *y = tmp;
}

int main(int argc, char *argv[]) {
  struct s s1;
  s1.x = 5;
  s1.y = 1;
  int x = 72;
  int y = 1;
  intswap(&x, &y);
  printf("%d, %d\n", x, y);
  intswap(&s1.x, &s1.y);
  printf("%d, %d \n", s1.x, s1.y);

  /* char string1[8] = "1234567"; */
  /* intswap(&x, &(int)string1); */
  /* printf("%d, %s\n", x, string1); */

  int *ptr = malloc(5 * sizeof(int));
  ptr[0] = 1;
  ptr[1] = 2;
  ptr[1000] = 100000000;
  printf("%u", &ptr);

  return 0;
}
