#include <iostream>
using namespace std;

void bswap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int partition(int *arr, int low, int high)
{
    int pivot = low, i = low + 1, j = high;

    do
    {
        while (arr[i] <= arr[pivot])
            i++;
        while (arr[j] > arr[pivot])
            j--;
            

        if (j > i)
            bswap(&arr[i], &arr[j]);
    } while (j > i);
    bswap(&arr[j], &arr[pivot]);
    
    return j;
}

void quickSort(int *arr, int low, int high)
{
    if (low >= high)
        return;
    int pivot = partition(arr, low, high);
    quickSort(arr, low, pivot - 1);
    quickSort(arr, pivot + 1, high);
}

int main()
{
	int n;
	cout << "Enter size of array = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements" << endl;
	for (int i=0; i<n; i++) cin >> arr[i];
	
	quickSort(arr, 0, n - 1);
	
	cout << "Sorted Array:" << endl;
	for(int i=0; i<n; i++) cout << arr[i] << " ";
	cout << endl;
	
	return 0;
}
