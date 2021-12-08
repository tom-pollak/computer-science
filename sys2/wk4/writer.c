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
    char * mypipe = "/tmp/mypipe"; 
    mkfifo(mypipe, 0666);  //created a named pipe
    char wmsg[SIZE], rmsg[SIZE]; 

    while(1){ 
        // Open FIFO for write only 
        fd = open(mypipe, O_WRONLY); 
  
        // Take an input arr2ing from user. 
        // 80 is maximum length 
   
        fgets(wmsg, SIZE, stdin);  //gets the input message  from the user from the terminal
  
        // Write the input message on FIFO 
        // and close it 
        write(fd, wmsg, strlen(wmsg)+1); 
        close(fd); 
  
        // Open FIFO for Read only 
        fd = open(mypipe, O_RDONLY); 
  
        // Read from FIFO 
        read(fd, rmsg, sizeof(rmsg)); 
  
        // Print the read message 
        printf("User2: %s\n", rmsg); 
        close(fd); 
    } 
    return 0; 
} 
