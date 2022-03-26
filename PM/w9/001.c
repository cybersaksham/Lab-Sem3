#include <stdio.h>

int stackDynamic()
{
    int k = 0;
    return ++k;
}

int staticSegment()
{
    static int k = 0;
    return ++k;
}

int main()
{
    for (int i = 0; i < 10; i++)
    {
        printf("Stack Dyanmic %d\n", stackDynamic());
        printf("Static        %d\n", staticSegment());
    }

    return 0;
}
