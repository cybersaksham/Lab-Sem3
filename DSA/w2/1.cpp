#include <iostream>
using namespace std;

int main()
{
	int n;
	cout << "Enter no of elements = ";
	cin >> n;
	
	int *arr = new int[n];
	cout << "Enter elements" << endl;
	for(int i=0; i<n; i++) cin >> arr[i];
	
	int a;
	cout << "Enter element to search = ";
	cin >> a;
	
	int index = 0;
	while(index < n)
	{
		if(a == arr[index]) break;
		index++;
	}
	
	if(index < n) cout << "Found at index " << index << endl;
	else cout << "Not found" << endl;
	
	delete [] arr;

	return 0;
}
