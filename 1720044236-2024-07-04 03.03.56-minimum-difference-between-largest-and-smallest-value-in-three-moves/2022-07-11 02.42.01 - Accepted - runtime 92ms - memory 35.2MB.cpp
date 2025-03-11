class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() <= 3) return 0;
        
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        int mn = INT_MAX;
        
        for(int i=0; i<4; i++) {
            mn = min(mn, nums[n-1 - (3-i)] - nums[i]);
        }
        return mn;
    }
};