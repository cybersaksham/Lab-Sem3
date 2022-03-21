#include <stdio.h>
#include <stdlib.h>

int allocationCounter = 0;
int deallocationCounter = 0;

int *allocateMemory(int n)
{
    int *arr = (int *)malloc(sizeof(int) * n);
    allocationCounter += n;
    return arr;
}

void deallocateMemory(int *arr, int n)
{
    free(arr);
    deallocationCounter += n;
}

int main()
{
    // Allocating Memory
    int *arr1 = allocateMemory(5);
    int *arr2 = allocateMemory(4);

    // De-allocating memory
    deallocateMemory(arr1, 5);

    printf("Allocated memory = %ld bytes\n", allocationCounter * sizeof(int));
    printf("De-allocated memory = %ld bytes\n", deallocationCounter * sizeof(int));

    // Memory Leak
    if (allocationCounter > deallocationCounter)
    {
        printf("Memory leak = %ld bytes\n", sizeof(int) * (allocationCounter - deallocationCounter));
    }

    return 0;
}