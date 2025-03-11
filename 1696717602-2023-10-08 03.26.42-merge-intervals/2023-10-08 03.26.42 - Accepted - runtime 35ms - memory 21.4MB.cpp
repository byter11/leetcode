class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<vector<int>> res;
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b) {
            return a[0] < b[0];
        });

        for(int i=0; i<n; i++) {
            int l = i, r = i+1;
            while(l < n && r < n) {
                auto a = intervals[l], b = intervals[r];
                if(a[1] >= b[0]) {
                    if(a[1] <= b[1]) l = r;
                    r++;
                }
                else break;
                // [1, 10], [2, 3], [3, 4], [4, 12] ...
            }
            if(l >= n) l--;
            r--;
            
            res.push_back({intervals[i][0], max(intervals[l][1], intervals[r][1])});
            i = r;
        }
        
        return res;
    }
};