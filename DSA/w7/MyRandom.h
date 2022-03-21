#include <ctime>
#include <iostream>
#include <fstream>
#include <unistd.h>
using namespace std;

class MyRandom
{
	long start;
public:
	MyRandom() {
		srand(time(0));
		this->start = 12568; // Minimum Seed
	}
	
	long generateOneRandom(long end) {
		return rand() % (end - this->start + 1) + this->start;
	}
	
	void generateRandoms(long n, string filename) {
		ofstream file(filename);
		for(int i=0; i<n; i++) {
			long val = this->generateOneRandom(n * 100);			
			file << val << endl;
		}
		file.close();
	}
};
