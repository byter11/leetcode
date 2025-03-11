class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        long long mn = 1e18, mx = 1e18;
        for(int x : nums) {
            if(x <= mn) mn = x;
            else if(x <= mx) mx = x;
            else return true;
        }
        return false;
    }
};
// 110 120 10 20