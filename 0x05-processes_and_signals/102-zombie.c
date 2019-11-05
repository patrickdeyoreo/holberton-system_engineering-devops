#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define STACKSIZE 8
#define N_ZOMBIES 5

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	pid_t zpid = 0;
	int zcount = 0;

	while (zcount++ < N_ZOMBIES)
	{
		zpid = fork();
		if (zpid)
			printf("Zombie process created, PID: %d\n", zpid);
		else
			return (0);
	}
	return (infinite_while());
}
