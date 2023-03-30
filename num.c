#include <stdio.h>
#include <time.h>

int main()
{
    clock_t start_time, end_time;
    double time_used;

    start_time = clock();

    for (int i = 0; i < 100000; i++)
    {
        printf("%d", i);
    }

    end_time = clock();

    time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("\n\nTiempo de ejecución: %f segundos", time_used);

    return 0;
}
