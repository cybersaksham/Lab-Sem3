#include <iostream>
using namespace std;

void insertionSort(int *arr, int n)
{
	for(int i=1; i<n; i++)
	{
		int elem = arr[i], counter = i, j = i - 1;
		while(j >= 0 && arr[j] > elem)
		{
			int tmp = arr[j];
			arr[j] = arr[counter];
			arr[counter] = tmp;
			counter = j;
			j--;
		}
	}
}

int main()
{
	int n;
	cout << "Enter size of array = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements" << endl;
	for (int i=0; i<n; i++) cin >> arr[i];
	
	insertionSort(arr, n);
	
	cout << "Sorted Array:" << endl;
	for(int i=0; i<n; i++) cout << arr[i] << " ";
	cout << endl;
	
	return 0;
}
