class Solution {
    vector<int> cache;
public:
    int rob(vector<int>& nums) {
        cache = vector<int>(nums.size()+1, -1);
        return dfs(nums, 0);
    }

    int dfs(vector<int>& nums, int i) {
        if(i >= nums.size()) return 0;

        if(cache[i] >= 0) return cache[i];

        cache[i] =  max(nums[i] + dfs(nums, i+2), dfs(nums, i+1));
        return cache[i];
    }
};