// Pass by value
// 2 10 20 30 3 33 10 20 0 2 10 20 0

// Pass by result
// 2 10 20 30 1 3 10 20 0 1 10 3 0

// Pass by value-result
// 2 10 20 30 3 33 10 20 0 3 error

// Pass by name
// 2 10 20 30 3 0 10 20 0 3 10 20 0

#include <stdio.h>

int a[] = {10, 20, 30};
int i = 2;

void fun(int j, int k)
{
    int i = 0;
    j = j + 1;
    k = k + 3;
    a[2] = 0;
    printf("%d\n", j);
    printf("%d\n", k);
    printf("%d\n", a[0]);
    printf("%d\n", a[1]);
    printf("%d\n", a[2]);
}

void fun2(int *j, int *k)
{
    int i = 0;
    *j = *j + 1;
    *k = *k + 3;
    a[2] = 0;
    printf("%d\n", *j);
    printf("%d\n", *k);
    printf("%d\n", a[0]);
    printf("%d\n", a[1]);
    printf("%d\n", a[2]);
}

void main()
{
    // By Value
    // printf("%d\n", i);
    // printf("%d\n", a[0]);
    // printf("%d\n", a[1]);
    // printf("%d\n", a[2]);
    // fun(i, a[i]);
    // printf("%d\n", i);
    // printf("%d\n", a[0]);
    // printf("%d\n", a[1]);
    // printf("%d\n", a[2]);

    // By Reference
    printf("%d\n", i);
    printf("%d\n", a[0]);
    printf("%d\n", a[1]);
    printf("%d\n", a[2]);
    fun2(&i, &a[i]);
    printf("%d\n", i);
    printf("%d\n", a[0]);
    printf("%d\n", a[1]);
    printf("%d\n", a[2]);
}