#include <iostream>
#include <fstream>
using namespace std;

class MyRandom
{
public:
	MyRandom() { srand(time(0)); }
	
	long generateOneRandom(long start, long end)
	{
		return rand() % (end - start + 1) + start;
	}
	
	// Array of operations & numbers
	// 0 for search, 1 for insert, 2 for delete
	long **generateOperations(long n, string filename)
	{
        ofstream file(filename);
		long** operations = new long*[n];
		for(int i=0; i<n; i++)
		{
			long op = generateOneRandom(0, 2);
			long num = generateOneRandom(0, 10 * n);
			long* newPair = new long[2];
			newPair[0] = op;
			newPair[1] = num;
			operations[i] = newPair;
            file << op << " " << num << "\n";
		}
        file.close();
		
		return operations;
	}
	
	void deleteOperations(long **ops, long n)
	{
		for(int i=0; i<n; i++) delete [] ops[i];
		delete [] ops;
	}
};