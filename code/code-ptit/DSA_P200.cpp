// TODO:TLE
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

void quickSort(vector<int>& a, int low, int high) {
    if (low < high) {
        int pivotIdx = low + rand() % (high - low + 1);
        swap(a[pivotIdx], a[high]);
        int pivot = a[high];
        int i = low - 1;
        for (int j = low; j < high; ++j) {
            if (a[j] < pivot) {
                ++i;
                swap(a[i], a[j]);
            }
        }
        swap(a[i + 1], a[high]);
        int pi = i + 1;
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    srand(time(0));

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        quickSort(a, 0, n - 1);
        for (int i = 0; i < n; ++i) {
            cout << a[i];
            if (i < n - 1) cout << " ";
        }
        cout << "\n";
    }
    return 0;
}