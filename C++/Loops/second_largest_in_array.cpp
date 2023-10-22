#include <iostream>
#include <climits>
using namespace std;
int findSecondLargest(int *input,int size){
    if(size==0 ||size==1){
        return INT_MIN;
    }
    int s=INT_MIN;
    int l=input[0]; 
    for(int i=1;i<size;i++){
        if(input[i]>l){
            s=l;
            l=input[i];
        }
        else if(input[i]<l){
            if(input[i]>s && input[i]!=l){
                s=input[i];
            }
        }
    }
    return s;
}
int main()
{
	int t;
	cin >> t;
	while (t--)
	{

		int size;
		cin >> size;
		int *input = new int[size];

		for (int i = 0; i < size; i++)
		{
			cin >> input[i];
		}

		cout << findSecondLargest(input, size) << endl;

		delete[] input;
	}

	return 0;
}
