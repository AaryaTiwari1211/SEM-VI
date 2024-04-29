// A person visited a stationary shop to buy stationary items. There are N items in the shop where the ith item has a quality rating Q[i] and price P[i]
// The person has decided to buy all the stationary items having a quality rating value greater than or equal to Y. Find the total cost of the stationary items, the person buys.
// Input Format
// The first line contains two space-separated integers N and Y — the number of items and the minimum quality rating an item should have.
// The second line contains N space-separated integers, the array Q, denoting the quality rating of each item.
// The third line contains N space-separated integers, the array P, denoting the price of each item.
// Constraints
// 1≤N,Y≤100
// 1≤Q[i],P[i]≤100
// Output Format
// Output on a new line, the total cost of all the stationary items, the person buys.
// Sample Input 0

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int n, y;
    cin >> n >> y;
    vector<int> q(n), p(n);

    for (int i = 0; i < n; i++)
    {
        cin >> q[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (q[i] >= y)
        {
            sum += p[i];
        }
    }
    cout << sum << endl;
    return 0;
}