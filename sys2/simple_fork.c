/* This is week 3 and 4 SYS2 hands-on task*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
pid_t pid_main;
pid_t pid_child, return_pid, terminated_child_pid;

pid_main = getpid();
return_pid = fork(); //first child created
if (return_pid == -1) {      /* fork() failed */
    perror("fork");
    exit(1);
} else if (return_pid == 1) {
    printf("Parent process = 1");
}
printf("The main process %d \n",pid_main);
printf("The parent process of the current process is %d \n",getppid());
printf("The child return pid %d \n", return_pid);
printf("The current process %d \n",getpid());

if(return_pid == 0)
{
    printf("I am the child process\n\n");
    exit(0);
}
else
{
    /* printf("I am the main parent process"); */
    /* sleep(10); */
    terminated_child_pid = wait(NULL);
    printf("The terminated child %d \n", terminated_child_pid); 

}}
