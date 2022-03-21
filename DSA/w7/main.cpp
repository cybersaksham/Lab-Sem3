#include <iostream>
#include <fstream>
#include "BST.h"
#include "MyRandom.h"
#include "MyClock.h"
using namespace std;

void writeToFile(string filename, string val) {
	ofstream file(filename);
	file << val << endl;
	file.close();
}

int main()
{
	int n;
	cout << "No of nodes in tree initially = ";
	cin >> n;
	
	// Initializing Clock
	MyClock clockTime;
	
	// Generating Randoms
	MyRandom randoms;
	randoms.generateRandoms(n, "random_nodes_" + to_string(n) + ".txt");
	randoms.generateRandoms(1000, "random_1000.txt");
	
	// Creating BST
	clockTime.startClock();
	BSTNode *root = BSTNode::createTree("random_nodes_" + to_string(n) + ".txt");
	clockTime.endClock();
	writeToFile("createTime_" + to_string(n) + ".txt", to_string(clockTime.consumedTimeInSecond()));
	clockTime.resetClock();
	
	root->inorderTraversal();
	
	// Inserting in BST
	clockTime.startClock();
	root = root->insertTree("random_1000.txt");
	clockTime.endClock();
	writeToFile("insertTime_" + to_string(n) + ".txt", to_string(clockTime.consumedTimeInSecond()));
	clockTime.resetClock();
	
	// Deleting in BST
	clockTime.startClock();
	root = root->deleteTree("random_1000.txt");
	clockTime.endClock();
	writeToFile("deleteTime_" + to_string(n) + ".txt", to_string(clockTime.consumedTimeInSecond()));
	clockTime.resetClock();
	
	// Destroying
	root->destroyTree();
	
	return 0;
}
