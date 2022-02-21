#include <iostream>
using namespace std;

void merge(int *arr, int n1, int n2, int m1, int m2)
{
	int i = n1, j = m1, k = 0, size1 = n2 - n1 + 1, size2 = m2 - m1 + 1;
	int *arr2 = new int[size1 + size2];
	
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
	
	for(int x=0; x<size1+size2; x++) arr[x+n1] = arr2[x];
	delete arr2;
}

void mergeSort(int *arr, int low, int high)
{
	if(high <= low) return;
	
	int mid = low + (high - low) / 2;
	mergeSort(arr, low, mid);
	mergeSort(arr, mid + 1, high);
	merge(arr, low, mid, mid + 1, high);
}

int main()
{
	int n;
	cout << "Enter size of array = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements" << endl;
	for (int i=0; i<n; i++) cin >> arr[i];
	
	mergeSort(arr, 0, n - 1);
	
	cout << "Sorted Array:" << endl;
	for(int i=0; i<n; i++) cout << arr[i] << " ";
	cout << endl;
	
	return 0;
}
