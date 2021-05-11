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

int process_1(size_t n, int arr[])
{
    size_t left = 0;
    size_t right = n - 1;
    int max = arr[left] + arr[right];
    while (left <= right)
    {
        int new_sum = arr[left] + arr[right];
        if (new_sum > max)
            max = new_sum;
        left++;
        right--;
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
    process_1(n, arr);
    gettimeofday(&tv_stop, NULL);

    elapsed_time = (tv_stop.tv_sec - tv_start.tv_sec) * 1000000L +
            (tv_stop.tv_usec - tv_start.tv_usec);
    printf("%" PRId64 " \n", elapsed_time);
    return EXIT_SUCCESS;
}