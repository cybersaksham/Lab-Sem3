#include "MaxHeap.h"
#include <fstream>
#include <sstream>

class PQHeap : public MaxHeap {
	MaxHeap heap;
	
public:	
	PQHeap() { this->heap = MaxHeap(); }
	
	bool empty() const { return this->heap.isEmpty(); }
	
	long top() const
	{
		if (this->heap.isEmpty()) return -1;
		return this->heap.top();
	}
	
	void insertRandom(string filename)
	{
		MyClock clock;
		clock.startClock();
		
		string line;
		ifstream ipFile(filename);
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				this->push(a);
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		
		clock.endClock();
		ofstream insertFile("insertHeap.txt");
		insertFile << clock.consumedTimeInSecond();
		clock.resetClock();
	}
	
	void searchRandoms(string filename)
	{
		MyClock clock;
		clock.startClock();
		
		string line;
		ifstream ipFile(filename);
		
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				bool isPresent = this->search(a);
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		
		clock.endClock();
		ofstream insertFile("searchHeap.txt");
		insertFile << clock.consumedTimeInSecond();
		clock.resetClock();
	}
	
	void deleteRandoms(string filename)
	{
		MyClock clock;
		clock.startClock();
		
		string line;
		ifstream ipFile(filename);
		
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				this->pop();
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		
		clock.endClock();
		ofstream insertFile("deleteHeap.txt");
		insertFile << clock.consumedTimeInSecond();
		clock.resetClock();
	}
	
	void changePriorityRandoms(string filename)
	{
		MyClock clock;
		clock.startClock();
		
		string line;
		ifstream ipFile(filename);
		
		if (ipFile.is_open())
		{
			while (getline(ipFile, line))
			{
				stringstream str(line);
				long a;
				str >> a;
				bool isPresent = this->search(a);
				if(isPresent)
				{
					this->heap.v.insert(this->v.begin(), a);
					this->heap.heapify(1);
				}
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		
		clock.endClock();
		ofstream insertFile("changeHeap.txt");
		insertFile << clock.consumedTimeInSecond();
		clock.resetClock();
	}
	
	bool search(long x) const { return this->heap.search(x); }
	
	void push(long x) { this->heap.insert(x); }
	
	void pop()
	{
		if (this->heap.isEmpty()) return;		
		this->heap.remove();
	}
};