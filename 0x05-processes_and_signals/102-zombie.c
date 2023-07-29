#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 *infinite_while - run an infinite loop
 *Return: 0
 */
int infinite_while(void)
{
        while (1)
        {
                sleep(1);
        }
        return (0);
}

/**
 *main - Create zombie process
 *Return: Success (0)
 */
int  main(void)
{
        pid_t pid;
        int count = 0;

        while (count < 5)
        {
                pid = fork();

                if (pid > 0)
                {
                        printf("Zombie process created, PID: %d\n", pid);
                        count++;
                }
                else
                        exit(0);
        }
        infinite_while();
        return (EXIT_SUCCESS);
}
