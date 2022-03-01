#include <iostream>
using namespace std;

class Node
{
	static void printHelp(Node const *root)
	{
		if(root == NULL) return;
		cout << root->data << " ";
		printHelp(root->next);
	}
	
public:
	long data;
	Node *next;
	
	// Constructors
	Node(long data) : data(data), next(NULL) {}
	Node(long data, Node *next) : data(data), next(next) {}
	
	// Inserting Sorted
	static Node *insert(Node *root, long val)
	{
		if(root == NULL)
		{
			Node *newNode = new Node(val);
			return newNode;
		}
		
		if(root->data < val)
		{
			Node *tmp = insert(root->next, val);
			root->next = tmp;
			return root;
		}
		
		Node *newNode = new Node(val, root);
		return newNode;
	}
	
	// Inserting Random
	static pair<Node *, Node*> insertRandom(Node *head, Node *tail, long val)
	{
		if(head == NULL || tail == NULL || head->data == -1)
		{
			Node *newNode = new Node(val);
			pair<Node *, Node *> newPair(newNode, newNode);
			return newPair;
		}
		
		Node *newNode = new Node(val);
		tail->next = newNode;
		pair<Node *, Node *> newPair(head, newNode);
		return newPair;
	}
	
	// Deleting
	static Node *remove(Node *root, long val)
	{
		if(root == NULL) return root;
		if(root->data == val)
		{
			Node *tmp = root->next;
			delete root;
			return tmp;
		}
		root->next = remove(root->next, val);
		return root;
	}
	
	// Searching
	static bool search(Node const *root, long val)
	{
		if(root == NULL) return false;
		if(root->data == val) return true;
		return search(root->next, val);
	}
	
	// Printing
	static void print(Node const *root)
	{
		printHelp(root);
		cout << endl;
	}
	
	// Destroying
	static void destroy(Node *root)
	{
		if(root == NULL) return;
		destroy(root->next);
		delete root;
	}
};