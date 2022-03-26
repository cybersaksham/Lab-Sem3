#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    int refCount;
    struct node *left;
    struct node *right;
};

void printCurrentLevel(struct node *root, int level);
int height(struct node *node);

void printLevelOrder(struct node *root)
{
    int h = height(root);
    int i;
    for (i = 1; i <= h; i++)
    {
        printf("Level %d : ", i);
        printCurrentLevel(root, i);
        printf("\n");
    }
}

void printCurrentLevel(struct node *root, int level)
{
    if (root == NULL || root->refCount == 0)
        return;
    if (level == 1 && root->refCount == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printCurrentLevel(root->left, level - 1);
        printCurrentLevel(root->right, level - 1);
    }
}

int height(struct node *node)
{
    if (node == NULL)
        return 0;
    else
    {

        int lheight = height(node->left);
        int rheight = height(node->right);

        if (lheight > rheight)
            return (lheight + 1);
        else
            return (rheight + 1);
    }
}

struct node *newNode(int data, int ref)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));

    node->data = data;
    node->refCount = ref;
    node->left = NULL;
    node->right = NULL;
    return (node);
}

void deleteTree(struct node *node)
{
    if (node == NULL)
        return;

    deleteTree(node->left);
    deleteTree(node->right);

    printf("\nDeleting node: %d", node->data);
    free(node);
}

void delPostorder(struct node *node)
{
    if (node == NULL)
        return;

    if (node->left)
        delPostorder(node->left);
    if (node->right)
        delPostorder(node->right);

    if (node->refCount == 0)
        deleteTree(node);
}

int main()
{

    struct node *head = newNode(1, 1);
    head->left = newNode(2, 1);
    head->right = newNode(3, 1);
    head->right->left = newNode(4, 1);
    head->left->left = newNode(5, 1);
    head->left->right = newNode(6, 1);
    head->right->right = newNode(7, 1);
    head->right->right->right = newNode(8, 1);
    head->right->right->left = newNode(9, 1);
    head->right->left->right = newNode(10, 1);
    head->right->left->left = newNode(11, 1);

    printLevelOrder(head);

    head->right->right->refCount = 0;
    head->left->right->refCount = 0;
    head->left->left->refCount = 0;

    delPostorder(head);

    printf("\n");

    printLevelOrder(head);

    return 0;
}