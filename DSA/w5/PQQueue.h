#include <queue>
#include <fstream>
#include <sstream>

class PQQueue {
	queue<long> q;
	
public:
	PQQueue() { this->q = queue<long>(); }
	
	long size() const { return this->q.size(); }
	
	bool empty() const { return this->q.empty(); }
	
	long top() const
	{
		if (this->q.empty()) return -1;
		return this->q.front();
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
		ofstream insertFile("insertQueue.txt");
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
		ofstream insertFile("searchQueue.txt");
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
		ofstream insertFile("deleteQueue.txt");
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
				queue<long> q2;
				
				while (!this->q.empty() && this->q.front() < a)
				{
					q2.push(this->q.front());
					this->q.pop();
				}
				if(!this->q.empty()) this->q.pop();
				while (!this->q.empty())
				{
					q2.push(this->q.front());
					this->q.pop();
				}
				this->q = q2;
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
		
		clock.endClock();
		ofstream insertFile("changeQueue.txt");
		insertFile << clock.consumedTimeInSecond();
		clock.resetClock();
	}
	
	bool search(long x) const
	{
		queue<long> tmp = this->q;
		
		while (!tmp.empty())
		{
			if (tmp.front() == x) return true;
			tmp.pop();
		}
		
		return false;
	}
	
	void push(long x)
	{
		
		if (this->q.empty())
		{
			this->q.push(x);
			return;
		}
		
		queue<long> q2;
		
		while (!this->q.empty() && this->q.front() < x)
		{
			q2.push(this->q.front());
			this->q.pop();
		}
		
		q2.push(x);
		
		while (!this->q.empty())
		{
			q2.push(this->q.front());
			this->q.pop();
		}
		
		this->q = q2;
	}
	
	void pop()
	{
		if (this->q.empty()) return;		
		this->q.pop();
	}
};