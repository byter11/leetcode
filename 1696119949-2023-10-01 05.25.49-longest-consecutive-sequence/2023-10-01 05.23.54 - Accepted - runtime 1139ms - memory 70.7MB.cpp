class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0, n = nums.size();
        int mn = 1e9;
        int mx = -mn;
        unordered_map<int, int> s;

        for(int i=0; i<n; i++) {
            mn = min(mn, nums[i]);
            mx = max(mx, nums[i]);
            s[nums[i]] = i;
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