#include <fstream>
#include <sstream>
#include "MyClock.h"
#include "MyRandom.h"
using namespace std;

class Array
{
	long *arr;
	long *arr2;
    long *arr3;
	long size;
	MyClock *clock;
	MyRandom *random;
	
	void merge(long *arr, long n1, long n2, long m1, long m2)
	{
		long i = n1, j = m1, k = 0, size1 = n2 - n1 + 1, size2 = m2 - m1 + 1;
		long *arr2 = new long[size1 + size2];
		
		while(i <= n2 && j <= m2)
		{
			if(arr[i] < arr[j])
			{
				arr2[k] = arr[i];
				i++;
			}
			else if(arr[i] > arr[j])
			{
				arr2[k] = arr[j];
				j++;
			}
			else
			{
				arr2[k] = arr[i];
				arr2[k + 1] = arr[i];
				i++;
				j++;
				k++;
			}
			k++;
		}
		while(i <= n2)
		{
			arr2[k++] = arr[i++];
		}
		while(j <= m2)
		{
			arr2[k++] = arr[j++];
		}
		
		for(long x=0; x<size1+size2; x++) arr[x+n1] = arr2[x];
		delete arr2;
	}
	
	
	
	void mergeSortHelp(long *arr, long low, long high)
	{
		if(high <= low) return;
		
		long mid = low + (high - low) / 2;
		mergeSortHelp(arr, low, mid);
		mergeSortHelp(arr, mid + 1, high);
		merge(arr, low, mid, mid + 1, high);
	}
	
	void insertionSortHelp(long *arr, long n)
	{
		for(long i=1; i<n; i++)
		{
			long elem = arr[i], counter = i, j = i - 1;
			while(j >= 0 && arr[j] > elem)
			{
				long tmp = arr[j];
				arr[j] = arr[counter];
				arr[counter] = tmp;
				counter = j;
				j--;
			}
		}
	}

public:
	Array(long n)
	{
		this->arr = new long[n];
		this->arr2 = new long[n];
		this->arr3 = new long[n];
		this->size = n;
		this->clock = new MyClock();
		this->random = new MyRandom();
	}
	
	void storeToFile(string filename)
	{
		this->random->generateRandoms(this->size, filename);
	}
	
	void takeInput(string filename)
	{
		string line;
		ifstream ipFile(filename);
		if (ipFile.is_open())
		{
			long i = 0;
			while (getline(ipFile, line) && i < this->size)
			{
				stringstream str(line);
				str >> this->arr[i];
				str >> this->arr2[i];
				str >> this->arr3[i];
                i++;
			}
			ipFile.close();
		}
		else cout << "Cannot open file " << filename << endl;
	}
	
	void prlong() const
	{
		for(long i = 0; i < this->size; i++) cout << this->arr[i] << " ";
		cout << endl;
	}
	
	double shellSort()
	{
		clock->startClock();
		long gap = this->size / 2;
		while(gap > 0)
		{
			long i = gap;
			while(i < this->size)
			{
				long temp = this->arr[i];
				long j = i;
				while(j >= gap && this->arr[j - gap] > temp)
				{
					this->arr[j] = this->arr[j - gap];
					j -= gap;
				}
				this->arr[j] = temp;
				i++;
			}
			gap /= 2;
		}
		clock->endClock();
		double time_ = clock->consumedTimeInSecond();
		clock->resetClock();
		return time_;
	}
	
	double mergeSort()
	{
		clock->startClock();
		
		this->mergeSortHelp(this->arr2, 0, this->size);
		
		clock->endClock();
		double time_ = clock->consumedTimeInSecond();
		clock->resetClock();
		return time_;
	}
	
	double insertionSort()
	{
		clock->startClock();
		
		this->insertionSortHelp(this->arr3, this->size);
		
		clock->endClock();
		double time_ = clock->consumedTimeInSecond();
		clock->resetClock();
		return time_;
	}
	
	void destroy()
	{
		delete [] this->arr;
        delete [] this->arr2;
        delete [] this->arr3;
	}
};