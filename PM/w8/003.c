#include <stdio.h>
#include <stdlib.h>

struct Node
{
    // struct Node(int value)
    // {
    //     this.value = value;
    //     this.next = nullptr;
    // }
    int value;
    struct Node *next;
};

struct Node *createNode(int data)
{
    struct Node *tmp = (struct Node *)malloc(sizeof(struct Node));
    tmp->value = data;
    tmp->next = NULL;
}

struct Node *removeNode(int value, struct Node *head)
{
    struct Node *newHead = head;
    if (head->value == value)
    {
        newHead = head->next; // Here head is creating memory leak
        // To prevent memory leak we have to delete head and return newHead
        free(head);
        return newHead;
    }

    while (head->next != NULL && head->next->value != value)
        head = head->next;
    if (head->next)
    {
        struct Node *temp = head->next;
        head->next = head->next->next;
        // Memory occupied by temp pointer is not freed so it is causing memory leak
        free(temp);
    }
    return newHead;
}

int main()
{
    struct Node *head = createNode(5);
    head->next = createNode(6);
    head->next->next = createNode(7);

    removeNode(7, head);
    removeNode(6, head);

    return 0;
}