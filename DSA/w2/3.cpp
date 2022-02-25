#include <iostream>
using namespace std;

void swap(int *arr, int a, int b)
{
	int tmp = arr[a];
	arr[a] = arr[b];
	arr[b] = tmp;
}

void heapify(int *arr, int n, int ind)
{
	int maxInd = ind;
	
	int left = 2 * ind + 1;
	int right = 2 * ind + 2;
	
	if(left < n && arr[left] > arr[maxInd]) maxInd = left;
	if(right < n && arr[right] > arr[maxInd]) maxInd = right;
	
	if(maxInd != ind)
	{
		swap(arr, ind, maxInd);
		heapify(arr, n, maxInd);
	}
}

void heapSort(int *arr, int n)
{
	for(int i=n/2-1; i>=0; i--) heapify(arr, n, i);
	
	for(int i=n-1; i>=0; i--)
	{
		swap(arr, 0, i);
		heapify(arr, i, 0);
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
	
	heapSort(arr, n);
	
	cout << "Sorted array is" << endl;
	for(int i=0; i<n; i++) cout << arr[i] << " ";
	cout << endl;
	
	delete [] arr;
	
	return 0;
}
