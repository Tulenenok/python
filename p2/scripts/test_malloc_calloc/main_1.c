#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <sys/time.h>

int main(void)
{
    struct timeval tv_start, tv_stop;
    int64_t elapsed_time;

    size_t n;
	int *a;

    scanf("%zu", &n);

    gettimeofday(&tv_start, NULL);
    a = malloc(n * sizeof(int));
    gettimeofday(&tv_stop, NULL);

    elapsed_time = (tv_stop.tv_sec - tv_start.tv_sec) * 1000000L +
            (tv_stop.tv_usec - tv_start.tv_usec);
    printf("%" PRId64 " \n", elapsed_time);
	
	if(!a)
		return EXIT_FAILURE;
	free(a);
    return EXIT_SUCCESS;
}