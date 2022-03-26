#include <stdio.h>

int fun(int b)
{
    printf("Auto is called\n");
    return b * b;
}

int funReg(int c)
{
    printf("Register is called\n");
    return c + c;
}

int main()
{
    // auto storage class
    int auto b;
    printf("%d\n", b);
    printf("%d\n", fun(b));

    // register storage class
    int register c;
    printf("%d\n", c);
    printf("%d\n", funReg(c));
}