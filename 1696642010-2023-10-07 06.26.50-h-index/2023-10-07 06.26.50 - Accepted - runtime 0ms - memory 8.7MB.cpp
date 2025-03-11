class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        sort(citations.begin(), citations.end(), greater<int>());
        int i = 0;
        for(i; i<n; i++) {
            if(i >= citations[i]) break;
        }
        return i;
    }
};