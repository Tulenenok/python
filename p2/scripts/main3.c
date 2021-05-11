#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <sys/time.h>

#define N_MAX 20000


int input(int *pa, int *pb)
{
    for (int *i = pa; i < pb; i++)
        scanf("%d", i);
    return EXIT_SUCCESS;
}

int process_3(int *pa, int *pb)
{
    pb--;

    int max = *pa + *pb;
    while (pa <= pb)
    {
        int new_sum = *pa + *pb;
        if (new_sum > max)
            max = new_sum;
        pa++;
        pb--;
    }
    return max;
}

int main(void)
{
    struct timeval tv_start, tv_stop;
    int64_t elapsed_time;

    size_t n;
    int arr[N_MAX];
    int *pa = arr, *pb = arr;

    scanf("%zu", &n);
    pb += n;

    input(pa, pb);

    gettimeofday(&tv_start, NULL);
    process_3(pa, pb);
    gettimeofday(&tv_stop, NULL);

    elapsed_time = (tv_stop.tv_sec - tv_start.tv_sec) * 1000000L +
                   (tv_stop.tv_usec - tv_start.tv_usec);
    printf("%" PRId64 " \n", elapsed_time);
    return EXIT_SUCCESS;
}
