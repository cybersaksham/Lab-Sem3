#include <iostream>
#include <fstream>
#include "Array.h"
using namespace std;

int main()
{
	int ops[] = {100, 1000, 10000, 100000, 1000000, 10000000};
	int m = 6;
		
	for(int i=0; i<m; i++)
	{
		Array arr(ops[i]);
		arr.storeToFile("ip" + to_string(ops[i]) + ".txt");
		arr.takeInput("ip" + to_string(ops[i]) + ".txt");
		
		// Sorting will not sort original array - just for calculating time
		double time1 = arr.shellSort();
		double time2 = arr.insertionSort();
		double time3 = arr.mergeSort();
		
		ofstream file("time" + to_string(ops[i]) + ".txt");
		file << "Shell - " << to_string(time1) << "\n";
		file << "Merge - " << to_string(time2) << "\n";
		file << "Insertion - " << to_string(time3) << "\n";
		file.close();
		
		arr.destroy();
	}
	
	return 0;
}