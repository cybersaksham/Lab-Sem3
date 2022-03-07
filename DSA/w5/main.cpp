#include <iostream>
#include <fstream>
#include "MyClock.h"
#include "MyRandom.h"
#include "PQQueue.h"
#include "PQHeap.h"
using namespace std;

int main()
{
	MyRandom myRandom;
	
	// Genereating random numbers
	cout << "Enter size to operate on = ";
	long n;
	cin >> n;
	myRandom.generateRandoms(n, "randoms.txt");
	
	// By Queue
	PQQueue myQueue;
	myQueue.insertRandom("randoms.txt");
	myQueue.searchRandoms("randoms.txt");
	myQueue.deleteRandoms("randoms.txt");
	myQueue.changePriorityRandoms("randoms.txt");
	
	// By Heap
	PQHeap myHeap;
	myHeap.insertRandom("randoms.txt");
	myHeap.searchRandoms("randoms.txt");
	myHeap.deleteRandoms("randoms.txt");
	myHeap.changePriorityRandoms("randoms.txt");
	
	return 0;
}