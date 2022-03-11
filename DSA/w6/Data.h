#include <unordered_map>
#include <vector>
#include <fstream>
#include <sstream>
#include "MyClock.h"
using namespace std;

class Data
{
	unordered_map<string, vector<string>> name_map;
	unordered_map<string, vector<string>> file_map;
	
	bool checkPresent(vector<string> const &v, string val) const
	{
		for(int i=0; i<v.size(); i++)
		{
			if(v[i] == val) return true;
		}
		return false;
	}
	
public:
	Data() {}
	
	// Run Queries
	void runQueries(string filename)
	{
		ifstream ipFile(filename);
		ofstream opFile("times.txt");
		string line;
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				int op;
				string a, b;
				str >> op;
				str >> a;
				if(op == 2) str >> b;
				
				if(op == 0)
				{
					opFile << to_string(this->searchName(a)) << endl;
				}
				else if(op == 1) opFile << to_string(this->searchFile(a)) << endl;
				else if(op == 2) this->addFile(a, b);
				else if(op == 3) this->dltFile(a);
				else if(op == 4) this->dltUser(a);
			}
		}
		else cout << "Cannot open file " << filename << endl;
		ipFile.close();
		opFile.close();
	}
	
	// Search files for an user
	double searchName(string name) const
	{
		MyClock myCl;
		myCl.startClock();
		
		vector<string> tmp;
		if(this->name_map.count(name) > 0) tmp = name_map.at(name);
		
		myCl.endClock();
		
		if(tmp.size() == 0)
		{
			cout << "File not found" << endl;
			return myCl.consumedTimeInSecond();
		}
		
		for(int i=0; i<tmp.size(); i++)
		{
			cout << tmp[i] << " ";
		}
		
		cout << endl;
		return myCl.consumedTimeInSecond();
	}
	
	// Search users for a file
	double searchFile(string file) const
	{
		MyClock myCl;
		myCl.startClock();
		
		vector<string> tmp;
		if(this->file_map.count(file) > 0) tmp = this->file_map.at(file);
		
		myCl.endClock();
		
		if(tmp.size() == 0)
		{
			cout << "File not found" << endl;
			return myCl.consumedTimeInSecond();
		}
		
		for(int i=0; i<tmp.size(); i++)
		{
			cout << tmp[i] << " ";
		}
		
		cout << endl;
		return myCl.consumedTimeInSecond();
	}
	
	// Add a given file and corresponding user
	void addFile(string name, string file)
	{
		vector<string> tmp;
		if(this->name_map.count(name) > 0) tmp = this->name_map[name];
		
		vector<string> tmp2;
		if(this->file_map.count(file) > 0) tmp2= this->file_map[file];
		
		bool isPresent = this->checkPresent(tmp, file);
		if(isPresent) return;
		
		tmp.push_back(file);
		tmp2.push_back(name);
		
		this->name_map[name] = tmp;
		this->file_map[file] = tmp2;
	}
	
	// Delete all users of a file
	void dltFile(string file)
	{
		vector<string> tmp;
		if(this->file_map.count(file) > 0) tmp = this->file_map[file];
		
		for(int i=0; i<tmp.size(); i++)
		{
			string user = tmp[i];
			vector<string> tmp2;
			if(this->name_map.count(user) > 0) tmp2 = this->name_map[user];
			if(tmp2.size() == 0) continue;
			vector<string>::iterator it = tmp2.begin();
			while(it != tmp2.end())
			{
				if(*it == file) tmp2.erase(it);
				else it++;
			}
			
			this->name_map[user] = tmp2;
		}
		this->file_map.erase(file);
	}
	
	// Delete all files of an user
	void dltUser(string name)
	{
		vector<string> tmp;
		if(this->name_map.count(name) > 0) tmp = this->name_map[name];
		
		for(int i=0; i<tmp.size(); i++)
		{
			string file = tmp[i];
			vector<string> tmp2;
			if(this->file_map.count(file) > 0) tmp2 = this->file_map[file];
			if(tmp2.size() == 0) continue;
			vector<string>::iterator it = tmp2.begin();
			while(it != tmp2.end())
			{
				if(*it == name) tmp2.erase(it);
				else it++;
			}
			
			this->file_map[file] = tmp2;
		}
		this->name_map.erase(name);
	}
};
