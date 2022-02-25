#include <iostream>
using namespace std;

void selectionSort(int *arr, int n)
{
	for(int i=0; i<n-1; i++)
	{
		int minElem = arr[i], minInd = i;
		for(int j=i+1; j<n; j++)
		{
			if(minElem > arr[j])
			{
				minElem = arr[j];
				minInd = j;
			}
		}
		
		int tmp = arr[i];
		arr[i] = arr[minInd];
		arr[minInd] = tmp;
	}
}

int main()
{
	int n;
	cout << "Enter no of elements = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements" << endl;
	for(int i=0; i<n; i++) cin >> arr[i];
	
	selectionSort(arr, n);
	
	cout << "Sorted array is" << endl;
	for(int i=0; i<n; i++) cout << arr[i] << " ";
	cout << endl;
	
	delete [] arr;
	
	return 0;
}
