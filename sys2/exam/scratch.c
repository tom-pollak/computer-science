#include <stdio.h>
#include <unistd.h>

int main() {
  int i = 10;
  pid_t return_id;
  return_id = fork();
  i = i + 5;
  printf("Return id is %d \n ", return_id);
  printf("i is %d ", i);
  return 0;
}
