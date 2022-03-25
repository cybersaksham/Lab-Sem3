// Static Scoping - 1 0
// Dynamic Scoping - 1 1

#include <stdio.h>

int i = 0;

int g()
{
    i++;
    printf("%d\n", i);
}

int f()
{
    int i = 0;
    g();
    printf("%d\n", i);
}

int main()
{
    f();
    return 0;
}