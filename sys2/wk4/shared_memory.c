#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <unistd.h>  

#define handle_error(msg) \
           do { perror(msg); exit(EXIT_FAILURE); } while (0)


int main()
{
    pid_t child_return;    
    const int SIZE = 4096; //get a block for 4096;
    const char *name = "Shared";
    const char *message_0 = "Hello ";
    const char *message_1 = "I am a shared message";

    int shm_fd;
    void *ptr, *ptr1;
    shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666); //create a file discriptor for shared object name
    ftruncate(shm_fd, SIZE); 

    ptr = (char*) mmap(0, SIZE, PROT_WRITE|PROT_READ, MAP_SHARED, shm_fd, 0); 
    if (ptr == MAP_FAILED) handle_error("mmap");

    sprintf(ptr, "%s", message_0); 
    ptr += strlen(message_0);
    sprintf(ptr, "%s", message_1);
    ptr += strlen(message_1);

    child_return = fork();
    if (child_return  == 0) {
        printf("child process %d\n", getpid());
        //shm_fd = shm_open(name, O_RDONLY, 0666);
        ptr1 = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);  //Why do we need this mapping again?
        if (ptr1 == MAP_FAILED) handle_error("mmap");
        printf("%s\n", (char*)ptr1);
        munmap(ptr1, SIZE);
        shm_unlink(name);
    }
    munmap(ptr, SIZE);

    exit(0);
}
