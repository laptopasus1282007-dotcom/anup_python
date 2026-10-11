#include <stdio.h>

int main()
{
    int memsize, n, remaining, process[20], i;

    printf("Enter total memory size: ");
    scanf("%d", &memsize);

    remaining = memsize;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("\nprocess\tsize\tstatus\n");

    for (i = 0; i < n; i++)
    {
        printf("Enter size of process %d: ", i + 1);
        scanf("%d", &process[i]);

        if (process[i] <= remaining)
        {
            printf("p%d\t%d\tAllocated\n", i + 1, process[i]);
            remaining -= process[i];
        }
        else
        {
            printf("p%d\t%d\tNot Allocated\n", i + 1, process[i]);
        }
    }

    printf("\nRemaining Memory=%d", remaining);
    return 0;
}