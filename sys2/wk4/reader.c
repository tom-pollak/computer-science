#include <stdio.h> 
#include <string.h> 
#include <fcntl.h> 
#include <sys/stat.h> 
#include <sys/types.h> 
#include <unistd.h> 
#define SIZE 80 
int main() 
{ 
    int fd; 
  
    // FIFO file path 
    char * mypipe = "/tmp/mypipe"; 
  
    // Creating the named file(FIFO) 
    // mkfifo(<pathname>,<permission>) 
    mkfifo(mypipe, 0666); 
  
    char wmsg[SIZE], rmsg[SIZE]; 
    while (1) 
    { 
        // First open in read only and read 
        fd = open(mypipe,O_RDONLY); 
        read(fd, rmsg, SIZE); 

        // Print the read string and close 
        printf("User1: %s\n", rmsg); 
        close(fd); 
  
        // Now open in write mode and write 
        // string taken from user. 
        fd = open(mypipe,O_WRONLY); 
        fgets(wmsg, SIZE, stdin); 
        write(fd, wmsg, strlen(wmsg)+1); 
        close(fd); 
    } 
    return 0; 
} 
