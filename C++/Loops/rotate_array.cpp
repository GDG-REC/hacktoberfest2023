#include <iostream>
using namespace std;
void rotate(int *input, int d, int size)
{
    if (size == 0)
    {
        return;
    }
    int t = d % size;
    if (t == 0)
    {
        return;
    }

    int b[t];
    for (int i = 0; i < t; i++)
    {
        b[i] = input[i];
    }
    int k = 0;
    for (int i = 0; i < size - t; i++)
    {
        input[i] = input[i + d];
        k++;
    }
    int l = 0;
    while (k < size)
    {
        input[k] = b[l];
        k++;
        l++;
    }
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

        for (int i = 0; i < size; ++i)
        {
            cin >> input[i];
        }

        int d;
        cin >> d;

        rotate(input, d, size);

        for (int i = 0; i < size; ++i)
        {
            cout << input[i] << " ";
        }

        delete[] input;
        cout << endl;
    }

    return 0;
}
