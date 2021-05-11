#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <sys/time.h>

#define N_MAX 20000


int input(size_t n, int arr[])
{
    for (size_t i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    return EXIT_SUCCESS;
}

int process_2(size_t n, int arr[])
{
    size_t i = 0;
    int max = *(arr + i) + *(arr + n - i - 1);
    while (arr + i <= arr + n - i - 1)
    {
        int new_sum = *(arr + i) + *(arr + n - i - 1);
        if (new_sum > max)
            max = new_sum;
        i++;
    }
    return max;
}

int main(void)
{
    struct timeval tv_start, tv_stop;
    int64_t elapsed_time;

    size_t n;
    int arr[N_MAX];

    scanf("%zu", &n);
    input(n, arr);

    gettimeofday(&tv_start, NULL);
    process_2(n, arr);
    gettimeofday(&tv_stop, NULL);

    elapsed_time = (tv_stop.tv_sec - tv_start.tv_sec) * 1000000L +
            (tv_stop.tv_usec - tv_start.tv_usec);
    printf("%" PRId64 " \n", elapsed_time);
    return EXIT_SUCCESS;
}