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
	
	// Array of random numbers
	void generateRandoms(long n, string filename)
	{
		ofstream file(filename);
		for(int i=0; i<n; i++)
		{
			long num = this->generateOneRandom(0, 10 * n);
			file << num << "\n";
		}
		file.close();
	}
};