#include <stdio.h>
#include <stdlib.h>

struct Node *danglingPointers[50] = {};
int counter = 0;

struct Node
{
    int data;
    struct Node *next;
};

struct Node *createNode(int data)
{
    struct Node *tmp = (struct Node *)malloc(sizeof(struct Node));
    tmp->data = data;
    tmp->next = NULL;
    return tmp;
}

struct Node *addNode(struct Node *head, int data)
{
    if (head == NULL)
        return createNode(data);

    struct Node *tmp = head;
    while (tmp->next != NULL)
        tmp = tmp->next;
    tmp->next = createNode(data);
    return head;
}

struct Node *dltNode(struct Node *head, int data)
{
    if (head == NULL)
        return NULL;

    if (head->data == data)
    {
        struct Node *tmp = head->next;
        free(head); // Here head becomes a dangling pointer
        danglingPointers[counter++] = head;
        return tmp;
    }

    struct Node *tmp = head;
    while (tmp->next != NULL && tmp->next->data != data)
        tmp = tmp->next;

    if (tmp->next == NULL)
        return head;

    struct Node *tmp2 = tmp->next->next;
    free(tmp->next); // tmp->next becomes a dangling pointer
    danglingPointers[counter++] = tmp->next;
    tmp->next = tmp2;
    return head;
}

void printList(struct Node *head)
{
    while (head != NULL)
    {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main()
{
    struct Node *head = createNode(1);
    for (int i = 0; i < 10; i++)
        head = addNode(head, i + 2);
    printList(head);

    head = dltNode(head, 1);
    head = dltNode(head, 2);
    head = dltNode(head, 3);

    printf("Dangling Pointers are: \n");
    for (int i = 0; i < counter; i++)
    {
        printf("%p\n", danglingPointers[i]);
    }

    printList(head);

    return 0;
}