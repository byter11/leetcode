class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> order;
        for(int i=0; i<arr2.size(); i++) order[arr2[i]] = i;

        sort(arr1.begin(), arr1.end(), [&order](const int &a, const int &b) {
            int c = order.contains(a) ? order[a] : order.size() + a;
            int d = order.contains(b) ? order[b] : order.size() + b;

            return c < d;
        });

        return arr1;
    }
};