#include <stdio.h>
#include <string.h>

void swapStrings(char a[], char b[])
{
    char tmp[100];
    strcpy(tmp, a);
    strcpy(a, b);
    strcpy(b, tmp);
}

int main()
{
    char a[100], b[100];
    gets(a);
    gets(b);
    swapStrings(a, b);

    printf("String 1 = ");
    puts(a);
    printf("String 2 = ");
    puts(b);

    return 0;
}