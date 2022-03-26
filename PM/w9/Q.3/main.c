#include <stdio.h>
#include "extern.c"

extern void factorialFun(int c);
static int c = 0;

int main()
{
    printf("Enter a number :");
    scanf("%d", &c);
    factorialFun(c);

    return 0;
}
