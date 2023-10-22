#include <iostream>
using namespace std;
void sumOfTwoArrays(int *input1, int size1, int *input2, int size2, int *output)
{
    int a = size1 - 1;
    int b = size2 - 1;
    int c = size1 > size2 ? size1 : size2;
    int carry = 0;
    output[0] = 0;
    while (a >= 0 && b >= 0)
    {
        int ans = input1[a] + input2[b] + carry;
        output[c] = ans % 10;
        carry = ans / 10;
        c--;
        a--;
        b--;
    }
    while (a >= 0)
    {
        int ans = input1[a] + carry;
        output[c] = ans % 10;
        carry = ans / 10;
        c--;
        a--;
    }
    while (b >= 0)
    {
        int ans = input2[b] + carry;
        output[c] = ans % 10;
        carry = ans / 10;
        c--;
        b--;
    }
    output[0] = carry;
}
int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int size1;
        cin >> size1;

        int *input1 = new int[size1];

        for (int i = 0; i < size1; ++i)
        {
            cin >> input1[i];
        }

        int size2;
        cin >> size2;

        int *input2 = new int[size2];

        for (int i = 0; i < size2; ++i)
        {
            cin >> input2[i];
        }

        int outsize = 1 + max(size1, size2);

        int *output = new int[outsize];

        sumOfTwoArrays(input1, size1, input2, size2, output);

        for (int i = 0; i < outsize; ++i)
        {
            cout << output[i] << " ";
        }

        delete[] input1;
        delete[] input2;
        delete[] output;
        cout << endl;
    }

    return 0;
}
