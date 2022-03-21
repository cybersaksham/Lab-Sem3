#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

class BSTNode
{
	long data;
	BSTNode *left;
	BSTNode *right;

public:
	// Constructors
	BSTNode(long data = 0) : data(data), left(NULL), right(NULL) {}
	BSTNode(long data, BSTNode *left, BSTNode *right) : data(data), left(left), right(right) {}
	
	// Creating from file
	static BSTNode *createTree(string filename) {
		string line;
		ifstream ipFile(filename);
		BSTNode *root = NULL;
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				root = insert(root, a);
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		return root;
	}
	
	// Insert from file
	BSTNode *insertTree(string filename) {
		string line;
		ifstream ipFile(filename);
		BSTNode *root = this;
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				root = insert(root, a);
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		return root;
	}
	
	// Delete from file
	BSTNode *deleteTree(string filename) {
		string line;
		ifstream ipFile(filename);
		BSTNode *root = this;
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				root = remove(root, a);
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		return root;
	}
	
	// Inserting a node
    static BSTNode *insert(BSTNode *root, long data) {
        if (root == NULL) {
            BSTNode *newNode = new BSTNode(data);
            return newNode;
        }

        if (data < root->data) root->left = insert(root->left, data);
        else if (data > root->data) root->right = insert(root->right, data);

        return root;
    }

    // Deleting a node
    static BSTNode *remove(BSTNode *root, long data)
    {
        if (root == NULL) return root;

        if (data < root->data) root->left = remove(root->left, data);
        else if (data > root->data) root->right = remove(root->right, data);
        else {
            BSTNode *leftNode = root->left;
            BSTNode *rightNode = root->right;

            delete root;

            if (leftNode == NULL) return rightNode;
            if (rightNode == NULL) return leftNode;

            BSTNode *tmp = rightNode;
            while (tmp->left != NULL) tmp = tmp->left;

            BSTNode *newNode = new BSTNode(tmp->data);
            newNode->left = leftNode;
            newNode->right = remove(rightNode, tmp->data);
            return newNode;
        }

        return root;
    }
    
    // Inorder Traversal
    void inorderTraversal() const {
    	if(this->left) this->left->inorderTraversal();
    	cout << this->data << endl;
    	if(this->right) this->right->inorderTraversal();
    }
    
    // Destroy Tree
    void destroyTree() {
    	if(this->left) this->left->destroyTree();
    	if(this->right) this->right->destroyTree();
    	delete this;
    }
};
