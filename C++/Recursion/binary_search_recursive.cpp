#include <iostream>
using namespace std;
int binarySearch1(int input[], int end, int start, int element)
{
    if (start > end)
    {
        return -1;
    }
    int mid = (start + end) / 2;
    if (input[mid] == element)
    {
        return mid;
    }
    if (input[mid] > element)
    {
        return binarySearch1(input, mid - 1, start, element);
    }
    if (input[mid] < element)
    {
        return binarySearch1(input, end, mid + 1, element);
    }
    return binarySearch1(input, end, start, element);
}
int binarySearch(int input[], int length, int element)
{
    int start = 0;
    return binarySearch1(input, length - 1, start, element);
}
int main()
{
    int input[100000], length, element, ans;
    cin >> length;
    for (int i = 0; i < length; i++)
    {
        cin >> input[i];
        ;
    }

    cin >> element;
    ans = binarySearch(input, length, element);
    cout << ans << endl;
}
