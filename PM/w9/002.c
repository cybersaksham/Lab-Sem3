#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *create(int val)
{
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = val;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

int main()
{
    struct node *head = create(1); // explicitly declare

    struct node head2; // implicitly
    head2.data = 5;
    printf("%d\n", head->data);
    printf("%d\n", head2.data);
}