#include <iostream>
using namespace std;

int binarySearch(int const *arr, int a, int low, int high)
{
	if(low > high) return -1;
	
	int mid = low + (high - low) / 2;
	
	if(a < arr[mid]) return binarySearch(arr, a, low, mid - 1);
	else if(a > arr[mid]) return binarySearch(arr, a, mid + 1, high);
	else return mid;
}

int main()
{
	int n;
	cout << "Enter no of elements = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements in sorted order" << endl;
	for(int i=0; i<n; i++) cin >> arr[i];
	
	int a;
	cout << "Enter element to search = ";
	cin >> a;
	
	int index = binarySearch(arr, a, 0, n - 1);
	
	if(index != -1) cout << "Found at index " << index << endl;
	else cout << "Not found" << endl;
	
	delete [] arr;
	
	return 0;
}
