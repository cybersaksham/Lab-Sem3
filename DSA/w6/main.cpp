#include <iostream>
#include "Data.h"
#include "MyRandom.h"
using namespace std;

int main()
{
	// Generate random names
	MyRandom random;
	random.generateQueries(1000000, "queries.txt");
	
	Data myData;
	myData.runQueries("queries.txt");
	myData.addFile("abc", "file1");
	myData.addFile("abc", "file2");
	myData.addFile("abd", "file1");
	myData.searchName("abc");
	myData.searchName("abd");
	myData.searchFile("file1");
	myData.searchFile("file2");
	myData.dltFile("file1");
	myData.dltUser("abd");
	myData.searchName("abc");
	myData.searchName("abd");
	myData.searchFile("file1");
	myData.searchFile("file2");
	
	return 0;
}
