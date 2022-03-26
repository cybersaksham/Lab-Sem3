#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str; // str is dangling pointer here because it is pointing to garbage memory
    // To make it free from dangling pointer we can point it to NULL;
    str = NULL;
    {
        char a = 'A';
        str = &a;
        free(str);
    }
    printf("%c", *str);
}