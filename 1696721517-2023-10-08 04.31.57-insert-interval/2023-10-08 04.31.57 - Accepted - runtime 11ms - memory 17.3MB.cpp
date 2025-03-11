class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int n = intervals.size();
        vector<vector<int>> res;
        int i = 0;
        for(i=0; i<n; i++) {
            if(intervals[i][0] >= newInterval[0]) break;
            res.push_back(intervals[i]);
        }

        int start = i;
        if(i > 0 && res[i-1][1] >= newInterval[0]) {
            res[i-1][1] = max(newInterval[1], res[i-1][1]);
            start = i-1;
        } else {
            res.push_back(newInterval);
        }

        for(i; i<n; i++) {
            if(res[start][1] >= intervals[i][0]) {
                res[start][1] = max(res[start][1], intervals[i][1]);
            } else {
                res.push_back(intervals[i]);
                start++;
            }
        }

        return res;
    }
};