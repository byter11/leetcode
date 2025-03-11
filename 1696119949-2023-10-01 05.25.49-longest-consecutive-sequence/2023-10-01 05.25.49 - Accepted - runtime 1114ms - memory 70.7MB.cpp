class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0, n = nums.size();
        unordered_set<int> s;

        for(int i=0; i<n; i++) {
            s.insert(nums[i]);
        }

        for(int i=0; i<n; i++) {
            int x = nums[i];
            if(s.contains(x-1)) continue;
            while(s.contains(x)) {
                x++;
            }
            ans = max(ans, x - nums[i]);
        }
    
        return ans;
    }
};