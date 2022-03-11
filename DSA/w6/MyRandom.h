#include <ctime>
#include <iostream>
#include <fstream>
#include <unistd.h>
using namespace std;

class MyRandom
{
public:
	MyRandom() { srand(time(0)); }
	
	int generateOneRandom(int start, int end)
	{
		return rand() % (end - start + 1) + start;
	}
	
	void generateQueries(int n, string filename)
	{
		ofstream file(filename);
		for(int i=0; i<n; i++)
		{
			// 0 for search user, 1 for search file
			// 2 for add file
			// 3 for delete file
			// 4 for delete user
			int op = this->generateOneRandom(0, 4);
			string s1 = this->generateString(this->generateOneRandom(1, 10));
			string s2 = this->generateString(this->generateOneRandom(1, 10));
			
			file << op << " " << s1;
			if(op == 2) file << " " << s2;
			file << endl;
		}
		file.close();
	}
	
	string generateString(int len)
	{
		static const char alphanum[] =
		   "0123456789"
		   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		   "abcdefghijklmnopqrstuvwxyz";
	   	string tmp_s;
	   	tmp_s.reserve(len);

		for (int i = 0; i < len; ++i) {
		   tmp_s += alphanum[rand() % (sizeof(alphanum) - 1)];
		}

		return tmp_s;
	}
};
