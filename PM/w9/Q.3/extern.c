#include <stdio.h>

void factorialFun(int a)
{
    int ans = 1;
    for (int i = 1; i <= a; i++)
        ans *= i;
    printf("Factorial of the number %d is : %d\n", a, ans);
}