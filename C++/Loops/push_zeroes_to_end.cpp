#include <iostream>
using namespace std;
void pushZeroesEnd(int *a, int n)
{
    int i = 0;
    for (int j = 0; j < n; j++)
    {
        if (a[j] != 0)
        {
            a[i] = a[j];
            i++;
        }
    }
    while (i < n)
    {
        a[i] = 0;
        i++;
    }
}
int main()
{
    int n;
    cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    pushZeroesEnd(a, n);
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}
