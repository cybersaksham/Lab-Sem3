#include <iostream>
using namespace std;

void swap(int **arr, int a, int b)
{
	int *tmp = arr[a];
	arr[a] = arr[b];
	arr[b] = tmp;
}

void bubbleSort(int **arr, int m, int ind)
{
	for(int i=0; i<m-1; i++)
	{
		for(int j=1; j<m-i; j++)
		{
			if(arr[j][ind] < arr[j - 1][ind]) swap(arr, j, j - 1);
		}
	}
}

int main()
{
	int m, n;
	cout << "Enter no of rows = ";
	cin >> m;
	cout << "Enter no of columns = ";
	cin >> n;
	
	int **arr = new int*[m];
	cout << "Enter rows" << endl;
	for(int i=0; i<m; i++)
	{
		int *arr2 = new int[n];
		for(int j=0; j<n; j++) cin >> arr2[j];
		arr[i] = arr2;
	}
	
	for(int i=n-1; i>=0; i--) bubbleSort(arr, m, i);
	
	for(int i=0; i<m; i++)
	{
		for(int j=0; j<n; j++) cout << arr[i][j] << " ";
		cout << endl;
		delete [] arr[i];
	}
	
	delete [] arr;
	
	return 0;
}
